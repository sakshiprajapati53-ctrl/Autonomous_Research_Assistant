from typing import TypedDict
from langgraph.graph import StateGraph,END
from agents.planner_agent import planner_agent
from agents.researcher_agent import researcher_agent
from agents.critic import critic_agent
from agents.writer import writer_agent

class ResearchState(TypedDict):
    query: str
    tasks: str
    research: list
    critique: str
    final_report: str

def planner_node(state):
    tasks = planner_agent(state["query"])

    return {"tasks": tasks}

def research_node(state):
    