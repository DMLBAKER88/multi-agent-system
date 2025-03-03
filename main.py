from agent_manager import AgentManager
from memory.memory_manager import init_db
from utils.logging_setup import logger
import tools.web_scraper_tool

def main():
    logger.info("Starting multi-agent system.")
    init_db()

    manager = AgentManager()
    manager.run()

if __name__ == "__main__":
    main()
