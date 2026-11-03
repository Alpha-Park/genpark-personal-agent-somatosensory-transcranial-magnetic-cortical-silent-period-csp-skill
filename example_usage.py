"""
Example usage of Cortical Silent Period (CSP) TMS Skill.
Demonstrates normal motor cortex GABAB inhibition vs focal dystonia cortical disinhibition.
"""

import json
from client import CorticalSilentPeriodTMSClient


def main():
    print("=== Testing Cortical Silent Period TMS Skill ===")
    client = CorticalSilentPeriodTMSClient()

    # 1. Healthy adult control (CSP = 165.0 ms, MEP = 3.8 mV at 120% RMT -> Normal physiological inhibition)
    res_normal = client.evaluate_csp(
        csp_duration_ms=165.0,
        mep_amplitude_mv=3.8,
        stimulus_intensity_pct_rmt=120.0,
        muscle_target="First Dorsal Interosseous (FDI)"
    )
    print("\n[Case 1: Normal Intracortical Inhibition]")
    print(json.dumps(res_normal, indent=2))

    # 2. Patient with writer's cramp focal dystonia (Shortened CSP = 75.0 ms, MEP = 4.2 mV -> Marked disinhibition)
    res_dystonia = client.evaluate_csp(
        csp_duration_ms=75.0,
        mep_amplitude_mv=4.2,
        stimulus_intensity_pct_rmt=120.0,
        muscle_target="First Dorsal Interosseous (FDI)"
    )
    print("\n[Case 2: Focal Dystonia / Cortical Disinhibition]")
    print(json.dumps(res_dystonia, indent=2))

    # Assertions
    assert res_normal["tms_metrics"]["csp_duration_ms"] >= 120.0
    assert "Normal" in res_normal["neurophysiological_assessment"]["inhibition_status"]
    assert res_dystonia["tms_metrics"]["csp_duration_ms"] < 110.0
    assert "Disinhibition" in res_dystonia["neurophysiological_assessment"]["inhibition_status"]
    print("\n[SUCCESS] Cortical Silent Period TMS tests passed!")


if __name__ == "__main__":
    main()
