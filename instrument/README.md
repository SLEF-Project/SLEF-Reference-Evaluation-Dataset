# SLEF extractor prompt

Version: 1.0.0 · Date: 2026-09-30
Changelog: 1.0.0 - first public release of the extractor prompt text used in the SLEF reference experiment.

`DAS_EXTRACTOR_PROMPT_v1_0_7.txt` is the literal text of the prompt given to the transcript extractor
(DAS_extractor v1.0.7) in all five conditions of the SLEF reference experiment. It is released unchanged,
exactly as used.

## Integrity

The SHA-256 of the file is

```
2553a90d99053da2ffbbc91893935b54b1ca0b06e397b0e2ea98583e301cc6e9
```

the same value recorded as `prompt_sha256` in `conditions/*/derived/DAS/scientific-run/scientific_run_manifest.json`
for every condition. To check it:

```
shasum -a 256 DAS_EXTRACTOR_PROMPT_v1_0_7.txt      # macOS
sha256sum DAS_EXTRACTOR_PROMPT_v1_0_7.txt          # Linux
```

## How it was used

Model `gemini-3.1-pro-preview`, temperature 1.0, seed 20260827, output limit 32,768 tokens, under extractor
specification v1.0.7. The extractor received the chronological learner and tutor text of each session, without the
assigned labels, and returned one label per dimension or INSUFFICIENT_EVIDENCE.

The prompt text documents the instrument. The code that assembled the extractor inputs and called the model is not
included, so a re-implementation should expect label-level differences from the released classifications, since the
extractor is a preview model run at temperature 1.0.

## License

Released under CC BY 4.0, the same license as the dataset (see `LICENSE` in the repository root).
