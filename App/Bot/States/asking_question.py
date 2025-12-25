from aiogram.fsm.state import State, StatesGroup


class AskingQuestion(StatesGroup):
    asking_question = State()