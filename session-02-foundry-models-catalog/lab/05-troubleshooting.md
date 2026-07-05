# Troubleshooting

**A model I expected to see isn't in the catalog.**
Check the filter panel — an active provider or modality filter from an earlier search can silently hide results. Clear all filters and search by name directly.

**The model card doesn't show pricing.**
Pricing is deployment-type and region dependent, so it's often not shown directly on the catalog card. Check the model's dedicated pricing page (linked from the card) or the Azure pricing calculator.

**A model shows as available but I can't select a deployment type for it.**
This usually means a quota or region mismatch between the model and your project's region. This gets resolved in Session 3 at actual deployment time — for this session, just note it in your comparison table.

**Benchmark numbers on two models' cards aren't using the same benchmark.**
This happens — not all providers report the same benchmark suite. When this happens, look for a shared benchmark (e.g., MMLU appears on most cards) to make an apples-to-apples comparison, and treat provider-specific benchmarks as supplementary.

**The rank shown on a Model benchmarks scatter point looks wrong.**
The rank (e.g., "Ranking No. 10/35") is relative to your current **Selected model** list, not the entire catalog. Add or remove models from the list and the ranking recalculates. Don't quote a rank number without also stating how many models were in the comparison set.
