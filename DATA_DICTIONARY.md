# Data dictionary

Version: 1.0  
Last modified: 2026-09-17  
Changelog: Initial dictionary for the frozen v1.0.0 public dataset. 2026-09-16: documented the reduced and extended DAS scoring layouts. 2026-09-17: final public-release documentation consolidation.

Identifiers include the internal execution ID, canonical session reference, instance-plan identity, stable profile reference, task-variant identity, and session position. Together, execution ID and canonical session identity provide the condition-scoped scientific join key; logical profile/session design identities are intentionally reused across conditions.

The assigned Ground Truth axes are Knowledge, Misconception, Metacognition, and Transfer. Help-seeking is behavioral and is not a Ground Truth axis. Null means unavailable or not applicable under the source schema; it must not be coerced to zero. In DAS, `INSUFFICIENT_EVIDENCE` (IE) means the blinded transcript does not provide sufficient evidence for a supported reconstruction and is handled according to the frozen scoring specification.

`status_risolto` is a resolved terminal state. `max_learner_turns_reached` is also a legitimate accepted scientific terminal state. An accepted session is a canonical session durably published by the frozen acquisition process; acceptance is not synonymous with resolution.

Raw conversations are linked to canonical evidence by execution-scoped session/profile/task identities and persisted hashes. A1 derives behavioral/profile consistency measures from the accepted population. DAS scientific-run artifacts contain transcript-only blinded extractions; DAS scoring artifacts join those finalized extractions to Ground Truth only in the explicit scoring phase.

The dialogue language is Italian and the domain is school mathematics, specifically fractions.

## Native-format disclosure

Proxima preserves one aggregate `transcripts.jsonl` containing exactly 220 records. Every Generic Tutor condition preserves exactly 220 per-session JSON files. The asymmetry is intentional and preserves frozen source provenance; no publication-time format normalization was performed. It is not missing data or an export error.

Local filesystem paths and the researcher username present in the source artifacts were replaced with normalized placeholders prior to public release. This transformation did not alter any scientific content or result values. A deterministic transformation log is retained by the maintainer.

## Proxima session-identity crosswalk

Proxima preserves conversations in one aggregate `transcripts.jsonl`, whose records use a `session_id` field, whereas the four Generic Tutor conditions preserve per-session files keyed by `canonical_session_ref`. To join a Proxima transcript to the canonical session identity reused across conditions, use the following value-equality join:

1. Each `transcripts.jsonl` record carries `session_id`, whose value is the instance-plan identity (for example `INST_CHVAR_CH01_CORE_CELL_01_style_a_01`).
2. Each `raw/evidence/sessions/*.json` file carries both `instance_plan_id` and `canonical_session_ref` (for example `instance_plan_id = "INST_CHVAR_CH01_CORE_CELL_01_style_a_01"` and `canonical_session_ref = "CHVAR_CH01_CORE_CELL_01_style_a::S1"`).
3. The join is therefore by value equality: `transcripts.jsonl.session_id` equals `raw/evidence/sessions/*.json.instance_plan_id`, which yields the `canonical_session_ref` used by the comparator conditions.

In the released Proxima condition, `session_id` is unique across the 220 transcripts (220 distinct values), and each value maps to exactly one evidence file with a distinct `canonical_session_ref` (220 distinct values); the two identifier sets correspond one-to-one. No string-transformation rule is required: the join is performed on the persisted values.

## Mistral DAS provenance disclosure

Before public release, provider/model provenance metadata in Mistral's DAS scientific-run manifest were corrected to the proper identifiers, replacing default fallback values previously populated in those fields. The dependent run-identity hash was recomputed accordingly. This correction affected provenance metadata only and did not alter any transcript, extraction, scoring, aggregate, or other scientific result. Correction details and the original audit evidence are retained by the maintainer.

## Source-path and public-path provenance

Some provenance records preserve source-repository paths to internal project governance or methodological material that is not distributed as part of this public dataset. Such references document source provenance and should not be interpreted as public-package paths. Publicly distributed specifications are referenced by their release locations where applicable.

## Frozen-specification lifecycle

Status and lifecycle statements inside frozen methodological specifications (e.g., schemas/DAS_EXTRACTOR_SPEC_v1_0_7.md) reflect the pre-execution state captured when the specification was frozen, before the corresponding analyses were run across the released conditions. These statements are intentionally not updated post-hoc to reflect later execution results, consistent with the project's methodological freeze discipline: a specification frozen before results exist is preserved as evidence of what was defined in advance, rather than revised once outcomes are known. Readers should therefore treat any "planned" or "pending" condition status inside a frozen specification as historical and refer to the corresponding condition_manifest.json and derived/DAS/ artifacts for the realized execution status of each released condition.

The three bundled methodological specifications (A1_METRICS_SPEC, DAS_SCORING_SPEC, DAS_EXTRACTOR_SPEC) contain historical references to ANALYSIS_SPEC_v1_0_2.md as project governance authority for cases not directly covered. ANALYSIS_SPEC_v1_0_2.md is internal project governance material and is not part of this public release. For the purpose of interpreting and verifying the released dataset, the three bundled specifications constitute the authoritative public methodological contract within their respective documented scopes. The historical references to ANALYSIS_SPEC_v1_0_2.md are retained unchanged as frozen text. For this public release, they do not create an external dependency for interpretation of the published results. No published result was identified as requiring resolution via ANALYSIS_SPEC_v1_0_2.md.

This public release does not include a per-manifest development- environment status field referenced in two frozen specifications (recorded there as "dirty-worktree state"). This field described only whether any file in the source repository — not necessarily related to A1 — had local changes that had not yet been saved to the project's version-control history at analysis time (a state Git calls "uncommitted"); it did not describe the scientific content, formulas, or results reported in this release. Whether this had any bearing on the A1 code path was investigated directly: a byte-level comparison confirmed that the A1 estimation formulas used to produce the published results are unchanged, across every condition, from the current reference implementation. On that basis, the field was judged not relevant to the scientific validity of the published results and was omitted from the public release. The investigation and its full evidence are retained by the maintainer and available on request. The frozen specifications that reference this field are preserved unchanged, consistent with this project's methodological freeze discipline.

## DAS scoring artifacts: reduced and extended layouts

DAS scoring results are persisted in two serialization layouts across the five conditions. The two layouts carry the same primary scientific estimands and results and differ in file granularity and naming, not in the underlying per-dimension estimates.

- **Reduced layout** (three files): `session_comparisons.jsonl`, `dimension_summary.json`, `provenance_manifest.json`. Used by Mistral, Claude Vanilla, and Claude Mainstream.
- **Extended layout** (seven files): `joined_session_scored.jsonl`, `class_a_primary_summary.json`, `class_b_secondary_analysis.json`, `bootstrap_results.json`, `confusion_matrices.json`, `population_definition_summary.json`, `scoring_provenance_manifest.json`. Used by OpenAI and Proxima (Proxima also has `pre_unblinding_analysis_registry.json`).

`dimension_summary.json` (reduced) and `class_a_primary_summary.json` (extended) report the same primary per-dimension quantities — correct / incorrect / insufficient-evidence counts, exact Ground-Truth recovery, and evidence sufficiency — over the same 220-session population. In the reduced layout the profile-cluster Bayesian-bootstrap intervals and the secondary misconception-subtype counts/rates are embedded directly in `dimension_summary.json`; in the extended layout those intervals are stored separately in `bootstrap_results.json` and the subtype and per-family tables are stored in `class_b_secondary_analysis.json`.

Evidence-sufficiency interval upper bounds may marginally exceed the mathematical maximum of 1.0 due to floating-point representation (e.g., 1.0000000000000018). Such values should be interpreted as 1.0. This is a numerical representation artifact, not a scoring or computation error. The frozen values are retained unmodified.

`session_comparisons.jsonl` (reduced) and `joined_session_scored.jsonl` (extended) are alternative per-session records of the same scoring join: for each of the four dimensions they record the extracted value, the assigned Ground-Truth value, and the outcome (`correct` / `incorrect` / `insufficient_evidence`). The extended file additionally carries the extractor's per-dimension evidence-turn references and per-session family/style/condition attributes; the reduced file carries a per-session misconception-subtype comparison. Each file contains exactly 220 rows.

The two layouts are not byte-identical and are not file-for-file interchangeable; the correspondence is at the level of the primary results and the per-session scoring join, not identical serialization.

The extended layout's `confusion_matrices.json` and the per-profile-family breakdowns (Core / ChannelLayer / NumericalProcessing) are absent from the reduced layout because they are not part of the frozen scoring output contract (`DAS_SCORING_SPEC_v1_0_0`, section "Persistent outputs"), which specifies the reduced set — `session_comparisons.jsonl`, `dimension_summary.json` (with subtype and uncertainty within it), `provenance_manifest.json`, and checksums. The extended files are the historical Proxima/OpenAI scoring serialization that preceded that frozen contract; the frozen contract consolidated the primary results, uncertainty, and subtype description into `dimension_summary.json` and did not carry forward separate confusion-matrix and per-family-breakdown files for the conditions scored under it (Mistral and the two Claude conditions). The same per-session inputs required to recompute such secondary tables are present in the reduced layout's `session_comparisons.jsonl`.

In `confusion_matrices.json` (extended layout), each matrix uses the assigned Ground-Truth value as the row and the extractor's classification as the column; the field names `rows_gt` and `columns_extractor` state this explicitly, and each count is addressed as `counts[ground_truth_value][extractor_value]`.
