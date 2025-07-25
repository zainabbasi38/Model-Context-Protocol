# # with open("data.txt", "r") as file:
# #     content = file.read()
# #     print(content)
# #     with open("out.txt", "w") as file:
# #         con = file.write(content.upper())
# #         print(con)


# # import asyncio
# # from contextlib import asynccontextmanager

# # @asynccontextmanager
# # async def make_connections(name):
# #     print(f"Connecting... {name}")
# #     yield name
# #     print(f"Connected... {name}")


# # async def main():
# #     async with make_connections("A") as a:
# #         print(f"Using connection... {a}")


# # asyncio.run(main())


# import asyncio
# from contextlib import AsyncExitStack

# async def make_connections(name):
#     class ctx():
#         async def __aenter__(self):
#             print(f"ENTER... {name}")
#             return name
#         async def __aexit__(self, exc_type, exc, tb ):
#             print(f"EXIT... {name}")


#     return ctx()

# # async def main():
# #     async with await make_connections("A") as a:
# #         async with await make_connections("B") as b:

# #             print(f"Using connection... {a} and {b}")


# async def main():
#     async with AsyncExitStack() as stack:
#         a = await stack.enter_async_context(await make_connections("A"))
#         if a == "A":

#             b = await stack.enter_async_context(await make_connections("B"))
#             print(f"Using connection {a} and {b}")
#         async def customcleanup():
#             print("Custom cleanup logic here!")

#         stack.push_async_callback(customcleanup)
#         print(f"Doing work with {a} and {locals().get("b")}")
# asyncio.run(main())from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="first-mcp-server", stateless_http=True)

mcp_app = mcp.streamable_http_app()