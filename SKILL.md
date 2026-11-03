---
name: genpark-personal-agent-somatosensory-cortical-silent-period-tms-skill
version: 1.0.0
description: Calculates Transcranial Magnetic Stimulation (TMS) Cortical Silent Period Duration (ms), MEP-Normalized Ratio, and evaluates motor cortex GABAB intracortical inhibition.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - neurophysiology
  - tms
  - cortical-silent-period
  - gabab
  - zero-dependency
---

# Cortical Silent Period (CSP) TMS Skill

## Mathematical Formulation

Single-pulse suprathreshold TMS over primary motor cortex (M1):

$$\text{CSP Duration} = t_{\text{EMG resumption}} - t_{\text{MEP onset}} \quad (\text{ms})$$

MEP-Normalized Silent Period ratio:

$$\text{Ratio} = \frac{\text{CSP Duration (ms)}}{\text{MEP Peak-to-Peak Amplitude (mV)}}$$

Intracortical inhibitory mechanisms:
- First $50\text{ ms}$: Spinal motoneuron refractory period and Renshaw recurrent inhibition.
- Beyond $50\text{ ms}$: Intracortical inhibition mediated by inhibitory interneurons via metabotropic $\text{GABA}_B$ receptors.

## Clinical Neurophysiology Stratification
- **Normal Intracortical Inhibition**: $\text{CSP} \in [120, 220]\text{ ms}$ at $120\%$ resting motor threshold.
- **Cortical Disinhibition / Hyperexcitability**: $\text{CSP} < 110\text{ ms}$ (hallmark of focal task-specific dystonia, myoclonus, cortical epilepsy, ALS).
- **Excessive Intracortical Inhibition**: $\text{CSP} > 240\text{ ms}$ (seen in Parkinsonian akinesia, chronic neuroleptic exposure, high-dose baclofen).
