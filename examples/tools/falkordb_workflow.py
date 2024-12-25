# import logging
# from griptape.artifacts import TextArtifact
# from griptape.structures import Pipeline
# from griptape.falkordb_integration.tools.falkordb.falkordb_tool import FalkorDBTool  # type: ignore
# from griptape.falkordb_integration.tasks.process_result_task import ProcessResultTask  # type: ignore

# logging.basicConfig(level=logging.INFO, format="%(message)s")

# url = "bolt://localhost:6379"

# falkordb_task = FalkorDBTool(url=url, graph_name="falkordb")
# process_result_task = ProcessResultTask()

# pipeline = Pipeline(tasks=[falkordb_task, process_result_task])  # type: ignore

# falkordb_task.context["input"] = TextArtifact(
#     "CREATE (:Person {name: 'Alice', age: 30})"  # type: ignore
# )
# pipeline.run()

# falkordb_task.context["input"] = TextArtifact("MATCH (p:Person) RETURN p")  # type: ignore
# pipeline.run()

# result = process_result_task.output

# if result:
#     logging.info("Final Processed Result: %s", result.to_text())
# else:
#     logging.error("No output was produced by the task.")


from griptape.structures import Agent
from griptape.falkordb_integration.tools.falkordb import FalkorDBTool

falkordb_tool = FalkorDBTool(url="bolt://localhost:6379", graph_name="falkordb")

agent = Agent(tools=[falkordb_tool])

create_query = "CREATE (:Person {name: 'Alice', age: 30})"
agent.run(f"Use FalkorDBTool to execute query: '{create_query}'")

match_query = "MATCH (p:Person) RETURN p.name, p.age"
result = agent.run(f"Use FalkorDBTool to execute query: '{match_query}'")

print("Query Result:", result)
