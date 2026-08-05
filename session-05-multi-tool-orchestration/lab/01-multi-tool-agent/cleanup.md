# Cleanup

The notebook's last cell handles this, but if it errors partway through or you stopped early, clean up
manually to avoid ongoing charges:

1. **Delete the agent**: `agents_client.delete_agent(agent.id)`
2. **Delete the vector store**: `agents_client.vector_stores.delete(vector_store.id)` — vector store
   storage has a small ongoing cost until deleted.
3. **Delete uploaded files**: both the CSV and the policy doc —
   `agents_client.files.delete(uploaded_csv.id)`, `agents_client.files.delete(uploaded_policy.id)`.
4. **Check for orphaned threads**: threads created during testing aren't billed directly, but if you're
   keeping the environment tidy, list and delete them via `agents_client.threads.list()`.

If you lost the notebook's variable references (e.g. kernel restarted), list and delete by name instead:

```python
for a in agents_client.list_agents():
    if a.name == "session5-multi-tool-agent":
        agents_client.delete_agent(a.id)

for vs in agents_client.vector_stores.list():
    if vs.name == "session5-policy-store":
        agents_client.vector_stores.delete(vs.id)
```
