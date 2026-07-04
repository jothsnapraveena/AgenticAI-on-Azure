# Knowledge Check: Foundry Fundamentals

Answer before moving to Session 2. No scoring — this is a self-check.

1. What is the relationship between a Foundry hub and a Foundry project?

2. If you set a Contributor role at the hub level, does it automatically apply to every project inside that hub? Why or why not is this useful?

3. Name one scenario where you'd want a new hub instead of a new project inside an existing hub.

4. What is the Operate tab used for, at a high level? (We go deeper in Sessions 7–8 — this just checks you know it exists and roughly why.)

5. True or false: Foundry is a completely new product unrelated to Azure OpenAI Studio or Azure AI Studio.

<details>
<summary>Answer key (expand after attempting)</summary>

1. A hub is the top-level governance container; a project is a workspace inside a hub where the actual building, evaluating, and deploying happens. One hub can hold multiple projects.
2. Yes — hub-level role assignments cascade down to all projects underneath. Useful when a team should have consistent access across everything they build.
3. When governance or billing boundaries differ — e.g., separate teams, separate cost centers, or separate compliance requirements.
4. The Operate tab is where fleet-level management happens — monitoring, governance, and control across agents/models/tools. Covered in depth in Session 7 (Control Plane) and Session 8 (Observability).
5. False — Foundry consolidates and evolves Azure OpenAI Studio, Azure AI Studio, and other prior services into one platform.

</details>
