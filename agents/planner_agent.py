from agents.agent_base import BaseAgent
from utils.llm_client import ask_llm

class PlannerAgent(BaseAgent):
    def run(self):
        self.log("Starting planning process.")
        task = ask_llm("What is the first step to plan a garden party?")
        self.send_message("ExecutorAgent", {"task": task})
        self.log(f"Planned task: {task}")
