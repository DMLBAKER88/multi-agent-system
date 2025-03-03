TOOL_REGISTRY = {}

def register_tool(name, func):
    TOOL_REGISTRY[name] = func

def call_tool(name, *args, **kwargs):
    if name not in TOOL_REGISTRY:
        raise ValueError(f"Tool {name} not found.")
    return TOOL_REGISTRY[name](*args, **kwargs)
