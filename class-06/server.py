from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP(stateless_http=True)

docs = {
    "intro":"This is a simple example of a stateless MCP server" ,
    "readme": "This serverb supports basic MCP operations ",
    "guide": "Refer to the documentation for more details"
}
@mcp.prompt(name="format", description="Format the document into markdown")
def format_doc(doc_id) -> list[base.Message]:
    prompt = f"Format this simple plain text {doc_id} into markdown format with adding headings and explanation"
    return [base.UserMessage(prompt)]


mcp_app = mcp.streamable_http_app()