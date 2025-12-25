import os
from pathlib import Path

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader

from App.Core.Settings import settings # Твой конфиг


BASE_DIR = Path(__file__).resolve().parents[2] 

# Теперь строим железобетонные пути
KB_PATH = os.path.join(BASE_DIR, "App", "Rag", "KnowledgeBase")
DB_PATH = os.path.join(BASE_DIR, "App", "Rag", "chroma_db")


def build_index():
    print("🔄 Начинаю индексацию базы знаний...")

    # 1. Загружаем документы (поддерживает txt, md)
    documents = []
    
    # 1. Загружаем PDF (тарифов)
    # Ищем все файлы .pdf в папке
    if os.path.exists(KB_PATH):
        for filename in os.listdir(KB_PATH):
            file_path = os.path.join(KB_PATH, filename)
            
            if filename.endswith(".pdf"):
                print(f"📚 Загружаю PDF: {filename}")
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())
                
            elif filename.endswith(".txt") or filename.endswith(".md"):
                print(f"📝 Загружаю текст: {filename}")
                loader = TextLoader(file_path, encoding='utf-8')
                documents.extend(loader.load())

    if not documents:
        print("❌ Папка KnowledgeBase пуста!")
        return

    # 2. Режем текст на кусочки (Chunks)
    # Это важно: если кусок слишком большой, модель запутается. 
    # Если слишком маленький — потеряется смысл. 1000 символов — ок для старта.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200, # Перекрытие, чтобы не резать предложения посередине смысла
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"📄 Создано {len(chunks)} фрагментов текста.")

    # 3. Создаем векторы (Embeddings) через OpenAI
    # Это превращает текст "Комиссия 0%" в набор чисел [0.123, -0.534...]
    embeddings = OpenAIEmbeddings(api_key=settings.AI_KEY)

    # 4. Сохраняем в локальную БД Chroma
    if os.path.exists(DB_PATH):
        # Если база уже есть, удаляем старую (для MVP проще пересоздать)
        import shutil
        shutil.rmtree(DB_PATH)

    db = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=DB_PATH
    )
    # В новых версиях Chroma сохранение автоматическое, но на всякий случай
    print("✅ База знаний успешно создана и сохранена!")

if __name__ == "__main__":
    build_index()