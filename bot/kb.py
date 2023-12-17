from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="Выбрать дату", callback_data="take_data")],
    [InlineKeyboardButton(text="Фильм в кинотеатре", callback_data="Movie_time"),
    InlineKeyboardButton(text="Какие кинотеатры работают", callback_data="cinema")],
    [InlineKeyboardButton(text="Какие есть фильмы", callback_data="Films"),
    InlineKeyboardButton(text="Расписание фильмов в кинотеатре", callback_data="afisha_theater")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти в меню", callback_data="menu_1")]])