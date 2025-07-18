from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="first-mcp-server", stateless_http= True)

mcp_app = mcp.streamable_http_app()

@mcp.tool()
def weather(city: str):
    return f"The weathr in {city} is sunny"