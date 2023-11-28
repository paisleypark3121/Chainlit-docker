import chainlit as cl
from dotenv import load_dotenv
from typing import Optional
import os

@cl.on_chat_start
async def on_chat_start():
    load_dotenv()
    app_user = cl.user_session.get("user")
    await cl.Message(f"Hello {app_user.username}").send()

@cl.password_auth_callback
def auth_callback(username: str, password: str) -> Optional[cl.AppUser]:
    _username=os.environ.get('MY_USERNAME')
    _password=os.environ.get('MY_PASSWORD')
    if (username.upper(), password) == (_username, _password):
        return cl.AppUser(username=_username, role="USER", provider="credentials")
    else:
        return None

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()