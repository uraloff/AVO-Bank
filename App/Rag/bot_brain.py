import os
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from App.Core.Settings import settings


# DB_PATH = "E:\\MyCodes\\PythonCodes\\TelegramBots\\AVObank\\App\\Rag\\chroma_db"
BASE_DIR = Path(__file__).resolve().parents[2] 

# Теперь строим железобетонные пути
KB_PATH = os.path.join(BASE_DIR, "App", "Rag", "KnowledgeBase")
DB_PATH = os.path.join(BASE_DIR, "App", "Rag", "chroma_db")


class AVOBrain:
    def __init__(self):
        # Подключаемся к готовой базе
        self.embedding_function = OpenAIEmbeddings(api_key=settings.AI_KEY)
        self.db = Chroma(persist_directory=DB_PATH, embedding_function=self.embedding_function)
        
        # Настраиваем модель
        # temperature=0 — КРИТИЧНО ВАЖНО для банка. Никакой фантазии.
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            api_key=settings.AI_KEY
        )

    async def get_answer(self, user_question: str):
        # 1. Поиск: ищем чуть больше кусков (k=4 или 5), чтобы повысить шансы
        results = self.db.similarity_search_with_score(user_question, k=4)

        # ИЗМЕНЕНИЕ: Поднимаем порог до 0.75 (или вообще убираем фильтр для теста)
        # Дистанция 0.75 для OpenAI embeddings — это "в целом про то же самое".
        relevant_docs = [doc for doc, score in results if score < 0.75]

        if not relevant_docs:
            print("❌ Все документы отфильтрованы по score!")
            return None 

        context_text = "\n\n---\n\n".join([doc.page_content for doc in relevant_docs])

        # 2. Улучшенный Промпт (English instructions + Russian content)
        # Инструкции на английском работают ЛУЧШЕ для моделей GPT, 
        # так как "под капотом" они думают на английском.
        
        PROMPT_TEMPLATE = """
        You are an official AI assistant for AVO Bank. 
        Your goal is to answer client questions using the context provided below.

        🛡️ SAFETY & BEHAVIOR RULES:
        1. **Core Truth:** Use ONLY the provided Context for banking facts (rates, limits, conditions).
        2. **Absurdity Check:** If the user asks something obviously wrong or absurd (e.g., "sell potatoes to get a card", "dance to open account"), politely REFUTE it using common sense, then state the ACTUAL rules from the Context.
        3. **No Hallucinations:** Do not invent new banking products or fees not listed in Context.
        4. **Retention:** If the user wants to leave/close account, add a retention message.

        🧠 Context from Knowledge Base:
        {context}

        ---

        🗣 User Question: {question}
        """

        prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        messages = prompt.format_messages(context=context_text, question=user_question)

        response = self.llm.invoke(messages)
        answer_text = response.content

        # Проверка на I_DONT_KNOW (иногда модель может добавить точку или пробел)
        if "I_DONT_KNOW" in answer_text:
            return None

        return answer_text