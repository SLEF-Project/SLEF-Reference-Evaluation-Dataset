# SLEF Pilot-0 — A1_METRICS_SPEC_v1_0_0

**Document status:** FROZEN — OWNER APPROVED
**Date:** 2026-08-28
**Track:** A1 — SLEF Execution Characterization
**Source run:** `SLEF_PILOT0_REFERENCE_RUN_3`
**Producing baseline:** `6d6089f2242b5d95852d78ab3006f89f1078d316`

---

## 0. Document identity, status, and changelog

This frozen, owner-approved child specification defines the normative Track A1
representation, estimands, nuisance adjustment, uncertainty procedure,
eligibility rules, derived-artifact contract, and verification gates. It is a
specification only and contains no substantive Run 3 manifestation result.

Implementation may be developed against this frozen specification. Scientific
Track A1 execution requires a verified implementation, completion of the
required automatic and V-model/manual verification gates, and binding the
execution to the exact frozen specification SHA-256 as described in §22.

### Changelog

| Version | Date | Status | Change |
|---|---|---|---|
| 1.0.0 | 2026-08-27 | DRAFT — PENDING OWNER APPROVAL | Initial child-spec draft implementing the approved Phase 1 design and binding Phase 2 refinements. |
| 1.0.0 (draft revision) | 2026-08-27 | DRAFT — PENDING OWNER APPROVAL | Owner-review corrections: explicit cumulative-disengagement geometry, deterministic bootstrap weighted-fit guards, and Spearman-only control associations. No scientific estimand or weight changed. |
| 1.0.0 | 2026-08-28 | FROZEN — OWNER APPROVED | Owner scientific review and differential freeze review completed; the three pre-freeze corrections were accepted. No scientific estimand, coordinate or coordinate order, weight, denominator, population, nuisance-adjustment design, bootstrap scientific design, or eligibility rule changed. Frozen as the normative basis for A1 implementation; scientific execution remains subject to implementation verification, required V-model/manual gates, and binding to the exact frozen specification SHA-256. |

## 1. Governing specification and precedence

The governing specification is:

- identity: `docs/pilot0/analysis/ANALYSIS_SPEC_v1_0_2.md`;
- version: `1.0.2`;
- status: `FROZEN — OWNER APPROVED`;
- SHA-256: `77a29d4ef101dcfe7b9c1b0b61f5bb344fe587da641773d8a8d68229e6461c2c`.

`ANALYSIS_SPEC_v1_0_2.md` has precedence. This child specification resolves
its D3 gate for A1 only. It does not alter the governing population,
research-track hierarchy, claim boundaries, A1/A2 separation, qualitative
selection rule, or cross-condition rules. A discovered conflict requires an
amendment; an implementation must not silently choose one text over the other.

## 2. Scope and claim boundaries

Track A1 characterizes what the synthetic learner generator declared and
instantiated during execution. Its primary evidence is the frozen
generator-native `manifested_this_turn` trace. It is descriptive internal
characterization of a controlled synthetic instrument.

A1 may describe:

- generator-declared turn manifestations and their session summaries;
- within-profile consistency and between-profile separation;
- task- and session-position-adjusted execution signatures;
- same-task contrasts supported by the frozen assignment graph;
- Core results and separately labeled extension/robustness results;
- prospectively specified relationships between selected learner controls and
  matching execution declarations.

A1 does not establish psychological validity, human realism, clinical
meaning, pedagogical quality, tutor superiority, external textual
observability, or recovery of assigned K/Misconception/Metacognition/Transfer
state. Run 3 alone contains one tutor condition and supports no cross-tutor
claim.

### 2.1 A1 versus A2

A1 records **what the generator declared it was intentionally
impersonating**. A2 evaluates **what an external rater can observe in the
realized learner text**. These values must not be substituted for one another.

Therefore an A1 implementation must not:

- recode a generator declaration from an external textual judgment;
- create a textual-visibility admission gate;
- reinterpret generator declarations as human-observed behavior;
- use a future A2 judgment to change A1 eligibility or values.

If a frozen source contract requires visible realization and a future
deterministic check finds a mismatch, the generator-native A1 value is
retained. The mismatch is recorded as a coherence/provenance finding unless it
is independently a structural contract failure under §15.

## 3. Producing-source lineage and frozen inputs

The Run 3 producing baseline is fixed at
`6d6089f2242b5d95852d78ab3006f89f1078d316`. The frozen `DEPLOYED_HEAD`
contains that exact identity. The analysis must consume immutable source
evidence and write only to the derived path in §18.

### 3.1 Frozen source identities and hashes

| Source | Analytical role | SHA-256 |
|---|---|---|
| `docs/pilot0/analysis/ANALYSIS_SPEC_v1_0_2.md` | governing specification | `77a29d4ef101dcfe7b9c1b0b61f5bb344fe587da641773d8a8d68229e6461c2c` |
| Run 3 freeze archive `SLEF_PILOT0_REFERENCE_RUN_3-freeze-20260823.tar.gz` | immutable SLEF evidence snapshot | `19c77ad19d7c458a500eab8865f3f41a80163926da2382615f845d356aed475f` |
| `manifest.snapshot.json` | frozen profile and assignment design | `4b4641a0a10c4e747537f3b12399c7eb6cbb914aa88ac063e9ed0fd92253f723` |
| `learner_cards.snapshot.json` | frozen 220-row scientific input/assignment snapshot | `5998c9f1f03e7ea35983c35450043432d4925e6aedcf7b0f7002aac77e39f6b9` |
| `run_descriptor.json` | source-run descriptor | `129b6dc939e6d9e1895fd880e4934941165138532939b91e1f62d483ab6954da` |
| Run 3 execution config | execution configuration | `8f6742f5cd09729a31e65f90b38e05a226d04e2bdbb456b5aae6e20ea69b53c8` |
| identity supplement archive | canonical identity freeze | `d15fc55dd5a1064dfca2ab7037c5f4181e36762da881cd542801f40ff241706b` |
| identity `MANIFEST.json` | identity provenance | `f0867e120a80cccb4c088535d11d27e9a21eb99afb621eeefd7abfaed2795e62` |
| identity `JOIN_QA.json` | 220-row join verification | `f0c205071e19b354a37cdc38300c917b754d9a53b33150b39680992d980bbf5b` |
| `ART-11-mapping-return-RUN-08A.5.json` | canonical session/profile/task/position mapping | `f08ccc96256815f1875c62c599449b8bbe3e9307ec05229d6ddb34f5078706b7` |
| `resolver-RUN-08A.5.json` | accepted runtime resolver | `34a41c311d250f2371cda07d214a722c360e1350293bfa9353972b5f77a6d38e` |
| resolver validation report | accepted resolver QA | `50ffc144d785d6b42692512b403e366afc8559bb400c27d1bdc0b72188191293` |
| staging account crosswalk | frozen cross-system join input; never an A1 scientific variable | `3009aa4d8d545cae105f1b59bde3c53ddce2b074690a17a029abc3199b7f7e43` |
| Proxima supplement archive | frozen cross-system evidence supplement; excluded from A1 metric inputs | `2d09412c05c6c33d8490e48a94c877c88a20cc23b103f0044f99749fac9b3fc3` |

At implementation time, every actually consumed frozen file must be listed
with its relative path and verified SHA-256, even if it is nested within one of
the archives above. The source files and archives must not be modified.

### 3.2 Actual producer schema

The operational trace schema is the schema implemented at the producing
baseline, not a design-level misconception catalog and not a later taxonomy.
The controlling source identities at that baseline are:

- `src/pslp/pilot0/manifestation_trace.py`, content SHA-256
  `1df42c12584564b3bbabbd674ed63e2cab7c63717c9139069059fe47bcddd115`;
- `src/pslp/pilot0/openai_student_model.py`, content SHA-256
  `f89f60918ce8fb850f28c054f69d9cae3ec865f733afa77fcbd05c5d5cb222d0`;
- `docs/pilot0/contracts/PILOT0-05C1-manifestation-trace-contract-v1_1_1.md`,
  SHA-256 `1b2f46610d73606e3d65fc1506b93db1d6c44802d4231cb682b55c8c2c5d65b8`;
- `docs/pilot0/learner-generator/PILOT0-DOCB-learner-generator-prompts.v1.0.0.md`,
  SHA-256 `728de4183baef6a0ffadf44b5764d0e979b3a7d511130282b94e643cf5263d91`.

The operational constants are `schema_version="1.0"` and
`trace_type="learner_generator_self_report"`.

## 4. Populations and canonical identities

The Full Audit Population contains all 220 frozen Run 3 sessions. No source
session disappears from the audit artifact.

The A1 hierarchy is:

- **Core:** primary population, 32 profiles × 5 assigned sessions = 160
  expected sessions;
- **ChannelLayer:** 8 profiles × 5 sessions, secondary matched
  extension/robustness analysis only;
- **NumericalProcessing:** 4 profiles × 5 sessions, secondary
  extension/robustness analysis only;
- **Full 44-profile:** descriptive only; it cannot redefine the Core primary
  estimand.

No clinical interpretation is permitted for either extension family.

Canonical identity is an exact tuple of:

1. `stable_profile_ref`;
2. `session_position`;
3. `task_variant_ref`;
4. `canonical_session_ref`;
5. `instance_plan_id`.

The canonical join is `canonical_session_ref -> ART-11`. The identity
supplement records 220/220 canonical session, profile, and task matches, with
no duplicate canonical or operational join key. No fuzzy matching, case
normalization, inferred suffix repair, or task substitution is permitted.
`proxima_username` is retained only as the frozen cross-system join key and is
not a scientific A1 feature.

Profile-family labels are mapped exactly as follows:

| Frozen `profile_category` | A1 label |
|---|---|
| `core` | `Core` |
| `channel_variant` | `ChannelLayer` |
| `numerical_processing` | `NumericalProcessing` |

## 5. Operational trace representation

### 5.1 Fixed coordinate order

The following exact 16-coordinate order is normative for A1 v1.0.0. It must
be stored in every relevant schema/provenance record and must not be sorted by
name or observed prevalence.

| Index | Family | Coordinate |
|---:|---|---|
| 1 | misconception | `adds_numerators_and_denominators` |
| 2 | misconception | `adds_denominators_keeps_numerator` |
| 3 | misconception | `no_common_denominator_search` |
| 4 | misconception | `partial_simplification_error` |
| 5 | misconception | `confuses_proper_improper_fractions` |
| 6 | misconception | `simplification_oversight` |
| 7 | misconception | `procedural_sequence_error` |
| 8 | misconception | `complexity_misstep` |
| 9 | misconception | `sign_oversight` |
| 10 | behavioral | `help_seeking` |
| 11 | behavioral | `frustration` |
| 12 | behavioral | `impulsivity` |
| 13 | behavioral | `verification_attempt` |
| 14 | cumulative disengagement | `dropout_risk >= low` |
| 15 | cumulative disengagement | `dropout_risk >= high` |
| 16 | cumulative disengagement | `dropout_risk = explicit` |

### 5.2 Misconception-vocabulary boundary

The nine producing codes in indices 1–9 are the complete operational A1
misconception universe for Run 3.

> A1 misconception manifestation coverage is defined by the producing
> nine-code operational vocabulary and is not assumed to be isomorphic to the
> assigned Ground-Truth misconception vocabulary.

`larger_denominator_larger`, and every other non-matching design-level code,
must not be translated, merged, or mapped onto a trace code post hoc. Exact
design-code/trace-code matches may support the explicitly secondary analysis
in §14.3. Non-matching codes are ineligible for that relationship and remain
visible with reason `nonmatching_design_trace_code`. This vocabulary mismatch
is a known operational limitation, not a Run 3 execution failure.

### 5.3 Turn-level encoding

For learner turn `t`, define

\[
T_t=(M_t,B_t,D_t;S_t),
\]

where:

- \(M_t\in\{0,1\}^9\) is the multi-hot misconception declaration;
- \(B_t\in\{0,1\}^4\) is the behavioral declaration;
- \(D_t\in\{\text{none}<\text{low}<\text{high}<\text{explicit}\}\) is
  the current generator-declared disengagement state;
- \(S_t\in\{\text{continua},\text{risolto},\text{arreso}\}\) is separate
  execution metadata.

For misconception code `c`, `M_tc=1` if one or more entries in
`misconceptions[]` have exactly code `c`; duplicate instances of the same code
count once. Different codes can be active together. For behavior `b`, `B_tb`
is its exact Boolean value; several flags can be true together.

`false` means absence of that generator declaration, not independently
verified textual absence. `misconceptions=[]` is a valid all-zero
misconception turn. `evidence_spans` are provenance/bookkeeping and do not add
events. `schema_version` and `trace_type` are structural/provenance fields.
Status remains outside the primary signature.

Disengagement is not encoded as interval-scale 0, 1, 2, 3. Its primary
coordinates are the cumulative indicators

\[
E_{t,low}=1[D_t\ge low],\quad
E_{t,high}=1[D_t\ge high],\quad
E_{t,explicit}=1[D_t=explicit].
\]

Thus valid turn patterns are `000`, `100`, `110`, and `111` in that order.

This cumulative encoding preserves ordinal direction without encoding the
four category labels themselves as an interval-scale variable. Equal weighting
of the three cumulative thresholds nevertheless imposes an explicit,
prospective geometry: each adjacent threshold crossing (`none -> low`,
`low -> high`, and `high -> explicit`) contributes equally to squared
disengagement-family distance. This equal-threshold-crossing convention is a
normative metric-design choice, not an empirically learned scale.

## 6. Session aggregation

### 6.1 Denominator rule and primary signature

For session `s`, let `n_s` be the number of structurally valid learner turns.
Every primary incidence coordinate uses `n_s`; tutor turns, dialogue turns,
evidence spans, and active-code totals are never denominators for the primary
signature.

For misconception `c`, behavior `b`, and cumulative threshold `k`, define

\[
m_{sc}=\frac{\sum_{t=1}^{n_s}M_{tc}}{n_s},\quad
b_{sb}=\frac{\sum_{t=1}^{n_s}B_{tb}}{n_s},\quad
e_{sk}=\frac{\sum_{t=1}^{n_s}E_{tk}}{n_s}.
\]

The primary session signature, in the fixed order of §5.1, is

\[
Y_s=(m_{s1},\ldots,m_{s9},b_{s1},\ldots,b_{s4},
e_{s,low},e_{s,high},e_{s,explicit}).
\]

Every rate is serialized with exact integer numerator, exact integer
denominator, and value. Raw counts must be preserved beside every rate.
Sessions and profiles receive equal weight in primary between-session and
profile estimands; sessions must not be weighted by `n_s`.

### 6.2 Secondary incidence and diversity summaries

These deterministic secondary summaries are required per session:

- **any-misconception incidence:** numerator
  `sum_t 1[sum_c M_tc > 0]`, denominator `n_s`;
- **distinct misconception diversity:** raw number of codes with
  `sum_t M_tc > 0`, plus proportion with denominator 9;
- **misconception multiplicity:** numerator `sum_t sum_c M_tc`, denominator
  `n_s`; this is the mean number of distinct declared codes per learner turn;
- **multi-code co-manifestation:** numerator
  `sum_t 1[sum_c M_tc >= 2]`, denominator `n_s`;
- **any-behavior incidence:** numerator
  `sum_t 1[sum_b B_tb > 0]`, denominator `n_s`;
- **four-state disengagement occupancy:** one count and rate, denominator
  `n_s`, for each of `none`, `low`, `high`, `explicit`.

### 6.3 Persistence, transitions, onset, and run lengths

For each of the nine misconception indicators, four behavior indicators,
three cumulative disengagement indicators, `any_misconception`, and
`any_behavior`, let `X_t` be its binary turn series. Adjacent persistence is

\[
P_s(X)=\frac{\sum_{t=1}^{n_s-1}1[X_t=1\land X_{t+1}=1]}
{\sum_{t=1}^{n_s-1}1[X_t=1]}.
\]

If `n_s<2`, the value is `null` with reason
`insufficient_adjacent_turns`. If the at-risk denominator is zero, it is
`null` with reason `no_at_risk_active_turn`. Zero is never substituted.

Disengagement transitions are a complete 4 × 4 matrix of raw adjacent-pair
counts in the fixed state order `none, low, high, explicit`. Each row also has
origin-conditional rates with the row sum as denominator. A zero row sum gives
`null` with reason `no_transition_from_origin_state`. Global stable,
escalating, and de-escalating transition rates use denominator `n_s-1`; for
`n_s<2` they are `null` with reason `insufficient_adjacent_turns`.

First onset is reported for every binary series above. It contains the
one-based turn index and, when `n_s>=2`, normalized location
`(first_turn-1)/(n_s-1)`. No onset gives `null` with reason
`manifestation_not_observed`. When onset exists but `n_s=1`, the normalized
value is `null` with reason `insufficient_temporal_span`.

Contiguous run lengths are the ordered list of maximal positive-run lengths
for every binary series. Preserve the list, run count, maximum, and arithmetic
mean. If there is no positive run, maximum and mean are `null` with reason
`manifestation_not_observed`; do not encode a fictitious zero-length run.

### 6.4 Terminal and structural session descriptors

The following remain separate from `Y_s`:

- session length `n_s`;
- final learner status;
- `termination_reason`;
- maximum-turn-boundary indicator.

Source-supported status semantics are:

- `continua`: non-terminal learner status; it is not measured engagement;
- `risolto`: the learner declares or believes the task resolved; it is not a
  correctness judgment and does not by itself prove session termination;
- `arreso`: explicit giving up and requires `dropout_risk=explicit`.

Actual session termination is taken from `termination_reason`, whose producing
values are `status_risolto`, `status_arreso`, and
`max_learner_turns_reached`. The maximum-turn-boundary indicator is true if
and only if `termination_reason="max_learner_turns_reached"`. Do not infer it
only from `n_s`. Do not double-count `status=arreso` and
`dropout_risk=explicit` in the primary signature.

### 6.5 Undefined-value representation

Every undefined quantity is encoded as:

```json
{"value": null, "not_estimable_reason": "machine_readable_reason"}
```

`NaN`, `Infinity`, `-Infinity`, empty strings, and numeric sentinel values are
prohibited substitutes for undefined quantities.

## 7. Primary raw session-distance function

For two eligible sessions `s` and `r`, define

\[
D_M^2=\frac{1}{9}\sum_{c=1}^{9}(m_{sc}-m_{rc})^2,
\]

\[
D_B^2=\frac{1}{4}\sum_{b=1}^{4}(b_{sb}-b_{rb})^2,
\]

\[
D_D^2=\frac{1}{3}\sum_{k\in\{low,high,explicit\}}
(e_{sk}-e_{rk})^2,
\]

and

\[
D_{A1\_raw}(s,r)=\sqrt{\frac{D_M^2+D_B^2+D_D^2}{3}}.
\]

The equivalent squared-distance coordinate weights are fixed:

- each misconception coordinate: `1/27`;
- each behavioral coordinate: `1/12`;
- each cumulative disengagement coordinate: `1/9`.

No empirical scale factor, z-score, Run 3 variance normalization, prevalence
weight, or outcome-dependent feature selection is permitted.
`D_A1_raw` is bounded in `[0,1]` because its input coordinates are incidences
in `[0,1]`. This bound does not apply to `D_A1_adj`.

### 7.1 Rationale for family balancing

The three construct families have different numbers of coordinates. Taking
the mean squared difference within each family and then giving the three
families equal weight prevents the nine-code misconception block from
receiving greater total weight merely because it has more coordinates. The
weights are design-fixed and do not depend on observed variability or
prevalence.

Within the disengagement family, equal weighting of its three cumulative
coordinates means that each adjacent ordinal threshold crossing contributes
equally to squared family distance. This is prospective normative geometry.
It does not encode the four source labels directly as interval values
`0,1,2,3`, and it is not estimated from Run 3 outcomes.

### 7.2 Why Jensen–Shannon divergence is not used

Misconception and behavioral declarations may co-occur and are not mutually
exclusive categories from one multinomial distribution. Disengagement is an
ordered state from a different construct family. Normalizing all
manifestations into one probability composition would make unrelated
manifestations compete mechanically for mass. The historical JSD proposal is
therefore not the primary A1 metric and must not be reopened after outcome
inspection.

## 8. Core structural-design verification

The Core-only check used only the accepted `ART-11` canonical mapping fields
`stable_profile_ref`, `canonical_session_ref`, `task_variant_ref`, and
`session_position`. No manifestation, trace, transcript, termination, L/M,
Gemini, DAS, or other scientific outcome was read.

The represented task levels are all 30 canonical levels:

`TASK_FRACTIONS_001`, `TASK_FRACTIONS_002`, `TASK_FRACTIONS_003`,
`TASK_FRACTIONS_004`, `TASK_FRACTIONS_005`, `TASK_FRACTIONS_006`,
`TASK_FRACTIONS_007`, `TASK_FRACTIONS_008`, `TASK_FRACTIONS_009`,
`TASK_FRACTIONS_010`, `TASK_FRACTIONS_011`, `TASK_FRACTIONS_012`,
`TASK_FRACTIONS_013`, `TASK_FRACTIONS_014`, `TASK_FRACTIONS_015`,
`TASK_FRACTIONS_016`, `TASK_FRACTIONS_017`, `TASK_FRACTIONS_018`,
`TASK_FRACTIONS_019`, `TASK_FRACTIONS_020`, `TASK_FRACTIONS_021`,
`TASK_FRACTIONS_022`, `TASK_FRACTIONS_023`, `TASK_FRACTIONS_024`,
`TASK_FRACTIONS_025`, `TASK_FRACTIONS_026`, `TASK_FRACTIONS_027`,
`TASK_FRACTIONS_028`, `TASK_FRACTIONS_029`, `TASK_FRACTIONS_030`.

All session positions `1, 2, 3, 4, 5` are represented. With intercept,
29 task indicators, and four position indicators, the Core matrix has:

- rows: 160 sessions;
- columns: 34;
- dimensions: **160 × 34**;
- exact rank: **34**;
- result: **full column rank**.

The rank was computed by exact rational Gaussian elimination over the binary
design matrix using Python 3.14.6. The verified Core design therefore supports
the additive fixed-effects adjustment in §9. The implementation must repeat
the identity, level, dimension, and full-rank checks before fitting. Failure
must stop primary adjustment with classification
`A1_CORE_ADJUSTMENT_STRUCTURE_BLOCKED`; no alternative model may be invented.

## 9. Exact task/session-position nuisance adjustment

For each original unscaled coordinate `j=1,...,16`, fit on eligible Core
sessions:

\[
Y_{sj}=\mu_j+\alpha_{task(s),j}+\beta_{position(s),j}+R_{sj}.
\]

The common design contains:

- intercept;
- task fixed effects;
- session-position fixed effects;
- no task × position interaction;
- equal session weights for the unweighted point estimate;
- no outcome-driven term selection.

Canonical task order is ascending numeric suffix of the frozen canonical IDs,
exactly as listed in §8. `TASK_FRACTIONS_001` is the first represented
canonical task and the reference. Position order is `1,2,3,4,5`, with
position 1 the reference. Standard treatment/dummy coding is used.

The exact 34-column order is:

1. `intercept`;
2. `task[TASK_FRACTIONS_002]` through
   `task[TASK_FRACTIONS_030]`, in numeric order;
3. `position[2]`, `position[3]`, `position[4]`, `position[5]`.

The implementation must use ordinary least squares on the 160 × 16 response
matrix, equivalently 16 independent regressions with the same `X`. The
prospective numerical procedure is `numpy.linalg.lstsq(X, Y, rcond=None)`.
The implementation artifact must record Python, NumPy, LAPACK/BLAS, platform,
and analysis-code versions. Full column rank is mandatory. Regularization,
pseudopredictor creation, imputation, data-dependent feature selection, and
outcome standardization are prohibited.

Let `R_s` be the 16-vector of OLS residuals from the unscaled original
coordinates. Define `D_A1_adj(s,r)` by replacing the raw coordinate
differences in §7 with `R_sj-R_rj` while retaining exactly the same family and
coordinate weights.

The coefficients are fitted on Core only. For an eligible ChannelLayer or
NumericalProcessing session, an adjusted residual signature is obtained by
applying those unchanged Core-fitted coefficients to that session's frozen
task and position and subtracting the prediction from its original unscaled
signature. Extension data never refit or influence the Core adjustment.

`D_A1_adj` is a nonnegative nuisance-adjusted session-distance function.
Residual coordinates can be negative or greater than one in magnitude, so
`D_A1_adj` is **not guaranteed to be bounded in `[0,1]`**.

## 10. Primary profile separation and within-profile consistency

The three distinct named objects are:

- `D_A1_raw`: raw session-distance function;
- `D_A1_adj`: nuisance-adjusted session-distance function;
- `R_WB`: primary profile-level separation/within-profile-consistency
  estimand.

They must never be conflated under an ambiguous label such as “the primary
metric.”

For each Core profile `i`, with exactly five eligible sessions, define

\[
W_i=\frac{1}{10}\sum_{\{s,r\}\subset i}[D_{A1\_adj}(s,r)]^2,
\]

where the sum covers its 10 unordered session pairs.

For each unordered pair of distinct Core profiles `(i,j)`, define

\[
B_{ij}=\frac{1}{25}\sum_{s\in i}\sum_{r\in j}
[D_{A1\_adj}(s,r)]^2.
\]

With `I=32`, the unweighted primary point estimates are

\[
W=\frac{1}{I}\sum_{i=1}^{I}W_i,
\]

\[
B=\frac{2}{I(I-1)}\sum_{i<j}B_{ij},
\]

and

\[
R_{WB}=\frac{W}{B}\quad\text{if }B>0.
\]

If `B=0`, `R_WB` is `null` with reason
`between_profile_dispersion_zero`. Lower `R_WB` means sessions sharing a
profile are relatively more similar; approximately 1 means comparable within-
and between-profile dispersion; above 1 means greater within-profile than
between-profile dispersion. It is descriptive and has no acceptance
threshold.

The primary `I=32` estimand requires five eligible sessions for every Core
profile. If that condition fails, primary `R_WB` is `null` with reason
`core_primary_population_incomplete`; a clearly labeled complete-profile
subset may be reported only as a secondary sensitivity with its actual `I`.

## 11. Secondary separation statistics

The following are fixed secondary outputs and may not be selected according to
observed favorability:

1. `B-W` using the same adjusted squared-distance components as §10;
2. family-specific `R_WB` values obtained by applying §10 separately to
   `D_M`, `D_B`, and `D_D`, with the same zero-denominator rule;
3. raw unadjusted `W_raw/B_raw`, calculated by §10 with `D_A1_raw`;
4. component distances `D_M`, `D_B`, and `D_D` for every raw and adjusted
   session pair;
5. coordinate-specific within and between dispersion, using squared
   coordinate differences and the same profile/profile-pair balancing;
6. a probability-of-superiority overlap statistic;
7. coordinate-specific ICC sensitivity estimates, never a composite ICC.

For the probability-of-superiority statistic, independently choose a Core
profile uniformly and one of its 10 within pairs uniformly, and choose one of
the 496 unordered distinct-profile pairs uniformly and one of its 25 cross
pairs uniformly. Average `h(d_w^2,d_b^2)`, where `h=1` if `d_w^2<d_b^2`,
`h=0.5` for equality, and `h=0` otherwise. Report this as
`P(adjusted within squared distance < adjusted between squared distance)`, not
as a hypothesis-test probability.

ICC sensitivity, when the structurally balanced 32 × 5 Core population and
full-rank adjustment are available, is computed for every one of the 16
adjusted residual coordinates using the one-way random-effects ICC(1,1):

\[
ICC_j=\frac{MS_{between,j}-MS_{within,j}}
{MS_{between,j}+4MS_{within,j}}.
\]

Do not truncate negative estimates. Report all 16 with the assumptions of
exchangeable sessions within profile, independent profiles, finite second
moments, and an approximately homoscedastic residual structure. If the
balanced structural prerequisite fails, every ICC is `null` with reason
`icc_balanced_design_requirement_failed`. No outcome-driven subset of
coordinates is permitted.

## 12. Same-task graph analysis

Create an undirected graph whose nodes are eligible sessions in the declared
analysis population. An edge is eligible exactly when:

- both endpoints have valid canonical identity;
- both belong to the declared population;
- `task_variant_ref` is identical;
- `stable_profile_ref` differs.

No complete profile × task factorial is required. No absent cell is imputed.
No claim may cover an unobserved profile-pair/task combination.

Each edge record retains:

- both canonical session IDs in ascending bytewise lexical order;
- task;
- both session positions;
- both profile IDs and families;
- frozen, design-only contrast metadata;
- `D_A1_raw` and its components;
- `D_A1_adj` and its components.

Design-only contrast metadata includes exact equality/difference indicators
for frozen Ground-Truth dimensions, factorial-cell identity, style variant,
and supported extension matching. It must be generated before distances are
joined to the edge table.

Raw same-task comparisons block task by construction. `D_A1_adj`
additionally removes the prospectively fitted session-position effect through
the common task+position residualization.

For distance `d` and represented task `q`, define the unweighted task mean

\[
\bar d_q=|E_q|^{-1}\sum_{e\in E_q}d_e.
\]

The overall same-task estimate is the arithmetic mean of `bar d_q` over tasks
with at least one eligible edge. Every represented eligible task has equal
weight; edge-rich tasks do not receive greater weight. Report this separately
for `D_A1_adj` and `D_A1_raw`, with adjusted designated the nuisance-adjusted
same-task summary and raw its unadjusted companion. A task with no eligible
edge remains in the audit with reason `no_eligible_same_task_edge` and is not
silently imputed.

## 13. Core and extension hierarchy

Core alone defines the primary OLS fit, `W`, `B`, and `R_WB`.

ChannelLayer is a matched secondary extension only where frozen identity
metadata supplies an exact `base_profile_id`/paired-instance relationship.
For every supported ChannelLayer-to-Core edge, require exact task and session
position agreement, retain both canonical identities, and compute signed
coordinate differences plus raw and adjusted distances. Average first over
the five matched instances per ChannelLayer profile, then give each of the
eight ChannelLayer profiles equal weight. Missing matches are not imputed.

NumericalProcessing is a separately reported secondary extension. No base
profile, paired contrast, or matched Core relationship may be inferred where
the frozen metadata does not supply one. Full 44-profile summaries are
descriptive and do not replace Core results.

## 14. Secondary profile-control characterization

These analyses characterize relationships inside the synthetic generator;
they are not validation and do not establish human realism.

### 14.1 Unit and aggregation

For Core, behavioral controls shared across style variants are analyzed at the
underlying `factorial_cell_id` level. Styled duplicates are not independent
control observations. For each cell, verify the control value is identical
across its style variants, then average the relevant session statistic with
equal session weight across all eligible sessions of both variants. A mismatch
is a structural finding and blocks that relationship with reason
`shared_control_value_mismatch`.

Each permitted relationship is summarized prospectively by a scatter table
and Spearman rank correlation across eligible factorial cells. Ranks use
average ranks for ties. Report `n_cells`, the paired values, rho, and no
confirmatory p-value. If fewer than three cells are eligible or either variable
is constant, rho is `null` with reason `insufficient_control_variation`.

For A1 v1.0.0, Spearman rank correlation is the **sole pre-specified
association summary** for these permitted relationships. No regression slope,
monotonic-slope companion, or other slope estimator is part of A1 v1.0.0, and
none may be introduced after substantive outcome inspection. The scatter-table
values and Spearman rho are descriptive internal-generator characterization;
they are not validation, calibration, evidence of human realism, or causal
inference. This parsimonious rule is fixed prospectively because there are only
16 underlying Core factorial-cell units.

### 14.2 Permitted behavior relationships

Only these approximate relationships are pre-specified:

- `clarification_request_rate` versus the cell-level equal-session mean of
  `help_seeking` incidence;
- `self_correction_rate` versus the cell-level equal-session mean of
  `verification_attempt` incidence.

### 14.3 Exact-code persistence relationship

`misconception_persistence` may be related to adjacent same-code persistence
only when the assigned design misconception code exactly equals one of the
nine operational trace codes. The response is the cell-level equal-session
mean of the §6.3 persistence value for that exact code, excluding undefined
session values with visible denominators and reasons. Non-matching codes,
including `larger_denominator_larger`, are not translated or merged.

### 14.4 Prohibited control interpretations

No one-to-one trace interpretation is supported for:

- `uncertainty_rate`;
- `transfer_attempt_rate`;
- `transfer_success_probability`;
- `answer_completeness`;
- `answer_consistency`;
- `confidence_expression_rate`;
- any non-matching design misconception code.

Style-to-linguistic-observable analysis is outside this specification unless
an independent dialogue-measure specification has already been frozen.

## 15. Missingness, validity, and exclusions

### 15.1 Deterministic session eligibility

Primary A1 session eligibility requires all of:

1. a valid exact canonical identity;
2. technically successful scientific evidence;
3. at least one learner turn;
4. one structurally valid `manifested_this_turn` object for every learner
   turn;
5. `schema_version="1.0"`;
6. `trace_type="learner_generator_self_report"`;
7. supported status, misconception, behavior, and disengagement categories;
8. all required fields with exact required types;
9. `status=arreso -> dropout_risk=explicit`.

No fuzzy matching, unknown-category coercion, imputation, or
scientific-outcome exclusion is permitted. Empty misconception arrays and
Boolean false are valid observations. Duplicate same-code entries are validly
deduplicated for incidence but retained in provenance for coherence review.

A technically successful session with a source-level coherence warning but no
structural failure remains eligible; its generator-native value is unchanged
and the warning is retained in the integrity artifact.

Every source session remains in `integrity_exclusions.jsonl` with
`eligible_session_level`, `eligible_same_task`, `eligible_primary_rwb`, and a
list of machine-readable reasons. A profile with fewer than five eligible
sessions may remain in session-level and same-task analyses but is not eligible
for the primary five-session `W_i`. The 32-profile primary `R_WB` then follows
the null rule in §10.

### 15.2 Failure classifications

At minimum, implementations must distinguish:

- `invalid_canonical_identity`;
- `technical_execution_failure`;
- `no_learner_turns`;
- `missing_trace_for_learner_turn`;
- `unsupported_schema_version`;
- `unsupported_trace_type`;
- `unsupported_category`;
- `invalid_required_field_or_type`;
- `arreso_without_explicit_dropout`;
- `profile_has_fewer_than_five_eligible_sessions`;
- `coherence_warning_only`.

The last code is a finding, not by itself an exclusion.

## 16. Core profile-cluster Bayesian bootstrap

### 16.1 Frozen RNG and replicates

Use exactly 10,000 replicates. For each replicate draw independently

\[
(w_1,\ldots,w_{32})\sim Dirichlet(1,\ldots,1).
\]

The deterministic seed is **20260827**. The RNG is NumPy
`numpy.random.Generator(numpy.random.PCG64(20260827))`, and Dirichlet draws use
`Generator.dirichlet(numpy.ones(32), size=10000)` in one call. Profiles are in
ascending bytewise lexical `stable_profile_ref` order. The execution artifact
must record the exact NumPy version. Reordering profiles or making separate
draw calls is not equivalent and is prohibited.

Each profile weight applies identically to all five of its sessions. Learner
turns are never resampled or independently weighted.

### 16.2 Weighted nuisance refit

For every replicate, refit all 16 nuisance regressions by weighted least
squares with session weight `w_i` for every session of profile `i`. Use

`numpy.linalg.lstsq(sqrt(w_session) * X, sqrt(w_session) * Y, rcond=None)`

with rowwise multiplication. Recompute residual signatures and all required
`D_A1_adj`, `W_i*`, and `B_ij*` values. Do not reuse the unweighted residuals.

After every weighted `lstsq` call, validate in this exact order:

1. the numerical rank returned by `numpy.linalg.lstsq` is exactly 34;
2. if rank is 34, every fitted coefficient is finite;
3. if the coefficients are finite, every residual required for the
   replicate's Core `W*`, `B*`, `R_WB*`, and Core same-task summaries is
   finite.

If the returned rank is not 34, mark the replicate non-estimable with reason
`bootstrap_weighted_design_rank_deficient`. If rank is 34 but any required
coefficient or residual is non-finite, mark it non-estimable with reason
`bootstrap_nonfinite_fit`. The ordered checks assign exactly one of these
reasons to a fit-guard failure.

This is a deterministic fail-closed numerical guard. Do not redraw or modify
the Dirichlet weights, regularize, change `rcond`, drop columns, reuse the
unweighted fit, replace the replicate, or substitute another fitting method.
The failed replicate remains in requested/estimable/non-estimable accounting.
The guard changes neither the scientific estimand nor the requested bootstrap
distribution or weighting design.

Compute

\[
W^*=\sum_i w_iW_i^*,
\]

and

\[
B^*=\frac{\sum_{i<j}w_iw_jB_{ij}^*}
{\sum_{i<j}w_iw_j},
\]

provided the denominator is positive. Then

\[
R_{WB}^*=W^*/B^*
\]

when `B*>0`. A nonpositive/invalid pair-weight denominator gives reason
`bootstrap_between_weight_denominator_zero`; `B*=0` gives reason
`bootstrap_between_profile_dispersion_zero`. Failed replicates remain counted
and reported by reason; they do not silently vanish.

### 16.3 Same-task bootstrap

For an eligible same-task edge joining profiles `i` and `j`, the pair weight is
`w_i w_j`. Within each represented task, compute the weighted edge mean and
normalize by that task's sum of eligible pair weights. Across tasks, take the
unweighted arithmetic mean of the task-level weighted means. Tasks never
receive weight according to bootstrap edge mass. Apply this procedure to the
adjusted same-task summary and its raw companion; adjusted distances are
recomputed from the replicate-specific weighted fit.

Because this bootstrap defines weights for the 32 Core profiles, its
same-task uncertainty result is Core-only. Extension same-task summaries are
secondary point descriptions unless a separately frozen prospective
extension uncertainty amendment is approved before their outcomes are
inspected.

### 16.4 Interval and reporting rule

The unweighted estimators in §§10 and 12 remain the primary point estimates.
For each bootstrap estimand, sort its estimable replicate values and report the
2.5th and 97.5th percentiles using NumPy percentile
`method="linear"`. Label the result exactly:

> **95% Bayesian-bootstrap uncertainty interval**

Do not label it an independent-observation classical confidence interval.
Report requested replicate count, estimable count, non-estimable count by
reason, including both weighted-fit guard codes, seed, RNG, and version. The
three counts must reconcile exactly, and failed replicates must never be
silently dropped, replaced, or redrawn. No turn-level bootstrap is permitted.

## 17. Qualitative-exhibit compatibility

This specification does not select examples. Future selection must apply the
governing deterministic same-task/different-profile Ground-Truth contrast rule
before trace metrics are attached.

Candidate selection may use frozen design metadata but must never use:

- `D_A1_raw`;
- `D_A1_adj`;
- `R_WB`;
- session length;
- termination;
- DAS;
- vividness or rhetorical attractiveness.

The candidate-set artifact must be hashed before it is joined to any A1
metric. Trace metrics may be attached only after that independent selection is
fixed.

## 18. Derived-artifact contract

No analytical output is created by this specification phase. Future outputs
must be placed under:

`data/pilot0/derived/SLEF_PILOT0_REFERENCE_RUN_3/track-a1/A1_METRICS_SPEC_v1_0_0/`

and never under frozen raw evidence or supplements.

### 18.1 Required files and deterministic sort order

| File | Minimum content | Sort order |
|---|---|---|
| `turn_encodings.jsonl` | identity, learner-turn index, raw trace provenance, `M[9]`, `B[4]`, disengagement state, cumulative `E[3]`, status, structural/coherence findings | canonical session, learner-turn index |
| `session_summaries.jsonl` | counts/rates for `Y[16]`, secondary summaries, temporal summaries, terminal descriptors, eligibility | canonical session |
| `profile_representations.jsonl` | family, profile identity, eligible session IDs/count, equal-session mean signature, completeness | family order Core/ChannelLayer/NumericalProcessing, profile ID |
| `nuisance_fit.json` | population, design levels/columns, dimensions/rank, OLS implementation/version, 16 coefficient vectors, fit eligibility | fixed keys |
| `pairwise_raw.jsonl` | endpoint identities, raw component squared distances and `D_A1_raw` | endpoint A, endpoint B |
| `pairwise_adjusted.jsonl` | endpoint identities, adjusted residual component squared distances and `D_A1_adj`, adjustment version | endpoint A, endpoint B |
| `same_task_edges.jsonl` | §12 edge contract including pre-defined contrast metadata and both distances | task, endpoint A, endpoint B |
| `within_between_consistency.json` | `W_i`, `B_ij`, `W`, `B`, `R_WB`, `B-W`, family/raw/coordinate/overlap/ICC secondary values and reasons | fixed keys; nested IDs sorted |
| `control_relationships.json` | permitted cell-level inputs, exact-code eligibility, scatter-table values, sole Spearman summaries, prohibited/nonmatching audit reasons; no slope field | relationship ID, cell ID |
| `integrity_exclusions.jsonl` | all 220 audit sessions, eligibility flags, integrity/coherence reasons | canonical session; unresolved identities last by source record ID |
| `bayesian_bootstrap_summary.json` | method, seed, RNG/version, requested/estimable/non-estimable replicate counts, returned-rank and finiteness guard definitions, failure counts by deterministic reason, intervals, optional retained replicate-file hash | fixed keys |
| `provenance_manifest.json` | complete §19 provenance and output inventory | fixed keys |
| `SHA256SUMS.txt` | SHA-256 of every derived file except itself | relative path, bytewise lexical |

`source_run_id` is exactly `SLEF_PILOT0_REFERENCE_RUN_3`. Use simple source
provenance terminology; do not use ambiguous lineage labels for ordinary
source relationships.

### 18.2 Common record conventions

Every scientific record includes `source_run_id`, `population_id`,
`canonical_session_ref` where applicable, `a1_metrics_spec_version`, and the
fixed coordinate-order version. Rates use:

```json
{"numerator": 0, "denominator": 1, "value": 0.0}
```

Undefined values use the §6.5 object. Arrays that represent coordinates use
the fixed 16-order and are accompanied by `coordinate_order_version`.

Profile mean signatures are equal-session means. They are not used in place
of the pair-balanced primary `R_WB`. If a profile has no eligible sessions,
its mean signature is `null` with reason `no_eligible_sessions`.

### 18.3 Machine-readable schema sketch

```json
{
  "source_run_id": "SLEF_PILOT0_REFERENCE_RUN_3",
  "canonical_session_ref": "<string>",
  "stable_profile_ref": "<string>",
  "profile_family": "Core|ChannelLayer|NumericalProcessing",
  "task_variant_ref": "TASK_FRACTIONS_NNN",
  "session_position": 1,
  "n_valid_learner_turns": 1,
  "coordinate_order_version": "a1_signature_16_v1.0.0",
  "signature_counts": ["<16 nonnegative integers>"],
  "signature_rates": ["<16 finite numbers in [0,1]>"],
  "final_status": "continua|risolto|arreso",
  "termination_reason": "status_risolto|status_arreso|max_learner_turns_reached",
  "maximum_turn_boundary": false,
  "eligibility": {"session_level": true, "primary_rwb": true},
  "integrity_reasons": []
}
```

```json
{
  "endpoint_a": "<canonical session ID>",
  "endpoint_b": "<canonical session ID>",
  "distance_version": "a1_raw_v1.0.0|a1_adjusted_v1.0.0",
  "d_m_squared": "<finite nonnegative number>",
  "d_b_squared": "<finite nonnegative number>",
  "d_d_squared": "<finite nonnegative number>",
  "distance": "<finite nonnegative number>"
}
```

## 19. Deterministic provenance, serialization, and hashing

Every derived output must record:

- governing `ANALYSIS_SPEC_v1_0_2` identity and hash;
- frozen `A1_METRICS_SPEC_v1_0_0` identity and owner-approved hash;
- `source_run_id=SLEF_PILOT0_REFERENCE_RUN_3`;
- producing baseline
  `6d6089f2242b5d95852d78ab3006f89f1078d316`;
- every consumed frozen-artifact path and verified SHA-256;
- analysis-code commit and dirty-worktree state;
- trace-encoding version `a1_trace_encoding_v1.0.0`;
- raw-distance version `a1_raw_v1.0.0`;
- adjusted-distance version `a1_adjusted_v1.0.0`;
- task/position-adjustment version `a1_task_position_fe_v1.0.0`;
- population definition and all exclusions;
- Bayesian-bootstrap method, 10,000 replicates, seed 20260827, RNG and exact
  NumPy version;
- weighted-fit guard version `a1_bootstrap_weighted_fit_guard_v1.0.0`, required
  returned rank 34, coefficient/residual finiteness checks, and failure counts
  by reason;
- deterministic input and output sort orders;
- Python, NumPy, LAPACK/BLAS, OS/platform, and analysis entry-point identity;
- every output SHA-256.

JSON and JSONL are UTF-8 with LF endings, object keys sorted bytewise,
compact separators, and exactly one terminal LF per file. Serialization must
reject non-finite floats (`allow_nan=False` or equivalent). JSONL has one
canonical object per line. Hash bytes only after final canonical
serialization. `SHA256SUMS.txt` excludes itself to avoid recursion.

No output is valid if the child-spec status is not frozen/owner-approved or
its recorded hash does not match the file consumed by the analysis.

## 20. Reporting requirements and prohibited claims

Every A1 report must state:

- audit, eligible session-level, same-task, and primary Core populations;
- raw turn/session/profile denominators and all exclusions;
- the exact 16-coordinate order and operational-vocabulary limitation;
- separate definitions and labels for `D_A1_raw`, `D_A1_adj`, and `R_WB`;
- task/position matrix dimensions/rank and adjustment implementation;
- unweighted primary point estimates and Bayesian-bootstrap uncertainty;
- equal-task weighting for same-task summaries;
- Core primary versus extension hierarchy;
- all pre-specified secondary results regardless of direction;
- Spearman rho as the sole control-association summary, the supporting
  scatter-table values, and the absence of slopes and confirmatory p-values;
- bootstrap requested/estimable/non-estimable counts, including deterministic
  weighted-rank and non-finite-fit failure counts;
- A1/A2 boundary and generator-native semantics;
- known limitations in §21.

Reports must not claim:

- that an A1 declaration was externally visible or human-observed;
- that A1 validates psychological realism, Ground Truth, or a clinical
  construct;
- that low distance or low `R_WB` is an acceptance pass;
- that one Run 3 tutor condition is superior to another tutor;
- that task adjustment makes `D_A1_adj` causal;
- that `D_A1_adj` is bounded in `[0,1]`;
- that Bayesian-bootstrap intervals are classical independent-observation
  confidence intervals;
- that non-matching misconception vocabularies are equivalent;
- that extension families redefine Core;
- that status `continua` is measured engagement;
- that `risolto` alone determines actual termination.

## 21. Known limitations

1. A1 measures generator-native declarations, not independent textual
   observation; external observability belongs to A2.
2. The nine-code operational trace vocabulary is not isomorphic to the
   assigned design vocabulary. This prevents post-hoc translation of
   non-matching codes.
3. Five sessions per profile limit profile-specific precision.
4. The task assignment is additive-task/position separable but imbalanced and
   not a complete profile × task factorial.
5. Nuisance residualization is descriptive adjustment; it does not create a
   randomized causal effect of task or position.
6. Cumulative disengagement coordinates preserve ordinal direction without
   directly encoding the four category labels as interval values `0,1,2,3`.
   Equal weights on the three cumulative thresholds impose the prospective
   normative convention that each adjacent threshold crossing contributes
   equally to squared disengagement-family distance; this is not an
   empirically learned scale. The three coordinates are also logically
   dependent.
7. `D_A1_raw` family balancing is a prospective normative weight choice, not
   an empirically learned scale.
8. Core control relationships characterize the synthetic generator and have
   only 16 underlying factorial-cell units.
9. ChannelLayer and NumericalProcessing evidence is secondary and admits no
   clinical interpretation.

These are reporting limitations, not post-outcome reasons to alter the metric
or exclude scientific evidence.

## 22. Freeze and amendment procedure

Owner scientific review and differential freeze review are complete. This
document is frozen and owner-approved as the normative basis for A1
implementation. The frozen status permits implementation development but does
not by itself authorize scientific execution.

Before scientific A1 execution:

1. the implementation must bind to the exact externally recorded frozen
   specification SHA-256;
2. required automatic tests must pass;
3. the V-model and manual verification gates in §§23–25 must be completed;
4. implementation and source-provenance verification must satisfy this
   specification.

After freeze, any change to fields, coordinates, weights, denominators,
adjustment, population, estimand, uncertainty, or eligibility requires a
versioned amendment stating what changed, why, whether relevant outcomes had
become visible, and which outputs are affected. Post-freeze additions made
after outcome inspection are labeled `EXPLORATORY / POST-SPECIFICATION` and
cannot replace the frozen estimands.

## 23. V-model verification matrix

| Requirement/design item | Implementation verification | Independent/manual gate |
|---|---|---|
| Frozen source and identity hashes | hash fixture and pre-execution hash gate | compare manifest to frozen evidence inventory |
| Nine-code operational vocabulary | parser allowlist and unknown-code rejection tests | compare baseline source, contract, and prompt |
| Fixed 16-coordinate order | exact-array/order unit test | inspect schema and one synthetic record |
| Turn deduplication and co-occurrence | multi-code/duplicate fixtures | review raw-to-encoded fixture trace |
| `n_s` denominators and raw counts | hand-calculated session fixtures | denominator audit |
| Temporal null semantics | onset/persistence/transition/run fixtures | inspect all reason codes |
| Status/termination separation | `risolto` follow-up and max-boundary fixtures | source-semantic audit |
| `D_A1_raw` weights/bound | known-vector and all-zero/all-one tests | formula review |
| Core task+position adjustment | 160 × 34 rank assertion and rank-deficient failure fixture | reproduce structural-only rank check |
| `D_A1_adj` residual construction | hand-calculated OLS fixture and unbounded synthetic fixture | numerical implementation/version audit |
| `W`, `B`, `R_WB` | small balanced-profile fixture | pair-count and equal-weight audit |
| Secondary separation statistics | hand-calculated component/overlap/ICC fixtures | no outcome-selected output audit |
| Same-task equal-task weighting | unequal-edge-count fixture | edge eligibility and task weighting audit |
| Extension hierarchy | matched/unmatched identity fixtures | verify no inferred NumericalProcessing base link |
| Control relationships | paired-style, exact-code, tied-rank, constant-input, and Spearman-only schema fixtures | underlying-cell unit audit; confirm no slope statistic or confirmatory p-value |
| Missingness/exclusion visibility | one fixture per integrity reason | reconcile audit population to source count |
| Profile-cluster Bayesian bootstrap | fixed-draw reproducibility, hand-weight, returned-rank failure, non-finite coefficient, non-finite residual, and no-redraw/no-replacement fixtures | confirm common profile weight across five sessions and exact requested/estimable/non-estimable reconciliation |
| Canonical JSON/hashes | non-finite rejection and byte-identical rerun tests | independent SHA-256 reproduction |
| Qualitative-selection independence | design-metadata-only candidate fixture | verify candidate hash predates metric join |

No scientific execution passes the V-model gate until automatic tests pass and
the corresponding manual checks are signed off.

## 24. Synthetic-fixture test requirements

Automatic tests must use synthetic data only and cover at minimum:

1. empty misconception arrays and all-false behaviors as valid zeros;
2. duplicate same-code entries counted once and retained for provenance;
3. simultaneous different misconceptions and behavior flags;
4. all four disengagement states and cumulative patterns `000/100/110/111`,
   including equal squared-distance contribution from each adjacent threshold
   crossing under the unchanged `1/9` coordinate weights;
5. rejection of direct interval-scale `0,1,2,3` disengagement encoding and
   unknown categories;
6. `arreso` without `explicit` as structurally invalid;
7. `continua`, final status, `risolto`, termination reason, and max boundary as
   separate fields;
8. exact `n_s` count/rate denominators;
9. all persistence, transition, first-onset, and run-length undefined cases;
10. `D_A1_raw=0` for identical signatures and `D_A1_raw=1` for the synthetic
    all-zero versus all-one signature;
11. exact family and coordinate weights;
12. no z-scoring, prevalence weighting, or empirical normalization;
13. the exact 34 design columns, reference levels, full-rank pass, and
    rank-deficient hard stop;
14. OLS residualization of unscaled coordinates and a synthetic
    `D_A1_adj>1` case showing no false bound;
15. 10 within pairs, 25 cross pairs, equal profile/profile-pair weights, and
    the `B=0` null reason;
16. raw and family-specific ratios, `B-W`, overlap tie handling, and all 16
    non-truncated ICC estimates;
17. same-task eligibility without factorial completion and equal task weights
    under unequal edge counts;
18. ChannelLayer exact matching and prohibition on invented
    NumericalProcessing matching;
19. underlying-factorial-cell aggregation, rejection of non-matching
    misconception translation, average-rank tie handling, Spearman as the sole
    association summary, and absence of slope/p-value fields;
20. incomplete-profile handling without turn or session imputation;
21. deterministic PCG64 draws, one profile weight shared by five sessions,
    replicate-specific WLS refits, weighted `W*`, normalized `B*`, and
    same-task pair weights;
22. exact returned-rank-34 validation; non-finite coefficient/residual
    detection; deterministic `bootstrap_weighted_design_rank_deficient` and
    `bootstrap_nonfinite_fit` reasons; no redraw, weight modification,
    regularization, `rcond` change, column dropping, unweighted-fit reuse, or
    replacement; exact replicate-count reconciliation;
23. exact linear percentiles and bootstrap failure accounting;
24. JSON rejection of `NaN`, positive/negative infinity, and canonical
    byte-identical serialization;
25. deterministic sorting and checksum-manifest coverage.

No fixture may contain real student data or invoke an external model/provider.

## 25. Manual audit requirements

Before execution and again before reporting, a human reviewer must verify:

- child-spec status/hash and governing-spec status/hash;
- producing baseline and all consumed evidence hashes;
- no source artifact was modified;
- canonical identity reconciliation and population counts;
- the exact coordinate and task/position column orders;
- the 160 × 34, rank-34 Core structural result using assignment fields only;
- no substantive manifestation distribution was used in method selection;
- no Proxima L/M, Gemini, DAS, or A2 value entered A1 encoding;
- every exclusion remains visible and has a machine-readable reason;
- equal session, profile, profile-pair, and task weighting where specified;
- bootstrap seed/RNG/version and absence of learner-turn resampling;
- bootstrap returned-rank/finiteness guards, failure reasons, and exact
  requested/estimable/non-estimable reconciliation without redraw or
  replacement;
- Spearman-only control-association output with no slope statistic or
  confirmatory p-value;
- separation of `D_A1_raw`, `D_A1_adj`, and `R_WB` in tables and prose;
- `[0,1]` is claimed only for `D_A1_raw`;
- operational-vocabulary and A1/A2 limitations are reported;
- qualitative candidate selection remained independent of A1 outcomes;
- output SHA-256 values reproduce from canonical bytes;
- no prohibited claim appears.

## Appendix A. Formula summary

Let `w_M=1/27`, `w_B=1/12`, and `w_D=1/9` per coordinate within their
families. Then

\[
D_{A1\_raw}(s,r)=\sqrt{
\sum_{j=1}^{9}\frac{(Y_{sj}-Y_{rj})^2}{27}+
\sum_{j=10}^{13}\frac{(Y_{sj}-Y_{rj})^2}{12}+
\sum_{j=14}^{16}\frac{(Y_{sj}-Y_{rj})^2}{9}}.
\]

For `R=Y-X(X'X)^{-1}X'Y` conceptually, with the required numerical least-
squares implementation used instead of explicit inversion,

\[
D_{A1\_adj}(s,r)=\sqrt{
\sum_{j=1}^{9}\frac{(R_{sj}-R_{rj})^2}{27}+
\sum_{j=10}^{13}\frac{(R_{sj}-R_{rj})^2}{12}+
\sum_{j=14}^{16}\frac{(R_{sj}-R_{rj})^2}{9}}.
\]

The primary profile estimand is `R_WB=W/B`, with `W_i`, `B_ij`, `W`, and `B`
defined in §10 and the zero/incomplete-population rules applied before
division.

## Appendix B. Machine-readable constants sketch

```json
{
  "spec_id": "A1_METRICS_SPEC_v1_0_0",
  "status_required_for_execution": "FROZEN — OWNER APPROVED",
  "source_run_id": "SLEF_PILOT0_REFERENCE_RUN_3",
  "producing_baseline": "6d6089f2242b5d95852d78ab3006f89f1078d316",
  "trace_schema_version": "1.0",
  "trace_type": "learner_generator_self_report",
  "coordinate_order_version": "a1_signature_16_v1.0.0",
  "family_sizes": {"misconception": 9, "behavioral": 4, "disengagement": 3},
  "squared_coordinate_weights": {
    "misconception": 0.037037037037037035,
    "behavioral": 0.08333333333333333,
    "disengagement": 0.1111111111111111
  },
  "core_profiles": 32,
  "sessions_per_profile": 5,
  "bootstrap_replicates": 10000,
  "bootstrap_seed": 20260827,
  "rng": "numpy.random.Generator(numpy.random.PCG64)",
  "bootstrap_weighted_fit_guard": {
    "version": "a1_bootstrap_weighted_fit_guard_v1.0.0",
    "required_rank": 34,
    "require_finite_coefficients": true,
    "require_finite_required_residuals": true,
    "rank_failure_reason": "bootstrap_weighted_design_rank_deficient",
    "nonfinite_failure_reason": "bootstrap_nonfinite_fit",
    "redraw_or_replacement_allowed": false
  },
  "control_association_summary": "spearman_rank_correlation_only",
  "percentile_method": "linear"
}
```

Decimal weights in this sketch are serialization conveniences only. The
normative values are the exact fractions `1/27`, `1/12`, and `1/9` in §7.
