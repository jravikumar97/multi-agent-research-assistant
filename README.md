# Research AI Agent

A multi-agent system that helps with research tasks by breaking down the process into three specialized agents: research, writing, and saving.

## Overview

This project implements a research assistant that uses multiple AI agents to:
1. Research a topic using various tools
2. Structure and format the research findings
3. Save the results to a file

## Components

### Agents

1. **Research Agent**
   - Uses search and Wikipedia tools to gather information
   - Collects facts and data about the specified topic

2. **Writer Agent**
   - Takes the raw research and structures it into a clear format
   - Creates a comprehensive summary with sources and tools used

3. **Save Agent**
   - Handles saving the final output to a file
   - Manages file operations and storage

### Tools

- Search Tool: Performs web searches for information
- Wikipedia Tool: Accesses Wikipedia articles
- Save Tool: Handles file operations

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd research-AI-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Anthropic API key:
```
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

Run the main script:
```bash
python main.py
```

When prompted, enter your research query. The system will:
1. Research the topic using available tools
2. Structure and format the findings
3. Save the results to a file

## Project Structure

```
research-AI-agent/
├── agents/
│   ├── research_agent.py
│   ├── writer_agent.py
│   └── save_agent.py
├── tools/
│   ├── search_tool.py
│   ├── wiki_tool.py
│   └── save_tool.py
├── models/
│   └── research_output.py
├── main.py
├── config.py
├── requirements.txt
└── .env
```

## Dependencies

- langchain
- langchain-anthropic
- anthropic
- python-dotenv
- pydantic
- duckduckgo-search# multi-agent-research-assistant
