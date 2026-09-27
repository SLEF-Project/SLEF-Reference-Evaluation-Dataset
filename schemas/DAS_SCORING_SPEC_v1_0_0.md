# SLEF Pilot 0 — DAS Scoring Child Specification

Version: 1.0.0
Last modified: 2026-09-08
Status: FROZEN — OWNER APPROVED
Changelog: Owner-froze the historically executed comparative DAS scoring
scope; Mistral uses identical Proxima/OpenAI semantics, broader Brier/ECE/T17
metrics remain deferred, and no Proxima/OpenAI reprocessing is authorized.

## 1. Status, authority and scope

This document is the frozen child specification for scoring outputs of
the external DAS extractor in Pilot 0. It does not authorize a DAS execution,
define a new Ground Truth, or replace the frozen extractor prompt, rubric, or
response schema.

The authority order is:

1. `docs/pilot0/analysis/ANALYSIS_SPEC_v1_0_2.md`;
2. the frozen DAS extractor specification and prompt;
3. accepted SLEF ADRs and governance decisions;
4. the accepted historical DAS implementation and regression evidence;
5. implementation modules, including `src/pslp/pilot0/das_scoring.py`.

The implementation is evidence of conformance, not scientific authority.

## 2. Relationship to the general analysis specification

`ANALYSIS_SPEC_v1_0_2` defines DAS as a primary diagnostic-recoverability
outcome reported by canonical dimension. It requires the DAS scoring child
specification to be frozen before extractor outputs are scored or inspected as
scientific outcomes (§14.2, §15, §D2, §32.4).

The broader framework also describes probability metrics and T17 volume
analyses. This child contract deliberately freezes only the common historical
comparative scope already applied to Proxima and OpenAI. Deferring broader
metrics here does not remove them from the framework; it prevents Mistral from
receiving analyses that were not applied to the prior comparison conditions.

The primary DAS remains unconditioned on Track A2 observability. No arbitrary
single composite DAS is introduced.

For the current comparison:

```text
Proxima = historical comparative scoring scope
OpenAI  = historical comparative scoring scope
Mistral = identical historical comparative scoring scope
```

No condition may receive an additional DAS metric or companion analysis unless
all comparison conditions are reprocessed under a future owner-approved
revised contract.

## 3. Scientific phase boundary

The pipeline has two strictly separated scientific phases:

1. **Blinded extraction**: the rater receives only the permitted dialogue and
   extraction instructions. Ground Truth, profile assignments, and
   `manifested_this_turn` are not available to the extractor.
2. **Explicit scoring**: after the accepted extraction corpus is durably
   finalized and structurally validated, the scorer joins extraction results
   to the pre-assigned Ground Truth/design rows and computes the metrics here.

No scoring, Ground Truth join, outcome-based filtering, or session exclusion may
occur inside the per-session extraction loop. A post-extraction result cannot
decide whether a session counts in the primary population.

## 4. Input contract

The scorer consumes exactly one completed, accepted extraction corpus and one
matching Ground Truth/design corpus.

Required identity and completeness conditions:

- one explicit `execution_id`/`source_execution_id` binds every accepted row;
- every canonical session reference is unique;
- accepted extraction and Ground Truth reference sets are exactly equal;
- no missing, duplicate, unexpected, mixed-execution, or cross-condition row
  is admitted;
- accepted rows contain the finalized extractor result and source identity but
  no pre-joined Ground Truth;
- source execution metadata, provider, model, scoring specification identity,
  and source hashes are retained in provenance;
- source and design inputs are read-only;
- scoring output is outside the source tree and scoped to the execution.

The fixed Pilot 0 assignment and population remain unchanged: 44 profiles,
five sessions per profile, 220 sessions, exact canonical task assignment, and
the frozen Core/ChannelLayer/NumericalProcessing structure.

## 5. Canonical DAS dimensions

The canonical dimensions are:

- Knowledge;
- Misconception;
- Metacognition;
- Transfer.

Help-seeking and learner-token volume are not additional Ground Truth axes.
Proxima-native DAS is not substituted for the external DAS instrument.

## 6. Primary scoring semantics

For each canonical dimension and scientifically eligible session:

- `correct`: extracted state maps exactly to the assigned Ground Truth state;
- `incorrect`: extracted state is valid but does not map to the assigned state;
- `insufficient_evidence`: extractor explicitly returns
  `INSUFFICIENT_EVIDENCE`.

The primary per-dimension estimand is top-1 exact recovery. Evidence
sufficiency is the proportion of successfully extracted sessions whose result
is either `correct` or `incorrect`.

For a dimension, the primary denominator is the number of successfully
extracted, scientifically eligible sessions. Technical failures remain
identified and are not silently converted into incorrect or insufficient
evidence. If the denominator is zero, the metric is non-estimable with an
explicit reason.

No post-extraction metric may be used to remove a session from the pre-declared
primary population.

## 7. Misconception subtype scoring

Subtype scoring is secondary and conditional. It applies only when:

1. Ground Truth misconception is present; and
2. the extractor identifies misconception as present.

Within that population:

- matching subtype is `correct`;
- a different subtype is `incorrect`;
- no extracted subtype is `unresolved`.

Sessions outside the conditional population are not evaluable and receive an
explicit non-evaluability reason. Subtype results must not be promoted to a
primary DAS outcome.

## 8. Probability and calibration metrics

Brier Score, ECE, cross-entropy, ordinal distance, probability calibration and
other probability-derived metrics are part of the broader framework described
by `ANALYSIS_SPEC_v1_0_2`, but are **OUT OF CURRENT COMPARATIVE SCOPE**.

They were not added to the Mistral comparison because they were not applied to
the already executed Proxima/OpenAI comparison. They are not deleted from the
broader framework and may be addressed only by a future owner-approved
contract/amendment that applies consistently to every comparison condition.

The current scorer must not represent categorical outputs as probability
metrics, infer probabilities, or calculate these deferred metrics implicitly.

## 9. Secondary and companion metrics

The following are secondary or companion analyses only when included by a
future contract; they are not part of this comparative child contract:

- evidence sufficiency;
- misconception subtype exact recovery and identifiability;
- probability calibration and Brier-related summaries;
- ordinal distance and other dimension-specific secondary metrics;
- T17 learner-token volume analysis;
- volume-conditioned DAS.

None may be interpreted as the primary total tutor effect or as an arbitrary
composite DAS.

## 10. Uncertainty and determinism

The accepted historical DAS behavior uses a profile-cluster Bayesian bootstrap:

- cluster unit: `stable_profile_ref`;
- RNG: `numpy.random.Generator(numpy.random.PCG64)`;
- seed: `20260827`;
- requested replicates: `10_000`;
- percentiles: 2.5 and 97.5;
- percentile method: linear;
- non-estimable replicates and failure counts are retained explicitly.

The bootstrap computes uncertainty for exact recovery and evidence sufficiency
using profile-cluster weights. The same seed, RNG, cluster unit, replicate
count, and percentile semantics are required for reproducibility. Any extension
of uncertainty to probability metrics or the T17 companion requires the
corresponding owner decision and must not silently alter this historical
behavior.

## 11. T17 learner-token volume — deferred

The broader framework defines T17 using learner-token volume per session, not
turn count. The tokenizer/counting rule is **OUT OF CURRENT COMPARATIVE SCOPE**.
Learner-turn count and total dialogue turns must not be substituted for it.

The primary DAS remains unconditioned. No T17 analysis is produced for the
current Proxima/OpenAI/Mistral comparison, and no session is filtered using
volume.

## 12. Volume-conditioned companion analysis — deferred

The broader framework contemplates reporting:

- the association between learner-token volume and DAS; and
- a volume-conditioned cross-condition estimate.

The unconditioned cross-condition difference remains the primary end-to-end
estimand. If this companion analysis is activated in a future contract, the
conditioned coefficient must remain mechanism-oriented sensitivity evidence and
must not be interpreted as the total tutor effect.

The exact model family and tokenizer are deferred together with this analysis;
they are not decisions blocking the current comparative freeze.

## 13. Determinism

For identical source inputs, Ground Truth/design inputs, specification identity,
seed, and configuration, the scorer must produce byte-stable canonical JSON/
JSONL content. Session ordering is canonical bytewise ordering of
`canonical_session_ref`. Nondeterministic timestamps may occur only in
provenance fields explicitly designated as operational metadata and must not
alter scientific content or checksum reproducibility expectations.

## 14. Provider neutrality

Scoring formulas do not branch on provider, model, tutor, or execution name.
Provider and model may be recorded in provenance only. A new Generic Tutor
execution with the canonical source schema must use the same scoring path.

## 15. Source identity and provenance

Every scoring result records, where available:

- source execution ID;
- source condition/target identity;
- provider and model;
- source execution and accepted-extraction hashes;
- scoring specification identity and hash;
- accepted session count and canonical inventory;
- bootstrap version, seed, replicates, and RNG;
- output inventory and checksums;
- scoring phase boundary and Ground Truth join status.

Provenance must not claim a provider-specific metric or configured control that
was not present in the source execution.

## 16. Persistent outputs

The execution-scoped output namespace contains at least:

- `session_comparisons.jsonl`;
- `dimension_summary.json`;
- misconception subtype results within the summary or a separately identified
  artifact;
- uncertainty metadata and intervals;
- `provenance_manifest.json`;
- `SHA256SUMS.txt`.

Publication is atomic, source inputs remain untouched, and an existing output
directory is a hard failure. No scientific output may be silently overwritten.

## 17. Failure behavior

The scorer fails closed on:

- missing or malformed accepted extraction;
- missing or malformed Ground Truth/design row;
- execution identity mismatch;
- duplicate, missing, unexpected, or mixed session references;
- pre-joined Ground Truth in a supposedly blinded extraction;
- invalid categorical state or subtype structure;
- missing provider/model source metadata when required by provenance;
- scoring specification/provenance mismatch;
- incomplete bootstrap inputs;
- output collision or checksum conflict.

## 18. Historical regression requirements

The following OpenAI results are regression evidence only and must never be
hardcoded into production code:

| Dimension | Correct | Incorrect | Insufficient evidence |
|---|---:|---:|---:|
| Knowledge | 127 | 93 | 0 |
| Misconception | 106 | 87 | 27 |
| Metacognition | 77 | 42 | 101 |
| Transfer | 0 | 2 | 218 |

Historical subtype evidence is:

- Ground Truth misconception present: 110;
- evaluable: 7;
- exact: 4;
- mismatch: 3;
- unresolved: 103.

Regression tests must compare generated results to these golden values and to
available persistent Proxima results without embedding them in production
logic. Proxima regression remains pending until its persistent evidence is
available in the current implementation context.

## 19. Current implementation compliance matrix

| Contract requirement | `das_scoring.py` status | Evidence | Action |
|---|---|---|---|
| Four canonical dimensions | PASS | `DIMENSIONS` and `score_corpus()` | None |
| Exact categorical comparison | PASS | `compare_value()` | None |
| Insufficient-evidence semantics | PASS | `compare_value()` | None |
| Evidence sufficiency | PASS | `dimension_summary()` | None |
| Misconception subtype | PASS | `compare_misconception_subtype()` | None |
| Exact execution/session join | PASS | `_validate_corpus()` | None |
| Blinded extraction boundary | PASS | rejects pre-joined Ground Truth | None |
| Provider neutrality | PASS | no provider branches | None |
| Profile-cluster bootstrap | PASS | `bootstrap_uncertainty()` | None |
| PCG64, seed, replicates, percentiles | PASS | bootstrap implementation | None |
| Deterministic ordering | PASS | bytewise canonical session ordering | None |
| Execution-scoped persistence | PASS | `write_artifacts()` | None |
| Output checksum/immutability | PASS | manifest and collision guard | None |
| Source hashes in CLI provenance | PASS | accepted/GT hashes and optional source-manifest hash | None for current scope |
| Brier Score | N/A | Broader framework metric, explicitly deferred | Future contract/amendment |
| Probability input schema | N/A | Not required by current comparative scope | Future contract/amendment |
| ECE | N/A | Broader framework metric, explicitly deferred | Future contract/amendment |
| Secondary probability metrics | N/A | Explicitly deferred | Future contract/amendment |
| T17 tokenizer/counting | N/A | Explicitly deferred; learner-token volume remains the broader framework rule | Future contract/amendment |
| Volume-conditioned DAS | N/A | Explicitly deferred companion analysis | Future contract/amendment |
| Current comparative uncertainty contract | PASS | Historical categorical bootstrap fully specified above | None |

## 20. Deferred broader-framework decisions

The following items are retained for future work and do not block this
comparative child contract. They must be resolved before the corresponding
broader metrics are used scientifically.

### DEFERRED DECISION OD-DAS-01

Question: How should exact top-probability ties be handled if probability
outputs are later scored?

Already fixed: categorical exact recovery remains primary; no arbitrary
composite is introduced.

Historical behavior: no complete probability tie rule is recorded in the
available accepted implementation.

Lowest-risk option: classify tied top probabilities as non-unique and record an
explicit non-estimability/tie reason rather than choosing by field order.

Alternatives: deterministic lexical/class-order tie-break.

Scientific consequence: affects probability-derived classification only, not
the categorical rule already frozen.

Implementation consequence: add one shared tie policy to probability scoring and
tests.

### DEFERRED DECISION OD-DAS-02

Question: What exact probability-vector schema, class ordering, normalization
and missing-probability handling shall govern deferred Brier, ECE and secondary
probability metrics?

Already fixed: Brier is mandatory when valid probability inputs exist; ECE is
conditional on at least 100 scored predictions; primary DAS remains exact
dimension-specific recovery.

Historical behavior: the current accepted categorical DAS outputs do not freeze
a complete probability-vector contract.

Lowest-risk option: use only normalized vectors with the frozen class ordering,
fail closed on malformed vectors, and omit ECE below the stated eligibility
threshold with an explicit reason.

Alternatives: define a deterministic normalization step for non-normalized
vectors; treat missing vectors as metric-specific non-estimability.

Scientific consequence: fixes which probability outcomes are estimable.

Implementation consequence: add probability validation and metrics without
changing categorical summaries.

### DEFERRED DECISION OD-DAS-03

Question: Which single tokenizer/counting rule should define learner-token
volume for future T17 analysis across all tutor conditions?

Already fixed: learner-token volume, not turn count, is the primary T17 measure;
the same rule must apply across conditions.

Historical behavior: no complete tokenizer identity and counting specification
is available in the current repository context.

Lowest-risk option: freeze a repository-persisted deterministic tokenizer and
its normalization/Unicode rules before any cross-condition T17 result.

Alternatives: a provider-independent established tokenizer, if its exact
version and behavior are frozen.

Scientific consequence: changes the volume covariate and companion analysis,
not the primary unconditioned DAS definition.

Implementation consequence: add a versioned counting utility and provenance.

### DEFERRED DECISION OD-DAS-04

Question: What exact statistical model and presentation should define the
future T17 volume-conditioned companion analysis?

Already fixed: it is companion/sensitivity analysis; it cannot be interpreted
as the total tutor effect or replace unconditioned DAS.

Historical behavior: the exact model was explicitly left to the DAS scoring
child specification.

Lowest-risk option: freeze the simplest prespecified cross-condition model that
uses session learner-token volume, retains the primary contrast separately, and
has explicit missing-data and uncertainty rules.

Alternatives: a profile-cluster regression or other model justified before
outcomes are inspected.

Scientific consequence: determines the conditional estimand and interpretation.

Implementation consequence: add a separate companion-analysis function and
artifact; do not alter primary dimension summaries.

### DEFERRED DECISION OD-DAS-05

Question: Which uncertainty procedure should apply to future probability
metrics and the T17 companion in addition to the frozen categorical bootstrap?

Already fixed: categorical exact-recovery/evidence-sufficiency bootstrap uses
profile clusters, PCG64, seed `20260827`, 10,000 replicates and linear 2.5/97.5
percentiles.

Historical behavior: no complete extension procedure is recorded.

Lowest-risk option: retain profile-cluster resampling and freeze metric-specific
estimability/failure handling before scoring.

Alternatives: a separate prespecified procedure for probability calibration or
conditional regression.

Scientific consequence: determines reported uncertainty for non-categorical
outcomes.

Implementation consequence: extend the existing deterministic bootstrap without
altering its categorical behavior.

## 21. Current comparative freeze criteria

The owner may freeze this child specification only after:

- no unresolved decision remains inside the current comparative scope;
- no conflict remains with `ANALYSIS_SPEC_v1_0_2` or the frozen extractor
  contract;
- primary dimension scoring is explicitly defined;
- historical subtype and uncertainty behavior are explicitly defined;
- implementation compliance gaps are identified and addressed;
- OpenAI and available Proxima regression requirements are fixed;
- provider neutrality, source isolation, provenance, checksums and immutable
  output behavior remain preserved;
- Brier, ECE, probability metrics, T17 and volume-conditioned analyses are
  explicitly marked deferred and are not silently computed.

The broader deferred metrics require a separate future contract or amendment
before they are used as scientific outcomes.
