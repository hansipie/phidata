from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.webrequests import WebRequestsTools

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    tools=[WebRequestsTools()],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("Get me pikachu's stats using the pokeapi.")