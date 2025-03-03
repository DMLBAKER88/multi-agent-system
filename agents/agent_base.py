from loguru import logger
from message_queue import MessageQueue

class BaseAgent:
    def __init__(self, name, queue: MessageQueue):
        self.name = name
        self.queue = queue

    def run(self):
        raise NotImplementedError

    def log(self, msg):
        logger.info(f"[{self.name}] {msg}")

    def send_message(self, target_agent, content):
        self.queue.send_message(self.name, target_agent, content)

    def receive_messages(self):
        return self.queue.get_messages_for(self.name)
