# Troubleshooting

| Error | Likely cause | Fix |
|---|---|---|
| `AuthorizationFailed` on `create_agent` or file upload | Your role is Owner/Contributor but not Azure AI User/Developer. Owner/Contributor grant management actions, not the `agents/write` data action. | Ask your subscription admin for the **Azure AI User** or **Azure AI Developer** role on the project (not just the resource group). |
| `SubscriptionNotRegistered` for `Microsoft.CognitiveServices` | The resource provider isn't registered on your subscription. | `az provider register --namespace Microsoft.CognitiveServices`, then retry. |
| Run status stuck on `requires_action` | `enable_auto_function_calls(toolset)` wasn't called, or was called with a different `ToolSet` instance than the one passed to `create_agent`. | Call `enable_auto_function_calls` on the exact same `toolset` object you pass into `create_agent`, before creating the agent. |
| File Search answer is generic / doesn't reflect the uploaded policy text | Vector store wasn't finished indexing before the run, or `file_search_tool.vector_store_ids` doesn't match the created store's id. | Use `create_and_poll` (not `create`) for the vector store so it blocks until indexing completes. Double-check `vector_store.id` matches what's passed into `FileSearchTool(...)`. |
| Code Interpreter question fails or times out | Model/region doesn't support Code Interpreter, or the session hit its idle timeout. | Confirm Code Interpreter is supported for your model/region. Sessions are active up to 1 hour with a 30-minute idle timeout — don't leave long gaps between cells. |
| `ModuleNotFoundError: azure.ai.agents` | Package not installed, or an old `azure-ai-projects`-only environment. | `pip install azure-ai-agents azure-identity`. |
| Function tool never gets called even when the question clearly needs it | The function's docstring/type hints are missing or vague, so the model can't tell when to use it. | `FunctionTool` builds its schema from the function signature and docstring — keep both specific (see `get_shipping_estimate` for the pattern). |
