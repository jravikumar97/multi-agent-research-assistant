from agents.research_agent import research_executor
from agents.writer_agent import writer_executor
from agents.save_agent import save_executor

def main():
    # Step 1: Get user query
    query = input("What do you want to research? ")

    # Step 2: Research Phase
    research_result = research_executor.invoke({"query": query})

    # Step 3: Writing Phase
    written_output = writer_executor.invoke({"raw_research": research_result["output"][0]["text"]})

    # Step 4: Save Phase
    save_executor.invoke({"final_text": written_output["output"][0]["text"]})

if __name__ == "__main__":
    main()