from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool

# Create a search tool using DuckDuckGo
search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information"
)
