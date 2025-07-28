import os
from  dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP(name="first-mcp-server", stateless_http=True)

mcp_app = mcp.streamable_http_app()

load_dotenv()

@mcp.tool(name="Weather-Tool", description="This is a weather tool.")
async def weather(city: str):
    return f"Weather in {city} is sunny"

@mcp.tool(name="News-Tool", description="This is a news tool.")
async def get_news(news: str):
    return f"News about {news} is fantastic"

