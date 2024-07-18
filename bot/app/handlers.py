from aiogram import Router, Bot, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from .keyboards import START, profile
from .database.data import insert_user, get_user, update_user

router = Router()

GREETING = """
Hello👋.
Stay alert and get ready to tap $BLAZE! We are excited to announce that our project will launch on July 15th. Prepare for an amazing opportunity and join us for the launch!
Get ready to ignite your earnings with $BLAZE!

Join our communities:
Telegram [https://t.me/blazetoken_Community] $BLAZE Community
X [https://x.com/blaze_meme_coin] $BLAZE TOKEN
"""


class UserState(StatesGroup):
    username = State()
    amount = State()
    user_id = State()
    invited_friends = State()
    invited_friends_usernames = State()
    support_query = State()
    feedback = State()


WEB_APP_URL = "https://your-web-app.com/api/register"


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username if message.from_user.username else first_name

    user = get_user(user_id)

    if user is None:
        insert_user(user_id, username, first_name)

    # Data to send to web app (replace with relevant user data)
    data = {"username": username, "first_name": first_name, "last_name": last_name}

    # Send data to web app using an HTTP library
    await send_http_request(WEB_APP_URL, method="POST", json=data)

    await message.answer(GREETING, reply_markup=START)


@router.message(Command('profile'))
async def profile_command(message: Message, state: FSMContext):
    user_id = message.from_user.id

    user = get_user(user_id)

    if user:
        name, amount, invited_friends, invited_friends_usernames = user[2], user[3], user[4], user[5]
        friends_usernames_list = eval(invited_friends_usernames)
        friends_usernames_str = "\n".join(friends_usernames_list) if friends_usernames_list else "None"

        await message.answer(
            f"💎Your Profile Infoℹ️:\n\n🆔Your ID: {user_id}\n\n👤Your name: {name}\n\n🔥Coins: {amount} $BLZ\n\n👥Invited Friends: {invited_friends}\n\n📜Invited Friends' Usernames: {friends_usernames_str}\n\nInvite Friends and get 🔥5000000 $BLZ per invited friend",
            reply_markup=profile
        )
    else:
        await message.answer("Profile not found. Please start with /start")


@router.callback_query(lambda c: c.data == 'invite')
async def handle_invite(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    invited_user_id = callback_query.message.from_user.id
    invited_username = callback_query.message.from_user.username if callback_query.message.from_user.username else callback_query.message.from_user.first_name

    update_user(user_id, invited_friends_increase=1, amount_increase=5000000, invited_friends_username=invited_username)

    referral_link = f"https://t.me/tap_blaze_bot?start=invite_{user_id}"
    await callback_query.message.answer(f"👥 Invite your friends using this link:\n {referral_link}")

    await callback_query.answer()
