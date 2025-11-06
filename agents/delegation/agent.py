from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search


# specialist in summarisation
paper_summariser = Agent(
    name="paper_summariser",
    model="gemini-2.0-flash",
    description="Summarises academic papers.",
    instruction="Summarise the paper in 2-3 lines.",
)

# specialist in analysis/critique
research_analyst = Agent(
    name="research_analyst",
    model="gemini-2.0-flash",
    description="Analyse the methodology of the paper.",
    instruction="Analyse the paper, and its methodology."
)

# coordinator/router
coordinator = Agent(
    name="coordinator",
    model="gemini-2.0-flash",
    instruction=(
        "Use the paper summariser if "
        "the user wants to "
        "understand what's in the "
        "paper. Otherwise, use the "
        "research analyst for "
        "critiquing, etc."
    ),
    description="Main router for academic paper analysis.",
    sub_agents=[paper_summariser, research_analyst],
)

root_agent = coordinator
