from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search


paper_search_agent = Agent(
    name="paper_search_agent",
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
root_agent = paper_search_agent
