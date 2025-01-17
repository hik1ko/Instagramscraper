from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from requester import instagram_requester, tiktok_requester

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {message.from_user.full_name}! Bu bot sizga Instagram va TikTok vediolarni yuklashga yordam beradi")


@main_router.message(F.text.startswith('https://www.instagram.com'))
async def instagram_video_sender(message: Message):
    photos, videos, caption = await instagram_requester(message.text)
    if photos:
        for photo in photos:
            await message.answer_photo(photo)
    if videos:
        for video in videos:
            await message.answer_video(video)
    await message.delete()
    await message.answer(caption)


@main_router.message(F.text.contains('tiktok.com'))
async def tiktok_sender(message: Message):
    video, music, title = await tiktok_requester(message.text)
    await message.answer_video(video)
    await message.answer(title)
    await message.answer_audio(music)
