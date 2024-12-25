from griptape.structures import Agent
from griptape.falkordb_integration.tools.falkordb import FalkorDBTool

falkordb_tool = FalkorDBTool(url="bolt://localhost:6379", graph_name="falkordb")

agent = Agent(tools=[falkordb_tool])

create_query = "CREATE (:Person {name: 'Alice', age: 30})"
agent.run(f"Use FalkorDBTool to execute query: '{create_query}'")

match_query = "MATCH (p:Person) RETURN p.name, p.age"
result = agent.run(f"Use FalkorDBTool to execute query: '{match_query}'")

print("Query Result:", result)
