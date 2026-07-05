# Implementation Steps

## 1. Open the model catalog

In your Foundry project, go to **Model catalog** in the left navigation. You'll land on "Find the right model to build your custom AI solution" — a featured-models carousel, model leaderboards, a filter bar, and a search box over the full catalog (11,000+ models at time of writing).

## 2. Check the leaderboards first

Before filtering, glance at **Model leaderboards**. It ranks the catalog across four criteria: **Quality**, **Safety**, **Cost**, and **Throughput**, each with a top-3 list. This is a fast way to get a first-pass sense of what's currently strong on the axis you care about most, before you narrow with filters. Click **Browse leaderboards** for the full ranked list beyond the top 3 shown.

## 3. Filter by task

The filter bar uses these categories, left to right:
- **Collections**
- **Industry**
- **Capabilities**
- **Deployment options**
- **Inference tasks**
- **Fine-tuning tasks**
- **Licenses**

For the task you picked in the prerequisites step, start with **Inference tasks** (e.g., chat completion) and **Capabilities**, then narrow further with **Licenses** or **Deployment options** if those matter for your use case. Use the **Search** box below the filter bar if you already know part of a model name.

## 4. Shortlist 2-4 candidates

Don't try to compare the entire catalog. Pick 2-4 models that plausibly fit your task based on the filtered list and the leaderboard results from step 2.

## 5. Open each model card

For each shortlisted model, open its model card and note:
- Benchmark scores (and which benchmarks are shown — they vary by model)
- Context window size
- Licensing terms (commercial use, fine-tuning allowed, etc.)
- Available deployment types (standard, provisioned throughput, serverless — availability varies by model)
- Region availability

## 6. Use the Model benchmarks tool

From the catalog, the comparison tool is called **Model benchmarks** (you'll see the breadcrumb change to Model catalog / Model benchmarks). It works differently than a static side-by-side spec sheet:

- Use the **Popular tasks** quick filters (General knowledge, Question answering, Reasoning, Coding, Groundedness) to narrow the model pool to your task type
- Build a **Selected model** list on the left — add your shortlisted models plus a few others for context; the tool can hold many models at once (dozens), each shown as a colored dot
- Pick what you're plotting with the **X-axis** and **Y-axis** dropgrid under "Metrics to compare" — e.g., Benchmark Cost vs. Quality Index. This renders as a scatter plot, not a table. The dropdown groups metrics under categories (Quality, Embeddings, Benchmark Cost, Latency, Safety); see `08-metrics-glossary.md` for what each individual metric actually measures before you pick axes
- Hover any point to see that model's exact score on both axes plus its **rank out of your selected set** (e.g., "Ranking No. 10/35")
- Toggle **List view** (top-right) as an alternative to the scatter plot for a more compact layout — confirm the exact table format yourself the first time you use it, since this wasn't fully verified during scaffolding

This tool is genuinely more useful than a manual table for spotting tradeoffs (e.g., a model that's slightly behind on quality but meaningfully cheaper) since the scatter plot makes that visible at a glance.

## 7. Build a comparison table

Record what the Model benchmarks scatter plot showed you (scores and ranks on your chosen axes), plus anything it didn't cover (e.g., your own read on licensing fit):

```
| Model | Benchmark (relevant one) | Context window | License | Deployment types | Regions |
|---|---|---|---|---|---|
```

## 8. Pick a primary and a fallback

Narrow to one primary model for your task, and optionally one fallback in case of quota or region issues at deployment time (Session 3).
