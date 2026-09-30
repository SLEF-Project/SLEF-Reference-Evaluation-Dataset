#!/usr/bin/env python3
"""Consistency tests independent of the analysis implementation.

Version: 1.0.0
Date: 2026-09-30
Changelog: 1.0.0 - first public release; the outputs folder can be set with the
SLEF_OUTPUTS environment variable (default: analysis_outputs next to this file).

Copyright 2026 Marco Iannacone. Licensed under the Apache License, Version 2.0
(see LICENSE and NOTICE in this folder).
"""
from pathlib import Path
import csv
import json
import os
import unittest

ROOT=Path(os.environ.get('SLEF_OUTPUTS', Path(__file__).resolve().parent/'analysis_outputs'))
RESULTS=json.loads((ROOT/'results.json').read_text())
with (ROOT/'normalized_sessions.csv').open() as stream:
    ROWS=list(csv.DictReader(stream))

class AnalysisTests(unittest.TestCase):
    def test_population(self):
        self.assertEqual(len(ROWS),1100)
        self.assertEqual(len({(r['condition'],r['session']) for r in ROWS}),1100)
        self.assertEqual(sum(int(r['learner_turns']) for r in ROWS),5644)

    def test_decomposition(self):
        for key in ['dimension_summary','class_conditional_summary','termination_metacognition_low']:
            for r in RESULTS[key]:
                self.assertEqual(r['correct']+r['incorrect']+r['ie'],r['n'])
                if r['n'] and r['coverage_pct']:
                    self.assertAlmostEqual(r['recovery_pct'],r['coverage_pct']*r['conditional_agreement_pct']/100)

    def test_exported_counts(self):
        for r in RESULTS['dimension_summary']:
            subset=[s for s in ROWS if s['condition']==r['condition']]
            d=r['dimension']
            correct=sum(s[d+'_gt']==s[d+'_pred'] for s in subset)
            abstained=sum(s[d+'_pred']=='INSUFFICIENT_EVIDENCE' for s in subset)
            self.assertEqual((correct,abstained),(r['correct'],r['ie']))

    def test_core_joint_counts(self):
        for r in RESULTS['core_knowledge_metacognition']:
            self.assertEqual(r['n'],40)
            self.assertEqual(r['pred_low']+r['pred_high']+r['ie'],40)
            self.assertEqual(r['ie'],0)
        for c in ['Claude Mainstream','Mistral']:
            subset=[s for s in ROWS if s['condition']==c and s['family']=='core' and s['metacognition_gt']=='HIGH']
            self.assertEqual(len(subset),80)
            self.assertEqual({s['knowledge_pred'] for s in subset},{'HIGH'})

    def test_pair_transitions(self):
        for r in RESULTS['paired_channel_summary']:
            trans=[t for t in RESULTS['paired_channel_transitions'] if t['condition']==r['condition'] and t['dimension']==r['dimension']]
            self.assertEqual(sum(t['count'] for t in trans),40)
            self.assertEqual(sum(t['count'] for t in trans if t['core_outcome']=='correct'),r['core_correct'])
            self.assertEqual(sum(t['count'] for t in trans if t['channel_outcome']=='correct'),r['channel_correct'])
            self.assertEqual(sum(t['count'] for t in trans if t['core_outcome']!=t['channel_outcome']),r['label_disagreements'])

    def test_sensitivity_reporting(self):
        for r in RESULTS['sensitivity_knowledge_metacognition']:
            self.assertLessEqual(r['difference_high_minus_low_pp'],1e-10)
        for c in {r['condition'] for r in ROWS}:
            tasks=[r for r in RESULTS['sensitivity_knowledge_metacognition'] if r['condition']==c and r['analysis']=='leave_one_task_out']
            self.assertEqual(len(tasks),30)
            self.assertTrue(all(r['difference_high_minus_low_pp']<0 for r in tasks))

if __name__=='__main__':unittest.main(verbosity=2)
