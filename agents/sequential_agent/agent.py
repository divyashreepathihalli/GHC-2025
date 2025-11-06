from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.agents import SequentialAgent


paper_searcher_agent = Agent(
    name="paper_searcher_agent",
    model="gemini-2.0-flash",
    description=(
       "Uses Google Search to find relevant academic papers."
    ),
    instruction=(
        "You are a dedicated research librarian. You MUST use the Google "
        "Search tool to find the top 2 most relevant academic paper titles. "
        "These papers should be academic papers. Briefly describe these "
        "papers. Keep your answers short and brief."
    ),
    tools=[google_search],
    output_key="retrieved_papers",
)

paper_key_idea_agent = Agent(
    name="paper_key_idea_agent",
    model="gemini-2.0-flash",
    description=(
        "Use the provided descriptions to extract the core idea of a paper."
    ),
    instruction=(
        "Your job is to extract the core ideas of the "
        "provided paper summaries: {retrieved_papers}. It should be not more "
        "than 2 lines; the very core of the idea "
        "is important. Just write the core idea. "
        "Nothing else."
    ),
)

sequential_agent = SequentialAgent(
    name='sequential_agent',
    description=(
        "Executes a sequence of paper search, "
        "followed by extracting the key idea."
    ),
    sub_agents=[
        paper_searcher_agent, 
        paper_key_idea_agent
    ],
)

root_agent = sequential_agent
