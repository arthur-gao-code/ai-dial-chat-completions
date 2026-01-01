import asyncio

from clients.client import DialClient
from clients.custom_client import CustomDialClient
from constants import DEFAULT_SYSTEM_PROMPT
from models.conversation import Conversation
from models.message import Message
from models.role import Role


async def start(stream: bool) -> None:
    #TODO:
    # 1.1. Create DialClient
    # (you can get available deployment_name via https://ai-proxy.lab.epam.com/openai/models
    #  you can import Postman collection to make a request, file in the project root `dial-basics.postman_collection.json`
    #  don't forget to add your API_KEY)
    dial_client = DialClient(
        deployment_name='gpt-4o',
    )

    # 1.2. Create CustomDialClient
    custom_dial_client = CustomDialClient(
        deployment_name='gpt-4o',
    )

    # 2. Create Conversation object
    conversation = Conversation()

    # 3. Get System prompt from console or use default -> constants.DEFAULT_SYSTEM_PROMPT and add to conversation
    #    messages.
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))

    # 4. Use infinite cycle (while True) and get yser message from console
    print("Type your question or 'exit' to quit.")
    while True:
        user_message = input("> ").strip()

    # 5. If user message is `exit` then stop the loop
        if user_message.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break

    # 6. Add user message to conversation history (role 'user')
        conversation.add_message(Message(Role.USER, user_message))

    # 7. If `stream` param is true -> call DialClient#stream_completion()
    #    else -> call DialClient#get_completion()
        print("AI:")
        if stream:
            ai_message = await custom_dial_client.stream_completion(conversation.get_messages())
        else:
            ai_message = custom_dial_client.get_completion(conversation.get_messages())

    # 8. Add generated message to history
        conversation.add_message(ai_message)

    # 9. Test it with DialClient and CustomDialClient
    # 10. In CustomDialClient add print of whole request and response to see what you send and what you get in response


asyncio.run(
    start(True)
)
