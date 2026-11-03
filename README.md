# Cortical Silent Period (CSP) TMS Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Transcranial Magnetic Stimulation (TMS) Cortical Silent Period Duration (ms) and MEP-Normalized Ratio to quantify motor cortex $\text{GABA}_B$ intracortical inhibition.

## Architecture

```mermaid
flowchart TD
    A[Single Suprathreshold TMS Pulse @ 120% RMT] --> B[Evoke Motor Evoked Potential MEP on Active Target Muscle]
    B --> C[Measure Suppression Duration of Voluntary EMG]
    C --> D[Compute CSP Duration ms & CSP / MEP Ratio]
    D --> E[Classify Normal vs Focal Dystonia Disinhibition < 110 ms]
```

## Quickstart

```python
from client import CorticalSilentPeriodTMSClient

client = CorticalSilentPeriodTMSClient()
result = client.evaluate_csp(
    csp_duration_ms=165.0,
    mep_amplitude_mv=3.8,
    stimulus_intensity_pct_rmt=120.0
)
print(result)
```

## License

Apache-2.0
