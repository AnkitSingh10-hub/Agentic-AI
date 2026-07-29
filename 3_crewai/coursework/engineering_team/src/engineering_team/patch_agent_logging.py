from datetime import datetime
from functools import wraps

from crewai import Agent

# Save original method
_original_execute_task = Agent.execute_task


@wraps(_original_execute_task)
def execute_task_with_logging(self, *args, **kwargs):
    print("\n" + "=" * 90)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] LLM EXECUTION")
    print(f"Agent : {getattr(self, 'role', '<unknown>')}")

    # Different CrewAI versions store the model differently.
    llm = getattr(self, "llm", None)

    if hasattr(llm, "model"):
        model = llm.model
    elif hasattr(llm, "model_name"):
        model = llm.model_name
    else:
        model = str(llm)

    print(f"Model : {model}")

    task = kwargs.get("task")
    if task is not None:
        print(f"Task  : {getattr(task, 'description', '')[:120]}")

    print("=" * 90)

    return _original_execute_task(self, *args, **kwargs)


Agent.execute_task = execute_task_with_logging