from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import PydanticOutputParser
from models.research_output import ResearchResponse  # Pydantic schema for structured output
from config import ANTHROPIC_API_KEY

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a technical writer. Summarize the research into a structured format.
The output should be a JSON object with the following structure:
{{
    "topic": "The main topic of the research",
    "summary": "A comprehensive summary of the research findings",
    "sources": ["List of sources used"],
    "tools_used": ["List of tools used in the research"]
}}"""),
    ("human", "{raw_research}"),
    ("placeholder", "{agent_scratchpad}")
])

writer_agent = create_tool_calling_agent(
    llm=ChatAnthropic(model="claude-3-5-sonnet-20241022", api_key=ANTHROPIC_API_KEY),
    tools=[],
    prompt=writer_prompt
)

writer_executor = AgentExecutor(agent=writer_agent, tools=[], verbose=True)
