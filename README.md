# SLEF Reference Evaluation Dataset v1.1.0

Version: 1.1.0
Date: 2026-09-30
Changelog: v1.1.0 adds the released DAS extractor prompt, reproducibility software, expected analysis outputs, and release metadata. The scientific corpus and scientific values are unchanged from v1.0.0.

Reference evaluation dataset for **SLEF (Synthetic Learner Evaluation Framework)** — a controlled-Ground-Truth framework for evaluating learner-state inference under synthetic learner conditions.

This release contains the scientific evidence produced by the SLEF Reference Evaluation across five tutor conditions: the synthetic-learner dialogue corpora, assigned hidden Ground Truth, generator-native behavioral characterization, and transcript-level learner-state recoverability analysis.

Version 1.1.0 is an additive reproducibility release. It preserves the v1.0.0 scientific corpus and scientific values unchanged while adding the exact DAS extractor prompt used in the reference experiment, offline reproducibility software, frozen expected analysis outputs, and corresponding release metadata.

## What this is — and is not

This dataset accompanies the first SLEF publication and contains the empirical record supporting its Reference Evaluation.

It includes two complementary analysis tracks:

- **Track A1 — Generator-native manifestation characterization:** characterizes which predefined behavioral manifestations were instantiated by the synthetic learner generator during the evaluated interactions.
- **Track B / DAS — Dialogue-based learner-state recoverability:** measures to what extent the assigned hidden learner state can be reconstructed from the realized dialogue by a fixed, independent, blinded extractor.

The canonical Ground-Truth dimensions are:

- Knowledge;
- Misconception;
- Metacognition;
- Transfer.

These analyses address different parts of the evaluation chain. Track A1 concerns behavior instantiated by the generator; DAS concerns learner-state information recoverable from the resulting dialogue.

**This dataset does not establish:**

- pedagogical effectiveness or learning gain;
- general tutor superiority;
- psychological or clinical validity of the synthetic learners;
- validity for real students.

All learners in this release are synthetic and non-human.

## At a glance

| | |
|---|---|
| Tutor conditions | 5 (Proxima, Claude Vanilla, Claude Mainstream, OpenAI, Mistral) |
| Synthetic learner profiles per condition | 44 (32 Core, 8 ChannelLayer, 4 NumericalProcessing) |
| Sessions per condition | 220 (5 per profile) |
| Total evaluated sessions | 1,100 |
| Domain | School mathematics (fractions), Italian middle-school level |
| Original language | Italian, not translated |
| Analysis tracks included | Track A1 and Track B / DAS |
| Ground-Truth dimensions | Knowledge, Misconception, Metacognition, Transfer |
| Reproducibility materials | Exact DAS extractor prompt, offline analysis code, tests, and frozen expected outputs |

## Relationship to the paper

This dataset accompanies and is cited by:

> Accompanying paper: Can Assigned Learner States Be Recovered from Synthetic Tutoring Dialogues? A Factorial Study with SLEF — forthcoming preprint.
> Marco Iannacone, 2026  
> Persistent identifier: not yet assigned.

The paper provides the full SLEF framework definition, experimental rationale, methodology, statistical treatment, interpretation, and validity discussion.

This repository is the corresponding scientific data release: it contains the released empirical evidence, frozen analysis artifacts, provenance, specifications, and integrity controls supporting the reported Reference Evaluation.

## Resources

L×M×C preprint: https://doi.org/10.35542/osf.io/hvx37_v2  
This release (v1.1.0): https://doi.org/10.5281/zenodo.23068043
All versions of this dataset: https://doi.org/10.5281/zenodo.22930175

## Historical `PILOT0` naming

Some internal execution identifiers preserved in this dataset retain the historical name `PILOT0`, for example:

`SLEF_PILOT0_REFERENCE_RUN_3`

The public dataset release is versioned independently as **SLEF Reference Evaluation Dataset v1.1.0**.

Historical `PILOT0` identifiers are retained only for provenance continuity and auditability back to the original scientific executions.

The public-facing condition names used throughout this README and the paper are:

- Proxima;
- Claude Vanilla;
- Claude Mainstream;
- OpenAI;
- Mistral.

## The five conditions

| Condition | Configuration | Role in the study |
|---|---|---|
| **Proxima** | Anthropic-backed Proxima maieutic tutoring system | Primary system under evaluation |
| **Claude Vanilla** | Claude Vanilla: Anthropic claude-sonnet-4-5, no reasoning effort configured, without Proxima ZSP's maieutic tutoring apparatus added on top. In the study design, this condition serves as a same-model, apparatus-contrast condition, as described in the accompanying paper's methodology. Because Proxima ZSP's model identifier is intentionally not asserted in this public release, the same-model relationship is a documented study-design property rather than one that can be independently established from model-identity fields in this dataset alone. | Same-model system-removal contrast designed to reduce model-generation confounding |
| **Claude Mainstream** | Anthropic, newer model generation with reasoning effort enabled | Additional comparator; differs from Proxima in both model generation and reasoning configuration and is therefore not a clean system-removal contrast |
| **OpenAI** | OpenAI general-purpose tutor condition | Cross-system benchmark comparator |
| **Mistral** | Mistral general-purpose tutor condition | Cross-system benchmark comparator |

### On Proxima ZSP's model field

Proxima ZSP's condition_manifest.json intentionally leaves the model field unasserted (see its identity_note). This is intentional in this public release, not an omission: Proxima ZSP is evaluated as a complete system, not as a bare model identity, unlike the comparator conditions. The model used at acquisition time is documented in the accompanying paper's methodology for readers who need that specific implementation detail.

Provider/model identity information is recorded in the corresponding condition_manifest.json files, subject to each condition's public-release disclosure policy. Full runtime configuration detail, including the reasoning-effort setting where applicable, is recorded in each session's raw record under effective_scientific_parameters.

## Directory structure

```text
├── README.md
├── DATASET_MANIFEST.json
├── FILE_INVENTORY.tsv
├── SHA256SUMS.txt
├── DATA_DICTIONARY.md
├── CITATION.cff
├── LICENSE
├── instrument/
│   ├── README.md
│   └── DAS_EXTRACTOR_PROMPT_v1_0_7.txt
├── software/
│   ├── README.md
│   ├── slef_reference_analysis.py
│   ├── test_slef_reference_analysis.py
│   ├── requirements.txt
│   └── expected_outputs/
├── schemas/
└── conditions/
    ├── <condition_name>/
    │   ├── condition_manifest.json
    │   ├── raw/
    │   │   ├── conversations/
    │   │   └── evidence/
    │   └── derived/
    │       ├── A1/
    │       └── DAS/
    └── ...
```

## Raw conversation format

The raw conversation corpus intentionally preserves the native scientific source format of each condition.

- **Proxima:** one aggregate `transcripts.jsonl` file containing 220 records.
- **OpenAI:** 220 individual per-session JSON files.
- **Mistral:** 220 individual per-session JSON files.
- **Claude Mainstream:** 220 individual per-session JSON files.
- **Claude Vanilla:** 220 individual per-session JSON files.

This asymmetry is deliberate. The release preserves source-native scientific artifacts rather than normalizing them into a common serialization after the fact.

See `DATA_DICTIONARY.md` for the corresponding field and relationship definitions.

## Scientific contents

Each condition contains three principal classes of material.

### Raw conversations

The realized interactions between the synthetic learner and the evaluated tutor.

All five conditions use the same canonical 44-profile experimental design and five sessions per profile.

### Scientific evidence

Artifacts required to establish session identity, provenance, source relationships, and interpretation of the released scientific corpus.

### Derived analysis

#### Track A1

Track A1 characterizes generator-native behavioral manifestations instantiated during the synthetic learner executions.

It does **not** measure external observability, learner-state recovery, psychological realism, or pedagogical effectiveness.

#### Track B / DAS

DAS evaluates transcript-level recoverability of the assigned learner state along four Ground-Truth dimensions:

- Knowledge;
- Misconception;
- Metacognition;
- Transfer.

A fixed independent extractor is applied to the realized dialogue under a blinded extraction procedure.

DAS measures recoverability from dialogue under that fixed extraction instrument. It does not measure tutor private internal state, pedagogical effectiveness, learning gain, or general tutor quality.

## DAS instrument transparency

The released material documents the semantic DAS instrument specification, including:

- Ground-Truth dimensions;
- evidence requirements;
- output schema;
- insufficient-evidence handling;
- scoring procedure;
- extractor model and configuration identity;
- instrument and specification identities;
- prompt SHA-256.

The exact literal extractor prompt used for the released DAS results is included in this release as:

`instrument/DAS_EXTRACTOR_PROMPT_v1_0_7.txt`

The file is released unchanged. Its SHA-256 is:

`2553a90d99053da2ffbbc91893935b54b1ca0b06e397b0e2ea98583e301cc6e9`

This is the same `prompt_sha256` recorded in the DAS scientific-run manifest for every released condition.

## Reproducibility software

The `software/` directory provides an offline reproduction path for the analyses accompanying the reference experiment.

- `slef_reference_analysis.py` recomputes the released analysis tables and figures directly from the public dataset.
- `test_slef_reference_analysis.py` provides six consistency tests over the generated outputs.
- `expected_outputs/` contains the frozen expected analysis outputs.
- `requirements.txt` records the tested Python dependencies.
- `software/SHA256SUMS.txt` provides integrity hashes for the reproducibility package.

The analysis software performs no model calls and does not relabel or modify the released scientific source data. Usage and output mapping are documented in `software/README.md`.

## Language and domain

The scientific corpus — including synthetic learner utterances, tutor replies, and task content — is preserved in its original **Italian**.

The experimental domain is **school mathematics, specifically fractions**, targeted at Italian middle-school level.

No translation has been applied to the released scientific conversations.

A study conducted in another language would therefore constitute a related reproduction rather than an exact replication of these released linguistic conditions.

## Verification

`FILE_INVENTORY.tsv` provides the released file inventory, including path, artifact class, size, provenance reference, and SHA-256 information.

Every released file has a SHA-256 integrity record in the release controls **except, necessarily, `SHA256SUMS.txt` itself**. The finalized `FILE_INVENTORY.tsv` is included in `SHA256SUMS.txt`.

To verify the released files after download:

```bash
sha256sum -c SHA256SUMS.txt
```

Source provenance, including acquisition identities, relevant Git commits, specification versions, and hashes, is recorded in each condition's `condition_manifest.json` and in `DATASET_MANIFEST.json`.

## License

The dataset content and released DAS instrument are released under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

See `LICENSE` for the dataset license summary and a link to the official CC BY 4.0 legal code.

The analysis source code under `software/` is released separately under the **Apache License, Version 2.0**. See `software/LICENSE` and `software/NOTICE`.

## Naming and Attribution

This CC BY 4.0 license governs reuse of the dataset content. It does
not grant any right to use the name "SLEF" or "Synthetic Learner
Evaluation Framework" to describe, endorse, or certify a product,
service, or derivative work as officially affiliated with, produced
by, or approved by this project.

You are free to state factually that your work uses, is derived from,
or has been evaluated against the publicly released SLEF Reference
Evaluation Dataset, provided this is not phrased in a way that could
reasonably be mistaken for an official SLEF-branded offering or imply
endorsement by the project or its author.

For citation, see CITATION.cff.

## Citation

Citation metadata is provided in `CITATION.cff`.

When hosted on a platform supporting Citation File Format, this file can be used to generate standard citation formats for the dataset.

Publication-specific metadata such as the final repository URL, release date, and DOI should be taken from the released `CITATION.cff`.

### Release stability

Version 1.1.0 is an additive reproducibility release built on the immutable v1.0.0 scientific release. The released dialogue corpus, assigned Ground Truth, Track A1 artifacts, DAS scientific artifacts, DAS scores, and scientific values are unchanged from v1.0.0.

Version 1.1.0 adds the exact DAS extractor prompt, offline reproducibility software, frozen expected analysis outputs, and updated release metadata. Any future addition or correction affecting released scientific content will be published as a new, separately versioned release.

## Key limitations

- All learners are synthetic; no real students or human research participants are represented in the scientific corpus.
- Ground-Truth learner states are controlled experimental assignments and remain static within a session under the SLEF-Core design used for this release.
- Track A1 characterizes generator-native manifestations; it should not be interpreted as an external behavioral-observability measure.
- DAS measures learner-state recoverability from realized dialogue using a fixed independent extractor; it should not be interpreted as pedagogical effectiveness, learning gain, or access to a tutor's private internal learner model.
- Dialogue volume and turn-boundary termination rates differ markedly across the five conditions (e.g., mean valid learner turns per session range from approximately 2.0 in the lowest condition to approximately 7.7 in the highest; the share of sessions reaching the configured turn ceiling ranges from about 1% to about 38% across conditions — see the accompanying paper for exact per-condition figures). Because DAS measures recoverability from the dialogue actually produced, unequal evidence volume across conditions is a confound for cross-condition comparison of diagnostic recoverability. Differences in unconditioned DAS results across conditions therefore cannot, by themselves, be interpreted as differences in tutor diagnostic competence. A volume-conditioned analysis is planned as future work and is not included in this release.
- The released experiment is restricted to a single educational domain, language, learner-profile design, and task family.
- No clinical interpretation is supported. NumericalProcessing is a controlled experimental profile, not a diagnosis.
- No claim of general tutor superiority follows from these data.

## Questions

Project contact: slef@digitallydifferent.it
Author / maintainer: Marco Iannacone — ianna@pippo.com
