from .graph import build_graph

class Agent:
    def __init__(self, enable_feedback_node=True):
        self.__graph = build_graph(enable_feedback_node)

    def run(self, task: str, thread_id: str):
        initial_state = {
            "task": task,
        }
        config = {"configurable": {"thread_id": thread_id}}
        try:
            result = self.__graph.invoke(initial_state, config=config)
        except Exception as e:
            raise ValueError(f"Agent execution failed: {e}")
        return result
