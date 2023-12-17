from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    text_prompt = State()
    cinema_prompt = State()
    movie_time_prompt = State()
    Films_prompt = State()
    afisha_theater_prompt = State()