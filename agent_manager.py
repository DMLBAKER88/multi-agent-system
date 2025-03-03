from agents.planner_agent import PlannerAgent
from message_queue import MessageQueue

class AgentManager:
    def __init__(self):
        self.queue = MessageQueue()
        self.agents = [PlannerAgent("PlannerAgent", self.queue)]

    def run(self):
        for agent in self.agents:
            agent.run()

        for agent in self.agents:
            messages = agent.receive_messages()
            for msg in messages:
                print(f"{agent.name} received: {msg}")
