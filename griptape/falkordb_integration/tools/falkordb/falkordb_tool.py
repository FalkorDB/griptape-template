from __future__ import annotations
from griptape.artifacts import TextArtifact, ErrorArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity
from schema import Schema, Literal
from attrs import define
from typing import Optional
from griptape.falkordb_integration.tools.falkordb.falkordb_client import FalkorDBClient


@define
class FalkorDBTool(BaseTool):
    url: str
    graph_name: str = "falkordb"
    client: Optional[FalkorDBClient] = None

    def __attrs_post_init__(self):
        """Initialize the FalkorDB client."""
        try:
            self.client = FalkorDBClient(url=self.url, graph_name=self.graph_name)
            self.client.create_client()
        except Exception as e:
            raise RuntimeError(f"Failed to initialize FalkorDB client: {e}")

    @activity(
        config={
            "description": "Execute a Cypher query on the FalkorDB graph",
            "schema": Schema(
                {Literal("query", description="The Cypher query to execute"): str}
            ),
        }
    )
    def execute_query(self, params: dict) -> TextArtifact | ErrorArtifact:
        """Execute a Cypher query and return the result."""
        query = params["values"].get("query")
        try:
            result = self.client.query(query) # type: ignore
            return TextArtifact(f"Query executed successfully. Result: {result}")
        except Exception as e:
            return ErrorArtifact(f"Error executing query: {e}")




