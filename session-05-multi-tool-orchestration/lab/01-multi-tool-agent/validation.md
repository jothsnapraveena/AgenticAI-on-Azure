# Validation

Run the notebook top to bottom, then confirm:

- [ ] `agent = agents_client.create_agent(...)` returns without error and prints an agent id.
- [ ] All three test questions return a `run.status` of `completed` (not `failed` or `requires_action`
      left hanging — `requires_action` stuck open usually means `enable_auto_function_calls` wasn't
      called before `create_agent`, or was called on a different toolset instance).
- [ ] The File Search question's answer mentions the 30-day window and free return shipping for
      defective items — both only exist in `return_policy.md`, so a correct answer proves retrieval
      actually happened, not the model guessing a generic policy.
- [ ] The Function Calling question's answer includes a specific dollar figure and day count that
      matches `get_shipping_estimate`'s math (base_cost = 12.5 + weight_kg * 3.2), not a generic
      "it depends on the carrier" non-answer.
- [ ] The Code Interpreter question correctly identifies Q4 as highest and Q1 as lowest, with the
      right dollar difference ($30,900).
- [ ] Section 8 (run steps) shows a tool call type matching the expected tool for each of the three
      runs. Record any mismatch — that's a real, useful finding for `session-notes.md`.

## What "cost-conscious skip" looks like here

If you don't want to run the full notebook live (Code Interpreter session charges), it's fine to run
through Section 5 (agent creation) and stop — that confirms the multi-tool `ToolSet` wiring works
without spending on the actual chat/code-execution runs. Note this as a skip in `session-notes.md`,
same pattern as Session 4.
