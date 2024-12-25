import falkordb

from typing import Optional

class FalkorDBClient:
    def __init__(self, url: str, graph_name: str = "falkordb"):
        """Initialize FalkorDBClient with URL and graph name."""
        self.url = url
        self.graph_name = graph_name
        self.client: Optional[falkordb.FalkorDB] = None
        self.graph: Optional[falkordb.Graph] = None

    def create_client(self) -> None:
        """Create a FalkorDB client and initialize the graph."""
        try:
            self.client = falkordb.FalkorDB(url=self.url)
            self.graph = self.client.select_graph(self.graph_name)
        except Exception as e:
            raise RuntimeError(f"Could not create FalkorDB client: {str(e)}")

    def query(self, query: str) -> None:
        """Execute a Cypher query on the FalkorDB graph."""
        if not self.graph:
            raise RuntimeError("Graph client is not connected.")
        try:
            return self.graph.query(query).result_set # type: ignore
        except Exception as e:
            raise RuntimeError(f"Error executing query: {str(e)}")



