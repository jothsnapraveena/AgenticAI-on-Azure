# Knowledge Check: Foundry Models II — Deployment & Model Router

Answer these before checking the key.

1. What's the main tradeoff between Standard (pay-as-you-go) and Provisioned throughput deployments?
2. True or false: every model in the catalog supports every deployment type.
3. What does Model Router actually do differently from a standard single-model deployment?
4. What's the main downside of using Model Router compared to a fixed model deployment?
5. Why does cleanup matter more in this session than in Session 2?

<details>
<summary>Answer key</summary>

1. Standard offers flexibility and no upfront commitment but variable cost; Provisioned throughput offers predictable latency and cost but requires paying for reserved capacity whether or not it's fully used.
2. False — deployment type availability varies by model, confirmed back in Session 2.
3. It routes each incoming request to one of several underlying models based on the request's complexity, rather than always using the same fixed model.
4. Reduced predictability — you don't always know in advance which underlying model answered a given request, which can complicate debugging and compliance.
5. Session 2 was catalog browsing only — nothing was deployed, so nothing was billable. Session 3 actually deploys a model, which incurs real cost until it's cleaned up.

</details>
