from google.adk.agents.llm_agent import Agent


paper_key_idea_agent = Agent(
    name="paper_key_idea_agent",
    model="gemini-2.0-flash",
    description=(
        "Use the provided descriptions to extract the core idea of a paper."
    ),
    instruction=(
        "Your job is to extract the core ideas of the provided paper "
        "summaries. It should be not more than 2 lines; the very core of the "
        "idea is important. Just write the core idea. Nothing else."
    ),
)

root_agent = paper_key_idea_agent
