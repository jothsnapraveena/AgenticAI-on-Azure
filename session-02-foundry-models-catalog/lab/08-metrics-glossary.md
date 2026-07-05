# Metrics Glossary (Model Benchmarks Tool) — Technical Reference

This is a working reference for actually using each metric in the Model benchmarks tool. 

## UI navigation path

X-axis / Y-axis dropdown → top-level category → sub-metric:

```
Quality
  └─ Quality index
  └─ Coherence
  └─ Fluency
  └─ GPT similarity
  └─ Groundedness
  └─ Relevance

Embeddings
  └─ Embeddings index
  └─ Accuracy
  └─ F1 score
  └─ Mean average precision
  └─ NDCG at 10
  └─ Spearman correlation
  └─ V-measure

Benchmark Cost   (flat, no sub-menu)
Latency          (flat, no sub-menu)
Safety           (flat, no sub-menu)
```

## Quick reference table

| Metric | Category | Range | Direction | Requires ground truth? |
|---|---|---|---|---|
| Quality index | Quality | Model-defined composite | Higher better | No (aggregate of below) |
| Coherence | Quality | Typically 1-5 scale | Higher better | No — judged on output alone |
| Fluency | Quality | Typically 1-5 scale | Higher better | No — judged on output alone |
| GPT similarity | Quality | 0-1 (cosine-based) | Higher better | Yes — needs a reference answer |
| Groundedness | Quality | Typically 1-5 scale | Higher better | Yes — needs source/context document |
| Relevance | Quality | Typically 1-5 scale | Higher better | Yes — needs the original question |
| Embeddings index | Embeddings | Model-defined composite | Higher better | No (aggregate of below) |
| Accuracy | Embeddings | 0-1 | Higher better | Yes — needs labeled data |
| F1 score | Embeddings | 0-1 | Higher better | Yes — needs labeled data |
| Mean average precision | Embeddings | 0-1 | Higher better | Yes — needs relevance judgments |
| NDCG at 10 | Embeddings | 0-1 | Higher better | Yes — needs relevance judgments, ranked |
| Spearman correlation | Embeddings | -1 to 1 | Higher (closer to 1) better | Yes — needs similarity labels |
| V-measure | Embeddings | 0-1 | Higher better | Yes — needs true cluster labels |
| Benchmark Cost | Operational | USD | Lower better | No |
| Latency | Operational | ms or seconds | Lower better | No |
| Safety | Operational | Model-defined score | Higher (safer) better | No |

Note: the "1-5 scale" ranges for Coherence, Fluency, Groundedness, and Relevance reflect the common Likert-style pattern used by LLM-as-judge evaluators; Foundry may normalize these for display, so treat the scale as approximate rather than confirmed portal behavior — check the actual axis values when you plot.

## Per-metric pitfalls

- **Coherence / Fluency** — these are usually scored by another LLM acting as judge, not a fixed formula. Two runs can produce slightly different scores even on the same output. Don't treat small differences (e.g., 4.1 vs 4.3) as meaningful.
- **GPT similarity** — sensitive to how close your reference answer is worded to a "typical" answer. A technically correct but differently-phrased response can score lower than a mediocre response that happens to match the reference's wording.
- **Groundedness** — only as good as the source document you evaluate against. If your real use case's source documents differ in structure or length from the benchmark's, don't assume the same groundedness score will hold.
- **Relevance** — can be high even when the answer is factually wrong, since relevance measures "on-topic," not "correct." Always pair Relevance with Groundedness or Accuracy, never read it alone.
- **F1 score** — a single F1 number hides the precision/recall split. A model can hit the same F1 by being overcautious (high precision, low recall) or overeager (low precision, high recall) — these behave very differently in production. Check precision and recall separately if the model card exposes them.
- **Mean average precision / NDCG at 10** — both depend heavily on how many relevant items exist in the underlying test set. Comparing MAP or NDCG across two different benchmark datasets is not valid, even if both are called "MAP."
- **Spearman correlation** — a correlation, not an accuracy score. A high Spearman correlation with a systematic offset (the model is consistently too generous or too harsh) will still score well, since correlation only checks relative ordering.
- **V-measure** — can be pushed to 1.0 by creating one cluster per item (perfect completeness, trivial homogeneity gaming) on unrealistic test setups. Sanity check the number of clusters used in the underlying evaluation if this metric looks suspiciously high.
- **Benchmark Cost** — this is Foundry's standardized cost to run the benchmark suite, not your production cost. Your actual cost depends on your deployment type, region, and traffic volume — recheck at deployment time in Session 3.
- **Latency** — benchmark latency is measured under the benchmark's own load conditions, not yours. Treat it as directional, not a guarantee of your production response times.
- **Safety** — a model scoring well on Foundry's Safety metric is not a substitute for your own content-safety layer (e.g., Azure AI Content Safety) if your application has specific compliance requirements.

## Picking a metric pair for common tasks

| Task | Suggested X-axis | Suggested Y-axis |
|---|---|---|
| Chat / general assistant | Benchmark Cost | Quality index |
| Summarization | Latency | Groundedness |
| RAG answer generation | Benchmark Cost | Groundedness |
| Search / retrieval ranking | Latency | NDCG at 10 |
| Document clustering | Benchmark Cost | V-measure |
| Classification | Benchmark Cost | F1 score |

These are starting points, not fixed rules — swap in Safety as one axis whenever your use case has compliance or brand-risk exposure, regardless of task type.
