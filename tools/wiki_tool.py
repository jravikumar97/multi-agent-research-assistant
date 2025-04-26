from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain.tools import Tool

# Wikipedia API Wrapper
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

wiki_tool = Tool(
    name="wiki_search",
    func=wiki_tool.run,
    description="Search Wikipedia for information"
)
