from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from tools.save_tool import save_tool
from config import ANTHROPIC_API_KEY

save_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a saving agent. Use the tool to save the content to a file."),
    ("human", "{final_text}"),
    ("placeholder", "{agent_scratchpad}")
])

save_agent = create_tool_calling_agent(
    llm=ChatAnthropic(model="claude-3-5-sonnet-20241022", api_key=ANTHROPIC_API_KEY),
    tools=[save_tool],
    prompt=save_prompt
)

save_executor = AgentExecutor(agent=save_agent, tools=[save_tool], verbose=True)
