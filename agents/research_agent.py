from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from tools.search_tool import search_tool
from tools.wiki_tool import wiki_tool
from config import ANTHROPIC_API_KEY

research_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant. Use the tools to gather facts about the topic."),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
])

research_agent = create_tool_calling_agent(
    llm=ChatAnthropic(model="claude-3-5-sonnet-20241022", api_key=ANTHROPIC_API_KEY),
    tools=[search_tool, wiki_tool],
    prompt=research_prompt
)

research_executor = AgentExecutor(agent=research_agent, tools=[search_tool, wiki_tool], verbose=True)
