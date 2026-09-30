#!/usr/bin/env python3
"""Reproduce the analyses of the SLEF reference-experiment paper from the unmodified public dataset.

Version: 1.0.0
Date: 2026-09-30
Changelog: 1.0.0 - first public release; renamed from the working script used for the
paper, with no change to the computations.

Copyright 2026 Marco Iannacone. Licensed under the Apache License, Version 2.0
(see LICENSE and NOTICE in this folder).

No model calls, new labels, exclusions based on outcome, or source writes.
Dependencies: numpy; matplotlib for figures (disable with --no-figures).
All analyses newly introduced by this script are post hoc exploratory.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import json
import platform
import subprocess
from pathlib import Path
import numpy as np

CONDITIONS = ['Proxima', 'Claude Vanilla', 'OpenAI', 'Claude Mainstream', 'Mistral']
DIMENSIONS = ['knowledge', 'misconception', 'metacognition', 'transfer']
IE = 'INSUFFICIENT_EVIDENCE'
SEED = 20260927

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def dump_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False)+'\n', encoding='utf-8')

def write_csv(path, records):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(records[0]))
        w.writeheader(); w.writerows(records)

def pct(a, b):
    return 100*a/b if b else None

def verify_release(root):
    count = 0
    for line in (root/'SHA256SUMS.txt').read_text().splitlines():
        if not line.strip(): continue
        expected, name = line.split(maxsplit=1)
        path = root/name.lstrip('*')
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected: raise ValueError(f'Checksum mismatch: {name}')
        count += 1
    return count

def load_condition(root, name):
    base = root/'conditions'/name
    cards = read_json(base/'raw/evidence/design/learner_cards.snapshot.json')
    cards = {(c['profile_id'], c['instance_index']): c for c in cards}
    path = base/'derived/DAS/scoring/joined_session_scored.jsonl'
    if not path.exists(): path = base/'derived/DAS/scoring/session_comparisons.jsonl'
    rows = []
    for line in path.read_text().splitlines():
        r = json.loads(line)
        session = r.get('canonical_session_ref', r.get('session_ref'))
        card = cards[(r['stable_profile_ref'], r['session_position'])]
        compare = r.get('comparison', r.get('dimension_comparisons'))
        evidence = read_json(base/'raw/evidence/sessions'/f'{session}.json')
        out = dict(condition=name, session=session, profile=r['stable_profile_ref'],
                   cell=card['factorial_cell_id'], family=card['profile_category'],
                   style=card['style_variant_id'], position=r['session_position'],
                   task=r['task_variant_ref'], base_profile=card.get('base_profile_id'),
                   learner_turns=len(evidence['learner_turns_privileged']),
                   termination=evidence['termination_reason'])
        assert card['task_variant_ref'] == out['task']
        for d in DIMENSIONS:
            if compare:
                gt = compare[d]['ground_truth'].upper()
                pred = compare[d].get('extractor', compare[d].get('extracted'))
                outcome = compare[d].get('outcome', compare[d].get('result'))
            else:
                gt, pred = r['ground_truth'][d].upper(), r['extractor'][d]['value']
                outcome = r['outcomes'][d]
            assert gt == card['ground_truth'][d].upper()
            expected = 'insufficient_evidence' if pred == IE else ('correct' if pred == gt else 'incorrect')
            assert outcome == expected, (name, session, d)
            out[d+'_gt'], out[d+'_pred'] = gt, pred
        for turn in evidence['learner_turns_privileged']:
            assert turn['manifested_this_turn']['trace_type'] == 'learner_generator_self_report'
        rows.append(out)
    assert len(rows) == 220 and len({r['session'] for r in rows}) == 220
    assert len({r['profile'] for r in rows}) == 44
    assert collections.Counter(r['family'] for r in rows) == {'core':160, 'channel_variant':40, 'numerical_processing':20}
    for d in DIMENSIONS:
        assert sorted(collections.Counter(r[d+'_gt'] for r in rows).values()) == [110,110]
    return sorted(rows, key=lambda r:r['session'])

def outcome_summary(rows, d):
    n = len(rows)
    correct = sum(r[d+'_pred'] == r[d+'_gt'] for r in rows)
    ie = sum(r[d+'_pred'] == IE for r in rows)
    return dict(n=n, correct=correct, incorrect=n-correct-ie, ie=ie,
                recovery_pct=pct(correct,n), coverage_pct=pct(n-ie,n),
                conditional_agreement_pct=pct(correct,n-ie))

def standardized_accuracy(rows):
    # Knowledge-class-balanced exact recovery, with IE contributing zero.
    parts = [[r for r in rows if r['knowledge_gt']==k] for k in ['LOW','HIGH']]
    if any(not x for x in parts): return None
    return 50*sum(sum(r['knowledge_pred']==r['knowledge_gt'] for r in x)/len(x) for x in parts)

def analyse(root, out, reps, figures):
    out.mkdir(parents=True, exist_ok=True)
    checksum_count = verify_release(root)
    data = {c:load_condition(root,c) for c in CONDITIONS}
    # Verify exact shared profile/task/assignment identity across all conditions.
    reference = data[CONDITIONS[0]]
    for c in CONDITIONS[1:]:
        for a,b in zip(reference,data[c]):
            for k in ['session','profile','cell','family','style','position','task']+[d+'_gt' for d in DIMENSIONS]:
                assert a[k]==b[k], (c,k)
    allrows = [r for c in CONDITIONS for r in data[c]]
    write_csv(out/'normalized_sessions.csv', allrows)
    totals=[]; classrows=[]; execution=[]; core=[]; sensitivity=[]; channels=[]; transitions=[]; termination=[]
    for c, rows in data.items():
        execution.append(dict(condition=c, sessions=len(rows), learner_turns=sum(r['learner_turns'] for r in rows),
                              turn_capped=sum(r['termination']=='max_learner_turns_reached' for r in rows)))
        for d in DIMENSIONS:
            totals.append(dict(condition=c, dimension=d, **outcome_summary(rows,d)))
            for gt in sorted({r[d+'_gt'] for r in rows}):
                classrows.append(dict(condition=c,dimension=d,gt=gt,**outcome_summary([r for r in rows if r[d+'_gt']==gt],d)))
        cr = [r for r in rows if r['family']=='core']
        for m in ['LOW','HIGH']:
            subset = [r for r in cr if r['metacognition_gt']==m]
            for k in ['LOW','HIGH']:
                rr = [r for r in subset if r['knowledge_gt']==k]
                assert len(rr)==40
                core.append(dict(condition=c,metacognition_gt=m,knowledge_gt=k,n=len(rr),
                                 pred_low=sum(r['knowledge_pred']=='LOW' for r in rr),
                                 pred_high=sum(r['knowledge_pred']=='HIGH' for r in rr),
                                 ie=sum(r['knowledge_pred']==IE for r in rr),
                                 correct=sum(r['knowledge_pred']==k for r in rr)))
        for factor in ['style','misconception_gt','transfer_gt']:
            for level in sorted({r[factor] for r in cr}):
                lo=[r for r in cr if r[factor]==level and r['metacognition_gt']=='LOW']
                hi=[r for r in cr if r[factor]==level and r['metacognition_gt']=='HIGH']
                al,ah=standardized_accuracy(lo),standardized_accuracy(hi)
                sensitivity.append(dict(condition=c,analysis='subgroup',factor=factor,level=level,n_low=len(lo),n_high=len(hi),
                                        accuracy_m_low_pct=al,accuracy_m_high_pct=ah,difference_high_minus_low_pp=ah-al))
        for task in sorted({r['task'] for r in cr}):
            rr=[r for r in cr if r['task']!=task]
            lo=[r for r in rr if r['metacognition_gt']=='LOW'];hi=[r for r in rr if r['metacognition_gt']=='HIGH']
            al,ah=standardized_accuracy(lo),standardized_accuracy(hi)
            sensitivity.append(dict(condition=c,analysis='leave_one_task_out',factor='excluded_task',level=task,n_low=len(lo),n_high=len(hi),
                                    accuracy_m_low_pct=al,accuracy_m_high_pct=ah,difference_high_minus_low_pp=ah-al))
        lookup={(r['profile'],r['position']):r for r in rows}
        pairs=[]
        for b in rows:
            if b['family']!='channel_variant':continue
            a=lookup[(b['base_profile'],b['position'])]
            assert a['task']==b['task']
            assert all(a[d+'_gt']==b[d+'_gt'] for d in DIMENSIONS)
            pairs.append((a,b))
        assert len(pairs)==40
        for d in DIMENSIONS:
            cnt=collections.Counter()
            for a,b in pairs:
                g,pa,pb=a[d+'_gt'],a[d+'_pred'],b[d+'_pred']
                sa='IE' if pa==IE else ('correct' if pa==g else 'incorrect')
                sb='IE' if pb==IE else ('correct' if pb==g else 'incorrect')
                cnt[(sa,sb)]+=1
            channels.append(dict(condition=c,dimension=d,n_pairs=40,
                core_correct=sum(a[d+'_pred']==a[d+'_gt'] for a,b in pairs),
                channel_correct=sum(b[d+'_pred']==b[d+'_gt'] for a,b in pairs),
                label_disagreements=sum(a[d+'_pred']!=b[d+'_pred'] for a,b in pairs),
                both_judged_opposite=sum(a[d+'_pred']!=b[d+'_pred'] and IE not in (a[d+'_pred'],b[d+'_pred']) for a,b in pairs),
                correct_to_incorrect=cnt['correct','incorrect'],incorrect_to_correct=cnt['incorrect','correct'],
                abstention_transitions=sum(v for (a,b),v in cnt.items() if a!=b and 'IE' in (a,b))))
            for a in ['correct','incorrect','IE']:
                for b in ['correct','incorrect','IE']:
                    transitions.append(dict(condition=c,dimension=d,core_outcome=a,channel_outcome=b,count=cnt[a,b]))
        for mode in ['status_risolto','max_learner_turns_reached']:
            rr=[r for r in rows if r['termination']==mode and r['metacognition_gt']=='LOW']
            termination.append(dict(condition=c,termination=mode,**outcome_summary(rr,'metacognition')))
    # Bayesian profile-cell weighting sensitivity, preserving balanced K classes.
    # Cell is the cluster: both styles and all five sessions remain together.
    # The same Dirichlet draws are reused across conditions. Intervals quantify
    # sensitivity to empirical cell weights, NOT uncertainty about new tasks,
    # generators, assessors, populations, or causal effects.
    cells=sorted({r['cell'] for r in reference if r['family']=='core'})
    rng=np.random.default_rng(SEED); w=rng.dirichlet(np.ones(len(cells)),size=reps)
    boot=[]
    for c,rows in data.items():
        cr=[r for r in rows if r['family']=='core']; rates=[]; labels=[]
        for cell in cells:
            rr=[r for r in cr if r['cell']==cell]
            assert len(rr)==10
            assert len({(r['knowledge_gt'],r['metacognition_gt']) for r in rr})==1
            labels.append((rr[0]['knowledge_gt'],rr[0]['metacognition_gt']))
            rates.append(sum(r['knowledge_pred']==r['knowledge_gt'] for r in rr)/10)
        rates=np.array(rates); draws={}
        for m in ['LOW','HIGH']:
            pieces=[]
            for k in ['LOW','HIGH']:
                mask=np.array([x==(k,m) for x in labels]); assert mask.sum()==4
                pieces.append((w[:,mask]@rates[mask])/w[:,mask].sum(axis=1))
            draws[m]=50*(pieces[0]+pieces[1])
        for name,v in [('accuracy_m_low_pct',draws['LOW']),('accuracy_m_high_pct',draws['HIGH']),('difference_high_minus_low_pp',draws['HIGH']-draws['LOW'])]:
            boot.append(dict(condition=c,quantity=name,lower_025=float(np.quantile(v,.025)),upper_975=float(np.quantile(v,.975)),replicates=reps,seed=SEED))
    tables={'dimension_summary':totals,'class_conditional_summary':classrows,'execution_summary':execution,
            'core_knowledge_metacognition':core,'sensitivity_knowledge_metacognition':sensitivity,
            'paired_channel_summary':channels,'paired_channel_transitions':transitions,
            'termination_metacognition_low':termination,'cell_weighting_intervals':boot}
    for name,records in tables.items(): write_csv(out/(name+'.csv'),records)
    dump_json(out/'results.json',tables)
    try: commit=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    except (OSError,subprocess.CalledProcessError): commit=None
    manifest=dict(analysis_version='1.0.0',analysis_date='2026-09-27',analysis_status='post_hoc_exploratory',
                  dataset_git_commit=commit,dataset_doi_as_declared='10.5281/zenodo.22930176',
                  dataset_checksum_entries_verified=checksum_count,sessions=len(allrows),
                  learner_turns=sum(r['learner_turns'] for r in allrows),conditions=CONDITIONS,
                  seed=SEED,weighting_replicates=reps,python=platform.python_version(),numpy=np.__version__,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  no_new_model_calls=True,no_relabeling=True,no_source_modifications=True)
    dump_json(out/'analysis_manifest.json',manifest)
    if figures: make_figures(out,tables)
    print(json.dumps(manifest,indent=2))
    for c in CONDITIONS:
        rr=[r for r in sensitivity if r['condition']==c and r['analysis']=='leave_one_task_out']
        print(c,'leave-task-out HIGH accuracy',min(r['accuracy_m_high_pct'] for r in rr),max(r['accuracy_m_high_pct'] for r in rr),
              'difference range',min(r['difference_high_minus_low_pp'] for r in rr),max(r['difference_high_minus_low_pp'] for r in rr))
    return tables

def make_figures(out,tables):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,ax=plt.subplots(figsize=(8.2,3.8),layout='constrained')
    x=np.arange(5); ys={}
    for m in ['LOW','HIGH']:
        ys[m]=[sum(r['correct'] for r in tables['core_knowledge_metacognition'] if r['condition']==c and r['metacognition_gt']==m)/80*100 for c in CONDITIONS]
    for dx,m,color in [(-.18,'LOW','#31546f'),(.18,'HIGH','#ba6a35')]:
        bars=ax.bar(x+dx,ys[m],.34,label=f'Assigned Metacognition {m}',color=color)
        for b in bars:ax.text(b.get_x()+b.get_width()/2,b.get_height()+1,f'{b.get_height():.2f}',ha='center',fontsize=9)
    ax.axhline(50,color='#555555',linestyle='--',linewidth=1,label='Constant-class baseline')
    ax.set_ylim(0,100);ax.set_ylabel('Knowledge exact recovery (%)')
    ax.set_xticks(x,['Proxima','Claude\nVanilla','OpenAI','Claude\nMainstream','Mistral'])
    ax.legend(loc='upper center',ncol=2,frameon=False,fontsize=8)
    fig.savefig(out/'figure_1_core_recovery.png',dpi=240);fig.savefig(out/'figure_1_core_recovery.svg');plt.close(fig)
    fig,ax=plt.subplots(figsize=(8.2,3.4),layout='constrained')
    for name,color in [('Correct','#31546f'),('Incorrect','#ba6a35'),('Abstained','#c9ced4')]:
        vals=[];bottom=[]
        for c in CONDITIONS:
            r=next(r for r in tables['dimension_summary'] if r['condition']==c and r['dimension']=='metacognition')
            vals.append(r[{'Correct':'correct','Incorrect':'incorrect','Abstained':'ie'}[name]]/220*100)
            bottom.append(0 if name=='Correct' else r['correct']/220*100 if name=='Incorrect' else (r['correct']+r['incorrect'])/220*100)
        bars=ax.barh(np.arange(5),vals,left=bottom,label=name,color=color,height=.6)
        for b,v,base in zip(bars,vals,bottom):
            ax.text(base+v/2,b.get_y()+b.get_height()/2,f'{v:.1f}%',ha='center',va='center',fontsize=9,color='white' if name!='Abstained' else 'black')
    ax.set_yticks(np.arange(5),CONDITIONS);ax.invert_yaxis();ax.set_xlim(0,100)
    ax.set_xlabel('Share of all 220 sessions in each condition (%)');ax.legend(loc='lower center',bbox_to_anchor=(.5,1.0),ncol=3,frameon=False)
    fig.savefig(out/'figure_2_metacognition_outcomes.png',dpi=240);fig.savefig(out/'figure_2_metacognition_outcomes.svg');plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('dataset',type=Path);p.add_argument('--output',type=Path,default=Path('analysis_outputs'))
    p.add_argument('--replicates',type=int,default=10000);p.add_argument('--no-figures',action='store_true')
    args=p.parse_args();analyse(args.dataset.resolve(),args.output.resolve(),args.replicates,not args.no_figures)
