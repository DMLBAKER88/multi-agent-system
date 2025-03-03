from loguru import logger

logger.add("agent_system.log", rotation="1 MB", level="INFO")
