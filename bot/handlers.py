from aiogram import types, F, Router, flags
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import Gen
from aiogram.types.callback_query import CallbackQuery
import utils

import kb
import text

date = '20231230'
def change_date(date_now):
    global date
    date = date_now
router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "take_data")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.text_prompt)
    await clbck.message.edit_text(text.date_text)
    await clbck.message.answer(text.date_exit, reply_markup=kb.exit_kb)

@router.message(Gen.text_prompt)
async def take_data(msg: Message, state: FSMContext):
    prompt = msg.text
    change_date(prompt)
    mesg = await msg.answer(text.date_wait)
    global date
    await utils.take_data(date)
    await mesg.edit_text(text.parse_end,disable_web_page_preview=True)

@router.callback_query(F.data == "cinema")
async def cinema(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.cinema_prompt)
    await clbck.message.edit_text(text.Cinema_text)
    await clbck.message.answer(text.date_exit, reply_markup=kb.exit_kb)
@router.message(Gen.cinema_prompt)
async def take_data(msg: Message, state: FSMContext):
    ans = utils.cinema(date)
    out = ''
    for i in ans:
        out += i + '\n'
    await msg.answer(out)
    await msg.answer(text.parse_end,disable_web_page_preview=True)

@router.callback_query(F.data == "Movie_time")
async def Movie_time(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.movie_time_prompt)
    await clbck.message.edit_text(text.Movie_text)
    await clbck.message.answer(text.date_exit, reply_markup=kb.exit_kb)
@router.message(Gen.movie_time_prompt)
async def take_data(msg: Message, state: FSMContext):
    movie = msg.text
    ans = utils.movie_ans(movie,date)
    out = ''
    for i in ans:
        for j in i:
            out += str(j) + " "
        out+= '\n'
    await msg.answer(out)
    await msg.answer(text.parse_end,disable_web_page_preview=True)

@router.callback_query(F.data == "Films")
async def Films(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.Films_prompt)
    await clbck.message.edit_text(text.Films_text)
    await clbck.message.answer(text.date_exit, reply_markup=kb.exit_kb)
@router.message(Gen.Films_prompt)
async def take_data(msg: Message, state: FSMContext):
    ans = utils.Films(date)
    out = ''
    for i in ans:
        out += i + '\n'
    await msg.answer(out)
    await msg.answer(text.parse_end,disable_web_page_preview=True)

@router.callback_query(F.data == "afisha_theater")
async def afisha(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.afisha_theater_prompt)
    await clbck.message.edit_text(text.Films_text)
    await clbck.message.answer(text.date_exit, reply_markup=kb.exit_kb)
@router.message(Gen.afisha_theater_prompt)
async def take_data(msg: Message, state: FSMContext):
    theater = msg.text
    ans = utils.afisha(theater, date)
    out = ''
    for i in ans:
        for j in i:
            out += str(j) + " "
        out+= '\n'
    await msg.answer(out)
    await msg.answer(text.parse_end,disable_web_page_preview=True)

