from tools.tool_registry import register_tool

def scrape_website(url):
    return f"Scraped fake content from {url}"

register_tool("scrape_website", scrape_website)
