"""
Cortical Silent Period (CSP) & Transcranial Magnetic Stimulation (TMS) Client.
Zero-mock pure Python standard library implementation.
Calculates TMS Cortical Silent Period Duration (ms), MEP-Normalized CSP Ratio,
and intracortical GABAB-mediated inhibitory neurophysiology.
"""

import math
from typing import Dict, Any, Optional


class CorticalSilentPeriodTMSClient:
    """
    Evaluates motor cortex GABAB-mediated intracortical inhibition via single-pulse TMS:
    - Target muscle held at 20-30% Maximum Voluntary Contraction (MVC)
    - Single suprathreshold TMS pulse (120% RMT) applied over primary motor cortex (M1)
    - CSP duration (ms): from MEP stimulus artifact/offset to resumption of uninterrupted voluntary EMG
    - MEP peak-to-peak amplitude (mV)
    - Ratio: CSP_duration_ms / MEP_amplitude_mv
    """

    def __init__(self):
        pass

    def evaluate_csp(
        self,
        csp_duration_ms: float,
        mep_amplitude_mv: float,
        stimulus_intensity_pct_rmt: Optional[float] = 120.0,
        muscle_target: Optional[str] = "First Dorsal Interosseous (FDI)",
        patient_age_years: Optional[int] = 35
    ) -> Dict[str, Any]:
        """
        Calculates TMS Cortical Silent Period parameters.
        csp_duration_ms: measured silent period duration in milliseconds (50 to 350 ms).
        mep_amplitude_mv: peak-to-peak Motor Evoked Potential in mV (0.5 to 10.0 mV).
        stimulus_intensity_pct_rmt: stimulation intensity as percentage of resting motor threshold (default 120%).
        muscle_target: target hand/limb muscle name.
        """
        if csp_duration_ms <= 0 or mep_amplitude_mv <= 0:
            raise ValueError("CSP duration and MEP amplitude must be strictly positive.")

        # MEP-Normalized CSP Ratio (ms / mV)
        csp_mep_ratio = csp_duration_ms / mep_amplitude_mv

        # Normal clinical reference ranges at 120% RMT in intrinsic hand muscles:
        # Normal CSP: 120.0 - 220.0 ms
        # Shortened CSP (< 110.0 ms): Cortical Hyperexcitability / Disinhibition (epilepsy, dystonia, ALS)
        # Prolonged CSP (> 240.0 ms): Excessive Intracortical Inhibition (Parkinsonian hypokinesia, GABAB agonists)
        if csp_duration_ms < 110.0:
            inhibition_status = "Pathologically Shortened CSP / Intracortical Disinhibition"
            neurocircuitry = "Deficient cortical GABAB-mediated inhibitory interneuronal tone; high motor cortex hyperexcitability seen in focal dystonia, myoclonus, or early ALS."
        elif csp_duration_ms > 240.0:
            inhibition_status = "Prolonged CSP / Excessive Intracortical Inhibition"
            neurocircuitry = "Hyperactive GABAB receptor neurotransmission or heightened basal ganglia-thalamocortical inhibitory drive; characteristic of Parkinsonian rigidity or baclofen exposure."
        elif csp_duration_ms >= 120.0 and csp_duration_ms <= 220.0:
            inhibition_status = "Normal Physiological Intracortical Inhibition"
            neurocircuitry = "Equilibrated motor cortical glutamatergic facilitation and GABAB-mediated inhibitory interneuronal feedback."
        else:
            inhibition_status = "Borderline / Intermediate Cortical Silent Period"
            neurocircuitry = "Subtle alteration in motor cortex silent period kinetics; repeat with recruitment curve testing."

        return {
            "status": "success",
            "tms_metrics": {
                "csp_duration_ms": round(csp_duration_ms, 1),
                "mep_amplitude_mv": round(mep_amplitude_mv, 2),
                "csp_mep_ratio_ms_per_mv": round(csp_mep_ratio, 2),
                "stimulus_intensity_pct_rmt": stimulus_intensity_pct_rmt,
                "target_muscle": muscle_target
            },
            "neurophysiological_assessment": {
                "inhibition_status": inhibition_status,
                "neurocircuitry": neurocircuitry
            }
        }
