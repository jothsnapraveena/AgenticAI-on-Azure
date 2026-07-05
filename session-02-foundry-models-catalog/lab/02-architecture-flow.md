# Architecture & Flow

## Where the catalog sits

The model catalog lives inside a Foundry project, under the "Model catalog" tab. It's a shared catalog across all projects in your tenant — nothing project-specific is applied until you actually deploy a model from it (which is Session 3).

## What's in the catalog

The catalog page opens with a featured-models carousel and a **Model leaderboards** panel (Quality, Safety, Cost, Throughput), then the full searchable/filterable catalog below — over 11,000 models at time of writing, spanning first-party Microsoft models, OpenAI models, and third-party/open-weight models from providers like Meta, Mistral, DeepSeek, Anthropic, Cohere, and others, each published by their respective provider.

## The filter bar

The catalog's filter bar is organized by: **Collections**, **Industry**, **Capabilities**, **Deployment options**, **Inference tasks**, **Fine-tuning tasks**, **Licenses** — plus a free-text search box. This is a different organizing structure than a generic "provider / modality / task" split; it's built around what you're trying to do (deploy, fine-tune, license terms) as much as what the model is.

## The comparison flow

```
Task in mind
    -> Scan leaderboards for a first-pass signal (Quality / Safety / Cost / Throughput)
    -> Filter catalog (Collections / Industry / Capabilities / Deployment options / Inference tasks / Fine-tuning tasks / Licenses)
    -> Shortlist 2-4 candidate models
    -> Open Model benchmarks: pick a Popular task filter, load a selected-model list, choose X/Y axis metrics, read the scatter plot (or switch to List view for a table)
    -> Compare: benchmarks, context window, licensing, deployment types, region availability
    -> Narrow to 1 (or 1 primary + 1 fallback)
```

This flow ends at a shortlist. It does not deploy anything — deployment and Model Router are covered in Session 3.
