import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession, types
from contextlib import AsyncExitStack
from typing import List
class MCPClient:
    def __init__(self, url):
        self.url = url
        self.stack = AsyncExitStack()
        self._sess = None
    
        

    async def __aenter__(self):
        read, write, _ = await self.stack.enter_async_context(
            streamablehttp_client(self.url)
        )
        self._sess = await self.stack.enter_async_context(
            ClientSession(read, write)
        )
        await self._sess.initialize()
        return self

    async def __aexit__(self, *args):
        await self.stack.aclose()

    async def list_tools(self) -> List[types.Tool]:
        return (await self._sess.list_tools()).tools
    
    async def call_tools(self, tool_name, args: dict)-> types.CallToolResult:

        return await self._sess.call_tool(tool_name, arguments=args)

async def main():
    async with MCPClient("http://127.0.0.1:8000/mcp") as client:
        tools = await client.list_tools()
        print("Available Tools:")
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")

        # Call Weather-Tool
        print("\nCalling Weather-Tool...")
        weather_result = await client.call_tools("Weather-Tool", args={"city": "Lahore"})
        print("Weather result:", weather_result.content[0].text)

        # Call News-Tool
        print("\nCalling News-Tool...")
        news_result = await client.call_tools("News-Tool", args={"news": "AI"})
        print("News result:", news_result.content[0].text)


asyncio.run(main())