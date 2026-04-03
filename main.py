from agents.agent_flow import build_graph
from demo_jobs import jobs

graph = build_graph()

for job in jobs:
    print("\nProcessing job:", job)

    state = {
        "job_url": job
    }

    graph.invoke(state)