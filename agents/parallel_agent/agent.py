from google.adk.agents.llm_agent import Agent
from google.adk.agents import ParallelAgent
from google.adk.tools import google_search

cv_researcher_agent = Agent(
    name="cv_researcher_agent",
    model="gemini-2.0-flash",
    description="Uses Google Search to find relevant academic papers.",
    instruction=(
        "You are a Computer Vision researcher. "
        "Research the latest techniques in "
        "Computer Vision. Use the provided Google "
        "Search tool. Summarise your key findings "
        "briefly (2-3 lines)."
    ),
    tools=[google_search],
    output_key="cv_research",
)

nlp_researcher_agent = Agent(
    name="nlp_researcher_agent",
    model="gemini-2.0-flash",
    description="Uses Google Search to find relevant academic papers.",
    instruction=(
        "You are a NLP researcher. "
        "Research the latest techniques in "
        "NLP. Use the provided Google "
        "Search tool. Summarise your key findings "
        "briefly (2-3 lines)."
    ),
    tools=[google_search],
    output_key="nlp_research",
)

parallel_researcher_agent = ParallelAgent(
    name="parallel_researcher",
    sub_agents=[
        cv_researcher_agent,         
        nlp_researcher_agent
    ],
    description=(
        "Runs multiple research agents "
        "in parallel to gather "     
        "information."
    )
)

merger_agent = Agent(
    name="merger_agent",
    model="gemini-2.0-flash",
    description="Finds the intersection of NLP and CV research.",
    instruction=(
        "You are responsible for combining research findings and summarising "
        "them. In particular, your job is to find the intersection of "
        "research happening in the NLP and CV worlds. It is important that "
        "your answer is sourced only from the text given below: "
        "{cv_research}\n{nlp_research}.\nDo not source your answer from "
        "anywhere else."
    ),
)

root_agent = SequentialAgent(
    name="sequential_agent",
    description="Perform parallel research and summarise those results.",
    sub_agents=[parallel_researcher_agent, merger_agent],
)
