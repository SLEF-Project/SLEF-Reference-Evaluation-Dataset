# SLEF DAS_extractor Specification v1.0.7

**Document ID:** `DAS_EXTRACTOR_SPEC_v1_0_7`
**Version:** 1.0.7
**Status:** FROZEN — OWNER APPROVED
**Created:** 2026-08-29
**Last modified:** 2026-08-30
**Initial source run:** `SLEF_PILOT0_REFERENCE_RUN_3`
**Provider/model:** Google Gemini / `gemini-3.1-pro-preview` (preview)

## Changelog

| Date | Version | Change |
| --- | --- | --- |
| 2026-08-30 | 1.0.7 | Superseded v1.0.6 before any scientific DAS extraction after GT-blind real-session repeatability exposed unstable interpretation of one isolated incorrect application. Clarified only the already-authorized Misconception construct boundary: `PRESENT` requires sufficient behavioral persistence/coherence of a stable incorrect model, while forced choice applies after construct identification and cannot promote an isolated error into a misconception. Provider configuration, schema, all other category semantics, scoring, uncertainty, population, and comparison-family rules remain unchanged. During pre-freeze semantic validation, provider HTTP 499 request closure was narrowly classified as transient/retriable; this technical mapping does not change the scientific instrument. |
| 2026-08-30 | 1.0.6 | Superseded v1.0.5 before any full scientific DAS extraction after its real one-session preflight ended with provider `finish_reason=MAX_TOKENS` and incomplete JSON; increased only the maximum output-token ceiling from 2048 to 32768 and added the causal technical failure class `gemini_max_tokens_incomplete_output`. Forced-choice semantics and every other scientific rule remain unchanged. |
| 2026-08-30 | 1.0.5 | Superseded v1.0.4 before any scientific DAS result; changed only the classification decision policy from potentially conservative abstention wording to explicit forced-choice evidence-based classification, with `INSUFFICIENT_EVIDENCE` retained as exceptional abstention for lack of discriminating evidence or meaningful observation opportunity. Provider, model, configuration, schema, categories, evidence attribution, scoring, uncertainty, population, and comparison-family rules remain unchanged. |
| 2026-08-29 | 1.0.4 | Superseded v1.0.3 before any successful scientific DAS extraction after its first structural smoke reached Gemini 3.1 but returned malformed/incomplete structured output with an unterminated JSON string; increased only the maximum output-token ceiling from 512 to 2048 and added safe stderr retry observability without claiming a proven cause for the failure. All scientific DAS rules remain unchanged. |
| 2026-08-29 | 1.0.3 | Activated the preregistered OPEN-family model-unavailability rule after the v1.0.2 smoke received a permanent pre-output HTTP 404; migrated the common extractor to Google `gemini-3.1-pro-preview`, fixed temperature at 1.0 with model-default thinking left unset, and added permanent-provider fail-fast handling. All other v1.0.2 scientific rules remain unchanged. |
| 2026-08-29 | 1.0.2 | Superseded v1.0.1 before any scientific extraction; clarified evidence attribution for Misconception ABSENT and Metacognition LOW; defined misconception subtype as a secondary conditional descriptive output; and froze OPEN/CLOSED comparison-family and extractor-model-unavailability rules. All other v1.0.1 scientific rules remain unchanged. |
| 2026-08-29 | 1.0.1 | Superseded v1.0.0 before any scientific extraction; classified DAS_extractor as an interaction-level recoverability measure; added mandatory learner-turn evidence attribution, condition blindness, canonical cross-provider transcript normalization, conservative provider/model-role independence, the fixed cross-condition instrument rule, and a pre-registered A1-informed Misconception interpretation. Scientific categorical scoring, retry, and uncertainty estimands remain unchanged. |

## 1. Authority, supersession, and precedence

`DAS_EXTRACTOR_SPEC_v1_0_7` supersedes
`DAS_EXTRACTOR_SPEC_v1_0_6` before any scientific DAS extraction. No
scientific DAS result was generated under v1.0.0, v1.0.1, v1.0.2, v1.0.3, or
v1.0.4, and no full scientific result was generated under v1.0.5 or v1.0.6. The earlier
versions remain preserved as historical pre-execution
evidence and are not executable scientific authorities after this freeze. All
v1.0.6 scientific semantics other than the authorized Misconception construct
clarification remain unchanged in v1.0.7.

### 1.1 v1.0.7 pre-scientific Misconception clarification

GT-blind repeatability validation of v1.0.6 on one real Run 3 transcript was
technically complete in three of three calls, but the primary Misconception
classification varied: one call returned `ABSENT`, while two returned
`PRESENT` based only on learner turn 1. No Ground Truth was inspected or used.
This exposed ambiguity between the forced-choice rule and the already normative
definition of Misconception as a stable incorrect explanatory or procedural
model rather than a single error.

Version 1.0.7 makes that existing construct boundary operational. `PRESENT`
requires sufficient behavioral persistence or coherence to distinguish a
stable incorrect model from a single wrong answer, isolated slip, arithmetic
mistake, accidental inconsistency, or one tentative incorrect hypothesis that
is immediately abandoned. Persistence/coherence may be evidenced by repeated
application, an articulated incorrect rule followed by consistent reasoning,
maintenance or reapplication after reconsideration, or use across related
steps/examples. These are illustrations, not a mechanical checklist, and no
fixed turn-count threshold is imposed.

If an initial incorrect rule is later rejected, revised, or abandoned without
sufficient prior persistence, the result is `ABSENT` when meaningful
misconception-relevant observation opportunity exists and
`INSUFFICIENT_EVIDENCE` when it does not. If sufficient behavior first
establishes a stable misconception and the learner later genuinely corrects
it, the earlier stable model may still support `PRESENT`; the category does not
mean the misconception remains active at the final turn.

Forced choice operates only after determining what construct the learner
behavior establishes. It cannot turn an isolated error into a stable
misconception merely because `PRESENT` appears marginally more plausible than
`ABSENT`. This clarification does not tune an observed category frequency,
define a turn threshold, expose Ground Truth, or encode the known regression
session or its expected classification. No other scientific or technical rule
changes.

### 1.2 v1.0.6 pre-scientific generation-ceiling correction

The real v1.0.5 preflight on
`CHVAR_CH01_CORE_CELL_01_style_a::S1` reached
`gemini-3.1-pro-preview` using the frozen model-default/high reasoning
configuration. The provider returned `finish_reason=MAX_TOKENS`, with observed
usage of 2,902 prompt tokens, 1,966 thought tokens, and 68 candidate/output
tokens. The application-visible response was incomplete JSON and no valid
categorical reconstruction or scientific DAS result was produced.

For this specific v1.0.5 event, the provider finish metadata establishes
`root_cause = generation_ceiling_exhausted`: Gemini exhausted the configured
2,048-token generation ceiling before completing the structured response.
Version 1.0.6 therefore raises only `max_output_tokens` from 2,048 to 32,768.
The value 32,768 is a ceiling, not requested token consumption, and no
scientific interpretation is attached to actual or maximum token consumption.
Model reasoning configuration remains unset/model-default; model, temperature,
seed, API, prompt semantics, schema, parser semantics, categories, evidence
rules, scoring, population, bootstrap, and comparison-family rules remain
unchanged.

The causal classification is not applied retroactively. The earlier v1.0.3 and
v1.0.4 malformed/incomplete-output events remain
`root_cause = not_established` unless their historical provider metadata
independently established a finish reason. Malformed JSON without
`finish_reason=MAX_TOKENS` remains the generic technical class
`gemini_invalid_structured_output`. Malformed or otherwise invalid structured
output with provider `finish_reason=MAX_TOKENS` is recorded prospectively as
`gemini_max_tokens_incomplete_output`. This distinction changes observability,
not scientific classification or scoring.

### 1.3 v1.0.5 pre-scientific decision-rule amendment

Version 1.0.5 changes one scientific semantic rule before any full scientific
extraction: DAS classification is explicitly a forced-choice evidence-based
classification. For every dimension, the extractor selects the substantive
category better supported by observable learner behaviour even when meaningful
uncertainty remains. Absolute certainty and formal proof are not required.

`INSUFFICIENT_EVIDENCE` remains available as an exceptional abstention only
when there is essentially no meaningful evidence, no genuine opportunity to
observe the construct, or no reasonable evidential basis for preferring either
substantive category. Imperfect evidence, residual uncertainty, another
possible interpretation, or confidence below certainty is not by itself a
basis for abstention.

Conceptual examples such as evidence being roughly 60/40 in favour of `HIGH`
or 55/45 in favour of `PRESENT` illustrate only that the better-supported
category is selected. They do not define, request, calculate, return, or
calibrate probabilities or confidence. The output remains categorical only.

No target or quota is defined for `INSUFFICIENT_EVIDENCE`: no empirical rate
such as 2%, 5%, or 10% may be imposed. Its observed frequency remains an
empirical output. Version 1.0.5 does not force a substantive classification
when the construct was not meaningfully observable. In particular, no genuine
transfer opportunity remains a legitimate `INSUFFICIENT_EVIDENCE` case.

Provider, exact model, temperature, seed, thinking configuration, output-token
ceiling, API, SDK, prompt inputs, structured schema, category sets, evidence-
turn rules, scoring, bootstrap, population, provenance, and OPEN comparison-
family semantics are unchanged. Historical v1.0.4 remains frozen.

### 1.4 v1.0.3 malformed-output smoke and technical instrument amendment

On 2026-08-29, v1.0.3 reached its first live structural smoke attempt using
Google `gemini-3.1-pro-preview`, temperature 1.0, seed `20260827`, unset/model-
default thinking, maximum output tokens 512, the frozen structured JSON schema,
and the frozen prompt. The provider call successfully reached Gemini and
returned model output. That output was malformed/incomplete JSON and could
not be parsed. Python raised
`json.decoder.JSONDecodeError: Unterminated string`; the runtime converted this
to `DASStructuredOutputError: provider output is not JSON` and then
`DASTechnicalAttemptError: gemini_invalid_structured_output`.

The runtime entered the existing 120-second retry wait, which the operator
interrupted with `KeyboardInterrupt`. The interrupt was not the root cause.
This was not model unavailability or quota failure: Gemini 3.1 was reached,
but no valid parsed extractor output, categorical reconstruction, Ground-Truth
recovery score, or scientific DAS result was produced. No scientific condition
has produced a DAS result, the Pilot-0 comparison family remains OPEN, and no
re-extraction is required.

The v1.0.3 smoke returned malformed/incomplete structured output with an
unterminated JSON string. Because the 512-token ceiling was a plausible
technical constraint but no provider finish reason established truncation as
the direct cause, v1.0.4 increases the output-token ceiling to 2048 as a pre-
scientific technical correction without attributing the failure to a proven
cause. It also adds safe stderr retry observability. The prompt, model,
temperature, seed, model-default thinking, schema, parser, scientific
categories, evidence rules, scoring, population, bootstrap, and comparison-
family rules remain unchanged. Version 1.0.4 became the intended common
instrument, then was superseded by v1.0.5 before any scientific result.

### 1.5 v1.0.2 smoke and instrument-version event

On 2026-08-29, v1.0.2 reached its first live smoke attempt using
`gemini-2.5-pro`. Google returned HTTP 404:

`This model models/gemini-2.5-pro is no longer available to new users.`

The rejection occurred before any model output. No parsed extractor output,
categorical reconstruction, or DAS scientific result was produced. The v1.0.2
retry logic entered its fixed 120-second wait; after the permanent nature of
the error was identified, the operator interrupted that unnecessary wait.
`KeyboardInterrupt` was not the root cause. The root cause was permanent
extractor-model unavailability.

The already preregistered OPEN comparison-family instrument-version rule
therefore applies. The Pilot-0 family remains OPEN, no condition has produced a
DAS scientific result, and there is nothing to re-extract. Version 1.0.3 is the
common extractor instrument for Proxima and every subsequent condition in this
OPEN family.

This child specification is the normative SLEF specification for
`DAS_extractor` from version 1.0.7 forward. It is governed by
`docs/pilot0/analysis/ANALYSIS_SPEC_v1_0_2.md` except where that older frozen
specification contains incompatible DAS_extractor requirements. For
`DAS_extractor`, this specification supersedes incompatible requirements for:

- a fixed `MEDIUM` category;
- probabilities or confidence scores;
- Brier score, calibration, cross-entropy, partial credit, or ordinal distance;
- treating DAS as direct tutor-internal diagnostic accuracy; and
- inclusion of T17 evidence-volume analysis inside DAS_extractor.

The older general specification and `A1_METRICS_SPEC_v1_0_0` remain unchanged
and frozen. T17 is a separate companion analysis and does not block
DAS_extractor implementation or execution. This precedence is permanent and
is not a Run-3-specific exception.

The general categorical rule is:

> DAS_extractor performs forced-choice evidence-based categorical
> reconstruction using exactly the preregistered Ground Truth categories
> applicable to the study being evaluated, plus exceptional abstention through
> `INSUFFICIENT_EVIDENCE` when discriminating evidence or meaningful
> observation opportunity is absent.

The category space is study-dependent. A future study may include `MEDIUM` only
when that study preregisters `MEDIUM` in its Ground Truth. Pilot-0 does not.

## 2. Scientific construct and evidence-layer separation

The normative construct is:

> DAS_extractor is an interaction-level Ground-Truth recoverability measure
> under a specific tutor condition.

The observed conversation is jointly produced by:

`SLEF learner manifestation × tutor interaction policy`.

The tutor condition may influence which learner evidence is elicited, which
errors are explored, whether clarification or verification occurs, whether a
transfer opportunity arises, and how much learner-state information becomes
observable. DAS_extractor measures how recoverable assigned Ground Truth is
from learner evidence in that realized conversation. It does not reveal the
tutor's private or internal learner-state representation.

The evidence layers are permanently separated:

| Layer | Construct | Primary subject |
| --- | --- | --- |
| A1 | Generator-native manifestation characterization | SLEF learner generator |
| A2 | External observability of declared manifestations in realized dialogue | Realized manifestation under interaction |
| DAS_extractor | Interaction-level recoverability of assigned Ground Truth from learner evidence in the realized conversation | SLEF × tutor interaction condition |
| Tutor-native or tutor-elicited readout | Tutor-attributable diagnostic representation | Tutor's own learner-state estimate |

When comparator conditions exist, the same DAS_extractor may be compared
across conditions. A supported comparison may state:

> One interaction condition made the learner Ground Truth more externally
> recoverable than another.

It must not be converted into a claim that the tutor internally knew the
learner state with that accuracy. DAS_extractor does not establish human
realism, psychological validity, pedagogical effectiveness, calibration, or a
tutor-internal causal mechanism.

## 3. Pre-registered interpretation of dimension heterogeneity

Before any DAS extraction, frozen Track A1 Core family summaries provide the
following descriptive context:

- Misconception family `R_WB = 0.8387358943301025` (approximately 0.84);
- Behavioral family `R_WB = 0.4675020061632003` (approximately 0.47);
- Disengagement family `R_WB = 0.9812010850074449` (approximately 0.98).

The pre-registered interpretation is:

> Track A1 provides prior evidence that misconception-related generator-native
> manifestations show weaker profile differentiation than behavioral
> manifestations in the current run. Therefore, if DAS_extractor later shows
> weaker Ground-Truth recovery for Misconception, that result would be
> compatible with weaker or less distinctive learner manifestation signal and
> must not automatically be attributed to tutor diagnostic weakness.

And:

> A1 does not entail that Misconception DAS must be lower, because A1 and
> DAS_extractor operate on different representations and estimands.

This is a pre-specified interpretive prior, not a causal prediction, numerical
expected DAS value, pass threshold, or acceptance rule.

## 4. Frozen Pilot-0 sources and identities

The exact initial source run is `SLEF_PILOT0_REFERENCE_RUN_3`. The Pilot-0
implementation fails before any provider call unless the source-root basename
and frozen `RUN_STATUS.json.execution_id` both equal that value.

The canonical sources are:

- Ground Truth and profiles: frozen `manifest.snapshot.json`, schema
  `pslp.slef.single_pass_manifest` v1.0.0;
- session Ground Truth materialization: frozen
  `learner_cards.snapshot.json`;
- completed dialogue: frozen `transcripts.jsonl`, schema
  `pslp.slef.session_transcript_record` v1.0.0;
- terminal success: frozen `attempts.jsonl` and `run_descriptor.json`;
- canonical scientific identity: manifest, learner cards, and
  `supplements/identity/source/ART-11-mapping-return-RUN-08A.5.json`.

The exact Pilot-0 identity tuple is:

1. `stable_profile_ref`;
2. `session_position`;
3. `task_variant_ref`;
4. `canonical_session_ref`;
5. `instance_plan_id`.

Every available identity element matches exactly across joined sources. No
fuzzy matching, case folding, suffix repair, inferred task, or substitution is
permitted. Every consumed file is SHA-256 verified before a provider call or
scientific calculation and recorded in provenance.

## 5. Pilot-0 Ground Truth and misconception catalog

The Pilot-0 manifest `ground_truth` object has exactly:

- `knowledge`: `low` or `high`;
- `misconception`: `absent` or `present`;
- `misconception_type`: `null` when absent, otherwise one exact catalog code;
- `metacognition`: `low` or `high`;
- `transfer`: `low` or `high`.

The canonical Pilot-0 fractions misconception catalog is, in order:

1. `adds_numerators_and_denominators`;
2. `larger_denominator_larger`.

Catalog codes are never uppercased, translated, normalized, or replaced by the
distinct A1 operational manifestation vocabulary.

## 6. Population and eligibility

The initial population is the single-condition Proxima Reference Run
population. It is not called CFAP. All scientifically eligible completed
sessions for which the four Ground Truth dimensions are defined are included.

Eligibility requires:

- valid exact source-run and canonical identity;
- a terminal successful source attempt;
- exactly one structurally valid completed transcript;
- at least one learner turn and one tutor turn;
- contiguous positive turn numbers with supported roles;
- all four Ground Truth dimensions defined with Pilot-0 values; and
- a valid conditional `misconception_type`.

No session is excluded because it is difficult, ambiguous, produces
`INSUFFICIENT_EVIDENCE`, or disagrees with Ground Truth. Source-integrity or
eligibility failures remain visible with deterministic reasons. The frozen Run
3 source contains 44 profiles, five sessions per profile, and 220 sessions,
but eligibility is never outcome-driven.

## 7. Canonical transcript normalization and condition blindness

The canonical extractor input is an ordered sequence of objects with exactly:

- `turn_number`: contiguous positive integer;
- `speaker`: `LEARNER` or `TUTOR`;
- `content`: original semantic dialogue content.

Each object is serialized as one compact JSON line with keys in the order
`turn_number`, `speaker`, `content`. Current Run 3 transcript records already
have chronological `turn_number`, `student`/`tutor` roles, and original Italian
`content`; normalization maps only `student` → `LEARNER` and `tutor` → `TUTOR`.

Future provider-specific raw formats may be normalized only by:

- mapping provider-specific dialogue roles to `LEARNER`/`TUTOR`;
- preserving chronological order and original semantic content; and
- removing transport-only metadata that is not part of the dialogue.

Normalization must not paraphrase, summarize, translate, add explanatory text,
remove substantive dialogue content, add tutor/provider or condition identity,
add Ground Truth, or add learner-profile metadata. Every condition evaluated
under this instrument receives the same semantic input representation.

The provider request contains only:

- the exact frozen extractor prompt;
- study-specific closed definitions and misconception catalog inside that
  prompt; and
- the canonical chronological dialogue with `LEARNER`/`TUTOR` roles.

No out-of-dialogue condition or provider identity is supplied. In particular,
the request builder does not accept or serialize `Proxima`, `ChatGPT`, `Claude`,
`Mistral`, provider labels, condition IDs, profile/session/task IDs, execution
metadata, learner-card state, generator controls, style, ChannelLayer,
NumericalProcessing, Ground Truth, expected classification, execution trace,
or tutor-native telemetry. Substantive dialogue content is preserved rather
than redacted, so metadata blindness is not a claim that a condition could
never be inferred from the conversation itself.

## 8. Learner-only evidence and attribution

Tutor turns may establish conversational context only. Tutor statements or
judgements about learner knowledge, misconception, confusion, monitoring, or
transfer are not learner-state evidence. Classification evidence must come
from observable learner utterances or behaviour.

Every dimension output includes `evidence_turns`, an ascending list of unique
transcript `turn_number` values. The runtime validates that every reference:

- resolves to an actual transcript turn;
- identifies a `LEARNER` turn; and
- never identifies a `TUTOR` turn.

When `value` is an applicable Ground Truth category rather than
`INSUFFICIENT_EVIDENCE`, at least one learner evidence turn is required. When
`value` is `INSUFFICIENT_EVIDENCE`, `evidence_turns` must be empty. No
free-form rationale is requested or accepted.

For categories partly defined by absence or low incidence of a behaviour, a
non-empty evidence attribution refers to learner turns establishing sufficient
evaluation opportunity and the observable behaviour supporting the category.
It is not interpreted as a claim that one isolated turn proves an absence.
This rule applies especially to Misconception `ABSENT` and Metacognition
`LOW`. It creates no exception to the non-empty evidence requirement.

This attribution check does not prove that a black-box LLM internally ignored
all tutor statements. It provides an auditable evidentiary constraint:

> Every reported classification must be supportable by explicitly identified
> learner turns.

## 9. Transcript-level tutor-diagnostic leakage audit

The authoritative persisted transcript schema contains only `turn_number`,
`role`, and `content`. Repository inspection found no frozen structured tag or
reliable deterministic rule identifying explicit tutor learner-state diagnoses.
Such statements are semantic, may be phrased variably in Italian, and cannot be
identified reliably through a narrow lexical rule without false precision.

Therefore v1.0.7 does not implement a transcript-level semantic leakage
classifier. Its prospective audit status is
`not_implemented_no_reliable_deterministic_rule`. No session is excluded,
redacted, rescored, or prompt-tuned on this basis. Mandatory learner-turn
attribution in §8 is the implemented auditable protection. This limitation is
recorded in provenance.

## 10. Dimensions and Pilot-0 category spaces

Each dimension is evaluated independently.

The general decision rule in §1.1 is normative for all four dimensions. When
observable learner behaviour supports one substantive category better than the
other, that category is selected even if uncertainty remains. Absolute
certainty is not required. `INSUFFICIENT_EVIDENCE` is used only when there is
essentially no meaningful evidence, no genuine opportunity to observe the
construct, or no reasonable evidential basis for preferring either category.

### 10.1 Knowledge

Knowledge is competence demonstrated in learner mathematical reasoning needed
for the task. Correctness and coherence are evidence; confidence, fluency,
verbosity, hesitation, politeness, and style are not.

- `LOW`: `LOW` is better supported than `HIGH` because substantial gaps or
  insufficient understanding are demonstrated.
- `HIGH`: `HIGH` is better supported than `LOW` because substantially correct
  and coherent understanding is demonstrated.
- `INSUFFICIENT_EVIDENCE`: there is essentially no meaningful learner evidence
  or no reasonable evidential basis for preferring `LOW` or `HIGH`.

### 10.2 Misconception

Misconception is a stable incorrect explanatory or procedural model. An
isolated wrong answer, slip, arithmetic error, or accidental inconsistency is
not sufficient.

- `PRESENT`: after meaningful misconception-relevant reasoning opportunity,
  `PRESENT` is better supported than `ABSENT` because learner evidence supports
  a coherent incorrect rule being applied or reapplied.
- `ABSENT`: after the conversation provided a meaningful opportunity to observe
  learner reasoning relevant to the study's applicable misconception space;
  the cited learner turns contain reasoning sufficient to assess whether a
  stable incorrect explanatory or procedural model is manifested; `ABSENT` is
  better supported than `PRESENT`; and across that relevant learner evidence no
  stable incorrect model is manifested.
  The cited turns establish evaluation opportunity and observable reasoning,
  not isolated logical proof that a misconception does not exist. Certainty is
  not required.
- `INSUFFICIENT_EVIDENCE`: there is no meaningful opportunity to evaluate
  misconception-relevant reasoning, essentially no meaningful evidence, or no
  reasonable evidential basis for preferring `PRESENT` or `ABSENT`.

`ABSENT` is never inferred merely because no misconception was noticed. The
extractor remains blind to assigned Ground Truth and is not told which assigned
misconception to test.

When `PRESENT`, `misconception_type` is one exact catalog code when uniquely
recoverable, otherwise `null`. For `ABSENT` or `INSUFFICIENT_EVIDENCE`, it is
`null`.

### 10.3 Metacognition

Metacognition is observable monitoring and regulation of the learner's own
reasoning, including localized uncertainty, error detection, self-correction,
targeted clarification, or verification. It is not inferred from style,
confidence, general intelligence, or another dimension.

- `LOW`: after cited learner evidence establishes a meaningful opportunity for
  monitoring or regulation, `LOW` is better supported than `HIGH` because
  observed learner behaviour during that opportunity supports little or no
  relevant monitoring or regulation.
  Opportunity may arise around error, uncertainty, inspection or verification,
  reconsideration of a procedure, or detection/correction of an inconsistency;
  these are illustrative rather than a required checklist. The cited turns are
  the observational basis, not isolated proof of an absence.
- `HIGH`: after a meaningful opportunity, `HIGH` is better supported than
  `LOW` because relevant monitoring or regulation is demonstrated.
- `INSUFFICIENT_EVIDENCE`: the interaction lacks a meaningful opportunity,
  essentially no meaningful learner evidence exists, or there is no reasonable
  evidential basis for preferring `LOW` or `HIGH`.

`LOW` is never inferred merely from an absence of noticed self-correction,
verification, uncertainty, or clarification.

### 10.4 Transfer

Transfer is successful application of a relevant principle or strategy in a
distinct but structurally related context.

- `HIGH`: a genuine transfer opportunity exists and `HIGH` is better supported
  than `LOW` because successful transfer is demonstrated.
- `LOW`: a genuine transfer opportunity exists and `LOW` is better supported
  than `HIGH` because generalization is attempted or required, but the
  principle is not applied successfully or remains context-bound.
- `INSUFFICIENT_EVIDENCE`: no genuine transfer opportunity exists, essentially
  no meaningful learner evidence exists, or there is no reasonable evidential
  basis for preferring `LOW` or `HIGH`.

Absence of transfer behaviour alone is not `LOW`. No genuine transfer
opportunity remains a legitimate `INSUFFICIENT_EVIDENCE` case. Once a genuine
opportunity exists, imperfect performance or residual uncertainty does not
justify abstention when one substantive category is better supported.

## 11. Structured output and strict parsing

The only valid logical output is:

```json
{
  "knowledge": {
    "value": "LOW|HIGH|INSUFFICIENT_EVIDENCE",
    "evidence_turns": [2, 4]
  },
  "misconception": {
    "value": "ABSENT|PRESENT|INSUFFICIENT_EVIDENCE",
    "evidence_turns": [4],
    "misconception_type": "adds_numerators_and_denominators|larger_denominator_larger|null"
  },
  "metacognition": {
    "value": "LOW|HIGH|INSUFFICIENT_EVIDENCE",
    "evidence_turns": [6]
  },
  "transfer": {
    "value": "LOW|HIGH|INSUFFICIENT_EVIDENCE",
    "evidence_turns": []
  }
}
```

The top level has exactly four dimension keys. Knowledge, Metacognition, and
Transfer objects have exactly `value` and `evidence_turns`; Misconception also
has exactly `misconception_type`. Parsing and evidence validation are exact and
case-sensitive. No extra field, probability, confidence, rationale, multiple
label, `MEDIUM`, `NOT_RECOVERABLE`, or `TECHNICAL_FAILURE` is accepted.

Misconception `evidence_turns` support the primary PRESENT/ABSENT classification
and, when applicable, the subtype classification. No separate subtype evidence
field is added.

The scoring mapping is exactly:

- `LOW` → `low`;
- `HIGH` → `high`;
- `ABSENT` → `absent`;
- `PRESENT` → `present`.

Misconception catalog codes retain exact lowercase form.
`INSUFFICIENT_EVIDENCE` is a successfully extracted scientific result meaning
that discriminating learner evidence or meaningful observation opportunity was
absent, leaving no reasonable basis to prefer either substantive category. It
is not a low-confidence substitute, an API/parser failure, or an incorrect
categorical prediction.

## 12. Provider/model-role independence

The fixed external extractor is Google `gemini-3.1-pro-preview`, a preview model. The authoritative
general analysis specification records:

- completed Proxima Reference condition: Anthropic/Claude-backed tutor role;
- planned Claude Vanilla/Generic Tutor: Anthropic/Claude;
- planned ChatGPT Vanilla/Generic Tutor: OpenAI;
- planned Mistral comparator: Mistral.

Google is therefore a different provider from every completed or currently
planned tutor-condition provider. The defensible statement is:

> DAS_extractor has provider/model-role independence: there is no same-provider
> overlap between the Google external extractor and any completed or currently
> planned tutor condition.

Comparator model identities remain planned until their own pre-execution
freezes. No claim of complete lineage independence is made because training
data, distillation lineage, and proprietary internal dependencies cannot be
fully verified.

## 13. Fixed instrument and cross-condition invariance

The fixed instrument is:

- official SDK `google-genai==2.20.0`;
- Gemini Developer API `v1beta`;
- explicit process-environment credential `GEMINI_API_KEY`;
- model exactly `gemini-3.1-pro-preview` (preview; no alias);
- text only; no tools, search, grounding, AFC, function calling, or fallback;
- candidate count 1;
- temperature exactly 1.0;
- seed 20260827;
- no explicit `thinking_level`, `thinking_budget`, or thinking configuration;
- thinking configuration: unset / model default;
- documented model-default thinking for `gemini-3.1-pro-preview`: high/dynamic;
- maximum output tokens 32768;
- response MIME type `application/json`;
- exact JSON schema in §11;
- per-attempt SDK timeout 120,000 milliseconds;
- SDK-internal HTTP attempts 1; outer retry/fail-fast policy in §14.

Temperature 1.0 is intentionally frozen following Google's Gemini 3 guidance,
which recommends the default temperature and warns that lower values can
degrade reasoning behaviour. The fixed seed does not make model output
perfectly deterministic at temperature 1.0. The instrument is fixed and seeded;
parsing, preprocessing, scoring, serialization, and selection remain
deterministic where separately specified.

The exact prompt is
`docs/pilot0/analysis/DAS_EXTRACTOR_PROMPT_v1_0_7.txt`. Its external SHA-256 is
bound by implementation and execution provenance.

Across Proxima, ChatGPT Vanilla, Claude Vanilla, Mistral, and every later tutor
condition evaluated under v1.0.7, all of the following remain identical:

- extractor provider/model ID;
- exact prompt and operational definitions;
- allowed preregistered study category space and `INSUFFICIENT_EVIDENCE` rule;
- structured-output schema and learner-evidence attribution rule;
- study misconception catalog;
- generation/API configuration;
- parser and scoring rules;
- technical-failure classification and retry policy;
- uncertainty procedure and provenance requirements; and
- canonical transcript representation.

No condition-specific prompt tuning, examples, model change, schema change, or
tutor/provider/condition metadata is permitted. The transcript is the only
condition-varying scientific input.

### 13.1 Comparison-family lifecycle

A `comparison family` is the explicitly defined set of tutor conditions
intended to be compared under one fixed DAS_extractor instrument. The currently
planned Pilot-0 comparison family comprises:

- Proxima — source condition completed; v1.0.7 DAS extraction pending;
- ChatGPT Vanilla — planned, not executed;
- Claude Vanilla — planned, not executed;
- Mistral — planned, not executed.

No condition has produced a DAS scientific result. Versions v1.0.0 through
v1.0.6 produced no full scientific extraction, so there is nothing to
re-extract. Version 1.0.7 is the common instrument for all subsequent DAS extraction in
this OPEN family.

A family is `OPEN` while its planned scientific comparison is not complete and
frozen. While OPEN, every included condition uses the same DAS_extractor
version: model, prompt, schema, configuration, scoring, retry, parser, study
category space, attribution, uncertainty, and canonical transcript
representation remain fixed. No condition-specific instrument change is
permitted.

If the frozen extractor model becomes unavailable before every required
condition in an OPEN family is complete, no substitute may be used only for
remaining conditions and mixed-instrument outputs may not be treated as
equivalent. A new governed DAS_extractor version must be frozen, and every
condition in that OPEN family must be executed or re-extracted under that same
new instrument.

A family becomes `CLOSED` only when all intended conditions have been executed
under one frozen instrument, the comparison results have been frozen as
complete, and the family is formally closed for reporting/publication. Later
model unavailability, a newer instrument version, or investigation of another
condition does not invalidate a CLOSED comparison. Its exact historical
instrument remains in provenance and it is not automatically re-run.

A later condition added after closure belongs to a new comparison family for
any comparison involving that condition and earlier conditions. The new family
must use one common frozen instrument for all included conditions. It may reuse
the original instrument if still reproducibly available; otherwise a new
version is frozen and every included condition is extracted under it. The
closed historical family remains unchanged.

The normative unavailability principle is:

> Extractor-model unavailability is an instrument-version event, not a
> condition-specific exception.

No fallback model/provider is silently substituted. A new extractor model
requires a governed specification identity, exact new model identity,
prompt/model provenance as applicable, an explicit relationship to the prior
instrument, and re-extraction of every condition in the OPEN family.

## 14. Technical failure and retry

`TECHNICAL_FAILURE` is runtime-only and is never an extractor category. It
covers transport/API/provider failure or invalid structured
output/schema/evidence-turn validation.

Permanent provider/configuration failures fail fast after one attempt: no retry
sleep, repeated request, session-level scientific result, or extractor
category is produced. HTTP 400, 401, 403, and 404 use the safe deterministic
failure classes `gemini_invalid_request_configuration`,
`gemini_authentication_failure`, `gemini_access_permission_failure`, and
`gemini_model_or_endpoint_unavailable`. Other non-transient 4xx responses use
`gemini_provider_permanent_failure`. A permanent instrument-level failure
terminates the run promptly.

Transient failures retain at most three identical total attempts:

1. execute attempt 1;
2. after failure, wait exactly 120 seconds and execute attempt 2;
3. after failure, wait exactly 120 seconds and execute attempt 3;
4. after attempt 3 fails, record `TECHNICAL_FAILURE` without another wait.

Timeout/transient transport failures, HTTP 408, HTTP 429, provider HTTP 499
request-closure responses, and HTTP 5xx are
retriable. Provider HTTP transients use
`gemini_provider_transient_failure`. Invalid structured
output/schema/evidence validation retains the existing retry policy.
When provider `finish_reason=MAX_TOKENS` accompanies incomplete or otherwise
invalid structured output, the attempt uses the stable retriable class
`gemini_max_tokens_incomplete_output`. Invalid structured output with
`finish_reason=STOP` or no available finish reason remains
`gemini_invalid_structured_output`; malformed JSON alone never establishes
token-ceiling exhaustion. Preflight still makes exactly one attempt with no
retry sleep, while integration-smoke, smoke, and full execution retain the
same fixed outer retry policy.

All retries use identical model, rendered prompt, transcript, schema,
generation/API configuration, and seed. No prompt repair, model/provider
switch, or fallback occurs. Each attempt records ordinal, status, safe failure
class, response identity when available, and raw response when returned.
Secrets, authorization data, and sensitive exception content are not
serialized.

Before each outer retry sleep, the runtime emits one concise stderr message
containing only attempt ordinal/limit, safe failure class, safe HTTP status when
available, and the fixed retry delay. A permanent fail-fast failure emits the
same safe fields and explicitly records that no retry will occur. The final
failed transient attempt may emit a safe no-retry/attempt-limit message but has
no sleep. Stderr never includes API keys, authorization data, full prompts,
transcripts, Ground Truth, learner-card metadata, raw provider response bodies,
or sensitive exception payloads. This observability changes neither scientific
result serialization nor retry/scoring semantics.

## 15. Scoring

For each dimension report:

- `scientifically_eligible_n`;
- `successfully_extracted_n`;
- `technical_failure_n`;
- `correct_n`;
- `incorrect_n`;
- `insufficient_evidence_n`.

Technical failures are excluded from the scientific denominator and remain
prominently reported. A publication run is incomplete while unresolved
technical failures remain.

`Exact Ground-Truth Recovery = correct_n / successfully_extracted_n`

`Evidence Sufficiency Rate = (correct_n + incorrect_n) /
successfully_extracted_n`

`INSUFFICIENT_EVIDENCE` remains in both denominators, contributes zero to both
metrics, and is not counted as an incorrect category prediction. Evidence-turn
metadata does not alter scoring. The two metrics are reported separately for
Knowledge, Misconception, Metacognition, and Transfer. No composite DAS exists.

Primary Misconception correctness compares only
`misconception.value` with Ground Truth `misconception`. A wrong or null
`misconception_type` never alters primary PRESENT/ABSENT correctness.

### 15.1 Secondary conditional misconception subtype description

`misconception_type` is not a fifth DAS dimension, primary endpoint, or part
of primary Misconception correctness. It is evaluated only in the fixed
conditional population:

`Ground Truth misconception = present AND extractor misconception.value = PRESENT`.

A session with Ground Truth PRESENT but extractor ABSENT or
`INSUFFICIENT_EVIDENCE` is already represented in primary Misconception DAS
and is not counted again as a subtype failure. Ground Truth ABSENT sessions are
also excluded.

Within the exact conditional denominator report:

- `subtype_evaluable_n`: every session in the conditional population;
- `subtype_correct_n`: non-null canonical extracted type exactly matches
  Ground Truth type;
- `subtype_incorrect_n`: non-null canonical extracted type differs from
  Ground Truth type;
- `subtype_unresolved_n`: primary PRESENT is correct but extracted type is
  `null` because the canonical subtype was not uniquely recoverable.

`Subtype Exact Recovery = subtype_correct_n / subtype_evaluable_n`.

`Subtype Identifiability Rate = (subtype_correct_n + subtype_incorrect_n) /
subtype_evaluable_n`.

A null subtype remains in both denominators and contributes zero. These are
secondary conditional descriptive measures only. They are not included in a
composite or promoted to a primary cross-condition endpoint. No subtype
bootstrap or other uncertainty method is added in v1.0.7. Any later
inferential/comparative promotion requires a prospective specification before
execution.

## 16. Profile-cluster Bayesian-bootstrap uncertainty

The unweighted §15 ratios are point estimates. Uncertainty uses exactly:

- 10,000 replicates;
- seed `20260827`;
- `numpy.random.Generator(numpy.random.PCG64)`;
- one `Dirichlet(1,…,1)` draw over scientifically eligible
  `stable_profile_ref` clusters per replicate;
- the same profile weight for every repeated session of that profile;
- separate weighted estimates for each dimension and each §15 metric;
- 2.5th and 97.5th percentiles with NumPy `method="linear"`;
- label `95% profile-cluster Bayesian-bootstrap uncertainty interval`.

For dimension `d`, replicate `r`, session indicator `v_sd`, and profile weight
`w_profile(s),r`:

`theta_d,r = Σ_s w_profile(s),r v_sd / Σ_s w_profile(s),r`,

with sums over scientifically eligible, successfully extracted sessions. For
exact recovery, `v=1` only for correct. For evidence sufficiency, `v=1` for
correct or incorrect. Zero/non-finite denominators or estimates create a
non-estimable replicate with deterministic reason; weights are never redrawn or
replaced. Requested, estimable, non-estimable, and failure counts are recorded
per dimension/metric. No A1 distance, WLS, or A1 estimand is reused.

## 17. Artifacts, serialization, and provenance

The initial full-run location is:

`data/pilot0/derived/SLEF_PILOT0_REFERENCE_RUN_3/track-b/DAS_EXTRACTOR_SPEC_v1_0_7/`

`track-b` follows the governing specification's diagnostic-extractor track.
Existing output directories are never overwritten.

The minimal artifact set is:

1. `session_extractions.jsonl` — identity, runtime status, attempts, raw/parsed
   response, validated learner evidence turns, post-call Ground Truth join, and
   per-dimension comparison;
2. `dimension_summary.json` — primary counts, point estimates and bootstrap intervals, plus secondary conditional misconception-subtype counts and rates;
3. `provenance_manifest.json` — instrument, input, code, runtime, retry,
   population, leakage-audit limitation, and output provenance;
4. `SHA256SUMS.txt` — SHA-256 for the other three files.

JSON is UTF-8/LF, sorted keys, compact separators, `allow_nan=false`, and one
terminal LF. JSONL has one canonical object per non-empty line and one terminal
LF. Undefined values use `null` plus a machine-readable reason. Non-finite JSON
values are forbidden.

Provenance records at minimum:

- this specification identity/status/hash and v1.0.6 supersession, including
  the historical malformed/incomplete pre-scientific smoke, the 512-to-2048
  output-token amendment, the v1.0.5 forced-choice decision-rule amendment,
  the v1.0.5 `MAX_TOKENS` preflight evidence, the 2048-to-32768 technical
  ceiling amendment, the GT-blind v1.0.6 repeatability evidence, the v1.0.7
  Misconception clarification, and no full scientific result under
  v1.0.0–v1.0.6;
- governing specification identity/hash and precedence;
- exact prompt identity/hash;
- source run and every consumed path/hash;
- analysis code commit/worktree state;
- SDK, API, preview-model status, temperature, seed, unset/model-default thinking, generation, and retry/fail-fast configuration;
- execution mode/date, identities, population, and exclusions;
- attribution validation version and leakage-audit status/limitation;
- bootstrap method, seed, replicate/failure counts, and NumPy version;
- payload hashes, attempt status, response identities; and
- deterministic serialization/sort rules and output hashes.

The API key is never logged, serialized, hashed into artifacts, or represented
in object reprs.

## 18. Verification requirements

Offline tests must cover:

- all allowed category objects and exact schema;
- rejection of `MEDIUM`, unknown values, extra/missing fields, invalid
  misconception-type combinations, and free-form rationale;
- every evidence reference resolving to an actual transcript turn;
- learner-only evidence references and rejection of tutor turns;
- non-empty evidence for category choices and empty evidence for
  `INSUFFICIENT_EVIDENCE`;
- forced-choice wording, exceptional-abstention semantics, conceptual 60/40
  and 55/45 illustrations, and absence of probability/confidence outputs;
- Misconception persistence/coherence semantics, isolated-error exclusion,
  abandoned-initial-rule handling, later-correction handling, and absence of a
  fixed turn-count threshold;
- normalized operator rendering from validated parsed JSON only, with no
  Ground Truth, probability, confidence, SDK metadata, or thought signature;
- condition/provider, Ground Truth, identity, and nuisance metadata absent from
  the request payload;
- canonical role normalization preserving text/order;
- evidence metadata leaving scoring unchanged;
- primary Misconception correctness being independent of subtype;
- the exact conditional subtype population, counts, and descriptive rates;
- separation of technical failure and scientific states;
- permanent HTTP 400/401/403/404 fail-fast behaviour with no sleep or repeat;
- transient transport, HTTP 408/429/499/5xx three-attempt/two-wait behaviour
  with identical requests;
- safe stderr observability before retry waits and at permanent fail-fast,
  without prompt, transcript, Ground Truth, raw response, or secret leakage;
- exact `MAX_TOKENS` causal classification only when provider finish metadata
  accompanies invalid structured output, with generic handling for `STOP` or
  unavailable finish reason;
- full provider response text visible in debug-console while opaque thought
  signatures are summarized as present/absent and retained only in the durable
  raw debug record;
- profile identity and deterministic cluster bootstrap;
- source hashes/identities, canonical serialization, immutable output, and
  provenance.

Tests use synthetic fixtures and fake clients only. They do not read credentials
or call a provider.

## 19. Smoke and scientific-execution gates

Before any full scientific run, validation proceeds in this fixed order:

1. offline unit tests for repository-owned responsibilities;
2. an opt-in live provider contract test using a harmless synthetic transcript,
   exactly one call, no retry, no Ground Truth, and no scientific scoring;
3. a one-session real preflight using the first eligible bytewise canonical
   session (or one exact `--session-ref`), exactly one call, no retry, no
   Ground-Truth join, and no scientific scoring;
4. a six-session heterogeneous integration smoke using shortest/longest frozen
   rendered prompts for Core, ChannelLayer, and NumericalProcessing, selected
   before provider calls and using the normal retry policy; and
5. the separately authorized 220-session scientific run.

Debug mode durably fsyncs the complete blind request event before provider
invocation and the SDK-exposed response event before structured parsing. Raw
debug logs remain outside Track-B scientific artifacts and checksums. After a
valid parse, a normalized human-facing block may display only the four inferred
categories, misconception subtype, and learner evidence turns. Opaque
`thought_signature` values are provider metadata, not chain-of-thought text or
classification output, and are excluded from normalized rendering and parsing.

The complete operational contract is
`DAS_EXTRACTOR_TESTING_DEBUG_AND_PREFLIGHT_v1_0_0.md`. Provider contract,
preflight, and integration-smoke labels are operational observations only: they
are not compared with Ground Truth, scored as DAS, or used to tune scientific
semantics. A structural incompatibility requires a governed amendment; observed
classification content or abstention frequency cannot justify automatic
instrument change.

## 20. Freeze and amendment

This document and its v1.0.7 prompt are frozen and owner-approved before any
successful scientific extraction. Implementation may be tested offline against them. Live
smoke execution requires separate authorization. Full scientific execution
requires a verified smoke test, verified implementation, exact specification
and prompt hashes, and an empty immutable output target.

Any change to construct, categories, definitions, prompt, model,
normalization/blindness, attribution, schema, configuration, retry, parsing,
scoring, uncertainty, population, or artifact semantics creates a governed
amendment or new version. Frozen raw evidence, A1 outputs, and existing
instrument versions are never modified.
