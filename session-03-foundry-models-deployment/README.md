# Session 3: Foundry Models II — Deployment & Model Router

## What this session covers

Taking the model you shortlisted in Session 2 and actually deploying it: the deployment types Foundry offers, what Model Router is and when to use it instead of a single fixed model, and testing a live deployment in the Playground.

## Why it matters

A model sitting in the catalog does nothing for your application. Deployment is where cost, latency, and quota decisions become real and billable — the deployment type you pick changes both what you pay and how the model behaves under load. Model Router adds another layer of decision-making: instead of hard-coding one model, you can let Foundry route each request to whichever underlying model fits it best, trading a little predictability for potential cost and quality gains.

## What you'll gain

By the end of this session, you will be able to:
- Explain the difference between the deployment types Foundry offers and when each one applies
- Deploy your Session 2 shortlisted model into your Foundry project
- Explain what Model Router does differently from a standard single-model deployment
- Test a deployed model in the Playground using your own prompts
- Tear down a deployment cleanly to avoid ongoing charges

## Deployment types: the theory

Azure Foundry model deployments generally fall into a few categories, though exact naming and availability vary by model:

- **Standard (pay-as-you-go)** — you pay per token processed, with no upfront commitment. Best for variable or unpredictable traffic, and the natural default while you're still validating a use case.
- **Provisioned throughput** — you reserve a fixed amount of throughput capacity ahead of time, paid for whether or not you use it in full. This trades flexibility for predictable latency and predictable cost at high, steady volume — the opposite profile from Standard.
- **Serverless API** — available for some third-party and open-weight models; billed per token like Standard, but hosted and scaled entirely by the model provider's own serving infrastructure rather than dedicated Azure compute.

Not every model supports every deployment type — this was flagged back in Session 2 as something to check on the model card before committing to a choice here.

## Model Router: the theory

Model Router is a single deployable endpoint that sits in front of multiple underlying models and picks which one actually handles each incoming request, based on the request's complexity and the routing policy configured. The pitch is straightforward: send easy requests to a cheap, fast model and hard requests to a stronger, more expensive one, automatically, without your application code needing to know which model answered.

The tradeoff is predictability. With a single fixed model deployment, you always know exactly which model produced a given response, which matters for debugging, compliance, and consistent behavior. With Model Router, the model that answers can vary request to request — worth confirming whether Foundry's implementation logs which underlying model actually served a given call, since that matters for troubleshooting a production issue after the fact.

## Prerequisites

- Completion of Session 2 (Foundry Models I) — you should have a shortlisted primary model (and ideally a fallback) with your own comparison notes
- A Foundry project with available quota in your target region for the model you're deploying

## Out of scope for this session

Fine-tuning a deployed model, and the Agent Service sessions that build on top of a deployment, are covered later in the series. This session stops at "model is deployed and responding in the Playground."

## Next session

Session 4: covers the next topic in the Foundry Models / Agent Service sequence — to be finalized after this session is portal-verified.
