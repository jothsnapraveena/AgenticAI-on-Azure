# Session 2: Foundry Models I — Catalog & Comparison

![Repository architecture](/images/2.png)

## What this session covers

The Foundry model catalog: what's in it, how models are organized, and how to compare models using benchmarks and evaluation metrics before picking one to deploy. This session stops short of deployment — that's Session 3 (Foundry Models II — Deployment & Model Router).

## Why it matters

Foundry's model catalog spans first-party Microsoft models, OpenAI models, and a large set of third-party and open-weight models (Meta, Mistral, DeepSeek, Anthropic, Cohere, and others) all surfaced through one catalog UI — over 11,000 models at time of writing. Picking the wrong model for a task is an easy way to overpay or under-deliver, and the catalog's benchmarks and comparison tools exist specifically to avoid that before you commit to a deployment.

## What you'll gain

By the end of this session, you will be able to:
- Navigate the Foundry model catalog and filter by collection, industry, capability, and task
- Read a model card and identify what actually differs between two candidate models
- Explain what a benchmark score actually measures, and where its limits are
- Understand the evaluation metric categories Foundry uses (Quality and Embeddings) and pick the right ones for your task
- Shortlist models for a given task using the catalog and the Model benchmarks tool, without deploying anything yet

## Benchmarks and evaluation metrics: the theory

### What a benchmark actually is

A benchmark is a standardized test: a fixed dataset plus a fixed scoring method, run against a model to produce a single comparable number. The value of a benchmark comes entirely from standardization — because every model is scored the same way on the same data, you can compare model A's score to model B's score and trust that the comparison means something. The moment a benchmark's dataset or scoring method changes, that trust resets; you can no longer compare an old score to a new one.

Benchmarks are proxies, not guarantees. A model that tops a reasoning benchmark today was tested on that benchmark's specific questions, not on your questions. A high score tells you a model is *capable* on that category of task; it does not tell you the model will perform identically on your data, your prompts, or your domain. Treat benchmark scores as a filter to build a shortlist, not as the final word on which model to deploy — that final word should come from testing your own shortlist against your own data (which is what the Playground in Session 3 is for).

### Why Foundry splits metrics into categories

Foundry's Model benchmarks tool groups its metrics into two evaluated categories — **Quality** and **Embeddings** — plus three operational categories: **Benchmark Cost**, **Latency**, and **Safety**. The split exists because "how good is this model" is not one question; it's several different questions depending on what the model is doing:

- **Quality** metrics evaluate free-form generation — chat responses, summaries, completions. These ask: is the output coherent, grammatically correct, relevant to the question, and grounded in the source material?
- **Embeddings** metrics evaluate a different task entirely — how well a model represents text as vectors for search, retrieval, ranking, and clustering. A model can be excellent at one and unremarkable at the other; they're not the same skill.
- **Benchmark Cost**, **Latency**, and **Safety** are not about output quality at all — they're operational and risk constraints that matter regardless of which task category you're in.

Picking metrics from the wrong category for your task is one of the most common ways to shortlist the wrong model. If your task is chat completion, plotting Embeddings metrics tells you nothing useful about how the model will perform for you.

### Quality category metrics

| Metric | What it measures |
|---|---|
| Quality index | Aggregate quality score — a single summary number rolling up the Quality sub-metrics below. |
| Coherence | Whether the output flows smoothly, reads naturally, and resembles human-like language. |
| Fluency | Grammatical proficiency — correct grammar, syntax, and vocabulary usage. |
| GPT similarity | Semantic similarity between a ground-truth answer and the model's generated response. |
| Groundedness | How well the generated answer aligns with the actual source data, rather than the model's own assumptions. |
| Relevance | How directly the generated response addresses the question actually asked. |

Use Quality metrics for chat, summarization, Q&A, content generation, and any task where the output is free-form text meant for a human to read.

### Embeddings category metrics

| Metric | What it measures |
|---|---|
| Embeddings index | Aggregate embeddings score — a single summary number rolling up the Embeddings sub-metrics below. |
| Accuracy | The average of dataset-level accuracies for the model. |
| F1 score | The weighted mean of precision and recall; 1 is perfect, 0 is worst. |
| Mean average precision (MAP) | How well a ranking/recommender system places the most relevant items at the top of results. Range 0-1, higher is better. |
| NDCG at 10 | Normalized Discounted Cumulative Gain — ranking quality against an ideal order, measured at the top 10 results. |
| Spearman correlation | Correlation based on cosine similarity; the standard metric for semantic textual similarity and summarization-embedding tasks. |
| V-measure | Clustering quality — the harmonic mean of homogeneity and completeness. Range 0-1, higher is better. |

Use Embeddings metrics for search, retrieval-augmented generation (RAG) retrieval quality, recommendation, and clustering tasks — not for evaluating raw chat output.

### The operational categories

- **Benchmark Cost** — a standardized cost figure (USD to benchmark quality datasets; lower is better) that lets you compare models on price using the same yardstick, separate from your own Azure deployment pricing.
- **Latency** — how fast the model responds; matters more for interactive or real-time applications than for batch processing.
- **Safety** — how the model scores on harmful, biased, or inappropriate content generation; a hard constraint for many production use cases regardless of how well the model scores elsewhere.

### Reading the comparison correctly

Foundry's Model benchmarks tool plots two metrics against each other as a scatter chart (e.g., Benchmark Cost vs. Quality index) and ranks each model in your selected set on both axes. Two things matter when reading this:

1. **The rank is relative to your selected model list, not the whole catalog.** A "Ranking No. 10/35" only means 10th out of the 35 models you chose to compare — add or remove models and the rank recalculates.
2. **There is rarely a single best point on the chart.** Comparing Cost against Quality (or Latency against Quality) almost always produces a tradeoff curve rather than one dominant model. Deciding where to sit on that curve is a judgment call based on your task's tolerance for cost, latency, or occasional lower-quality output — the tool surfaces the tradeoff, it doesn't resolve it for you.

## Prerequisites

- Completion of Session 1 (Foundry Fundamentals) — you should already have a Foundry project
- No deployment or billing setup needed for this session; it's read-only exploration



## Next session

Session 3: Foundry Models II — Deployment & Model Router.
