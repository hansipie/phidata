from phi.assistant import Assistant
from phi.llm.groq import Groq

from phi.tools.webrequests import WebRequestsTools


assistant = Assistant(
    llm=Groq(model="llama3-8b-8192"),
    tools=[WebRequestsTools()],
    show_tool_calls=True,
    description="Retrieve bitcoin price.",
    debug_mode=True, 
    markdown=True
)

try:
    assistant.print_response("Using an API call give me the actual bitcoin price.", stream=False)
except Exception as e:
    print(e)
