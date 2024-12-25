from griptape.artifacts import TextArtifact, ErrorArtifact
from griptape.falkordb_integration.tools.falkordb.falkordb_tool import FalkorDBTool


class TestFalkorDBTool:
    def test_execute_query_valid_input(self):
        """Test FalkorDBTool with a valid Cypher query."""
        valid_query = "CREATE (:Person {name: 'Alice', age: 30})"
        tool = FalkorDBTool(url="bolt://localhost:6379", graph_name="test_graph")
        params = {"values": {"query": valid_query}}
        result = tool.execute_query(params)
        assert isinstance(result, TextArtifact), "Expected TextArtifact instance"
        assert "Query executed successfully" in result.value, "Expected success message in result"

    def test_execute_query_return_results(self):
        """Test FalkorDBTool with a query that returns results."""
        valid_query = "MATCH (p:Person) RETURN p.name, p.age"
        tool = FalkorDBTool(url="bolt://localhost:6379", graph_name="test_graph")
        params = {"values": {"query": valid_query}}
        result = tool.execute_query(params)
        assert isinstance(result, TextArtifact), "Expected TextArtifact instance"
        assert "Result:" in result.value, "Expected result in the output"

    def test_execute_query_invalid_input(self):
        """Test FalkorDBTool with an invalid query."""
        invalid_query = None
        tool = FalkorDBTool(url="bolt://localhost:6379", graph_name="test_graph")
        params = {"values": {"query": invalid_query}}

        result = tool.execute_query(params)
        assert isinstance(result, ErrorArtifact), "Expected ErrorArtifact instance"
        assert (
            "Error executing query" in result.value
        ), "Expected error message in result"
