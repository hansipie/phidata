from phi.assistant import Assistant
from phi.llm.groq import Groq

from phi.tools.dnslookup import DNSLookupTools

assistant = Assistant(
    llm=Groq(model="llama3-8b-8192"),
    tools=[DNSLookupTools()],
    show_tool_calls=True,
    description="Make DNS request to get hostnames or IPs.",
    debug_mode=True, 
    markdown=True
)

try:
    assistant.print_response("What is google.com's IP ? From this IP what is the attached hostname ?", stream=False)
except Exception as e:
    print(e)
