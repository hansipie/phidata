from phi.assistant import Assistant
from phi.tools.webrequests import WebRequestsTools

assistant = Assistant(tools=[WebRequestsTools()], show_tool_calls=True)
assistant.print_response("send requests to a web API", markdown=True)
