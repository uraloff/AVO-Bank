from aiogram.fsm.state import State, StatesGroup


class SendingPhoneNumber(StatesGroup):
    sending_phone_number = State()