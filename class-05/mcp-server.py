from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="MCPSERVER", stateless_http=True)

docs = {
    "intro":"This is a simple example of a stateless MCP server" ,
    "readme": "This serverb supports basic MCP operations ",
    "guide": "Refer to the documentation for more details"
}

@mcp.resource("docs://document", mime_type="application/json")
def list_docs():
    """List of all docs"""
    # print(list(docs.keys()))
    return list(docs.keys())
    # return docs.get("intro")

@mcp.resource("docs://document/{doc_id}")
def read_docs(doc_id):
    """Read a specific doc"""
    return docs[doc_id]
mcp_app = mcp.streamable_http_app()