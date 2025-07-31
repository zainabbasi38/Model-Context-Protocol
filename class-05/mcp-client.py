import asyncio
import json
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession, types
from contextlib import AsyncExitStack
from typing import List
from pydantic import AnyUrl
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
    
    async def list_resources(self) -> List[types.Resource]:
        result : types.ListResourcesRequest= await self._sess.list_resources()
        # print("RESULT: ", result)
        return result
    async def list_resource_template(self)-> List[types.ResourceTemplate]:
        result : types.ListResourceTemplatesResult = await self._sess.list_resource_templates()
        print("LIST RESOURCES TEMPLATE ",result.__dict__)
        # print(result.resourceTemplates)
        return result.resourceTemplates


    async def read_resources(self, uri:str) -> types.ReadResourceRequest:
        _url = AnyUrl(uri)
        print("URL",_url)
        result =  await self._sess.read_resource(_url)
        print("REsult", result)
        response = result.contents[0]
        if isinstance(response ,types.TextResourceContents ):
            if response.mimeType == "application/json":
                try:
                    # print(json.loads(response.text))
                    return json.loads(response.text)
                
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON : {e}")
        # print("READ RESOURCES DICT",result.__dict__)
        


async def main():
    async with MCPClient("http://127.0.0.1:8000/mcp") as client:
        tools = await client.list_tools()
        print("Tools: ", tools)

        #Getting list resources
        resources = await client.list_resources()
        # print(resources)
        
        # temp_resources = resources[0].uri
        # read resources
        # read_resources = await client.read_resources(temp_resources)
        # print("READ RESOURCES  ",read_resources)  

        templates_resources = await client.list_resource_template()
        print("\n")
        print(templates_resources)
        print("\n")
        print(templates_resources[0].uriTemplate)
        uri_temp = templates_resources[0].uriTemplate.replace("{doc_id}", "readme")
        print(uri_temp)
        read_template_resource = await client.read_resources(uri_temp)
        print(read_template_resource)


asyncio.run(main())