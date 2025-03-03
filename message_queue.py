from collections import defaultdict

class MessageQueue:
    def __init__(self):
        self.messages = defaultdict(list)

    def send_message(self, sender, recipient, content):
        self.messages[recipient].append({"from": sender, "content": content})

    def get_messages_for(self, agent_name):
        msgs = self.messages[agent_name]
        self.messages[agent_name] = []
        return msgs
