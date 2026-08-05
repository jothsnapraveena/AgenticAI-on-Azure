# Knowledge Check — Session 5

1. What does `ToolSet` do that passing a single tool's `.definitions` directly to `create_agent`
   doesn't handle?

2. Why does `enable_auto_function_calls` need to be called before `create_agent`, and what happens to
   a run if you forget it?

3. File Search requires a vector store as an intermediate step, unlike Code Interpreter or Function
   Calling. Why — what is the vector store actually doing that the other two tools don't need?

4. If you ask the agent a question that could plausibly be answered by two different attached tools,
   how would you actually confirm (not guess) which one it used?

5. Name one cost-relevant difference between Code Interpreter and File Search in terms of what keeps
   accruing charges after your code stops running.

6. `AuthorizationFailed` shows up even though your account has the Owner role on the resource group.
   What's the actual missing piece, and why doesn't Owner cover it?
