"""
MCP Server for Cortical Silent Period (CSP) TMS Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import CorticalSilentPeriodTMSClient


def main():
    client = CorticalSilentPeriodTMSClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_csp",
                            "description": "Calculates Transcranial Magnetic Stimulation (TMS) Cortical Silent Period Duration (ms), MEP-Normalized Ratio, and evaluates motor cortex GABAB intracortical inhibition.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "csp_duration_ms": {
                                        "type": "number",
                                        "description": "Silent period duration in milliseconds (ms)."
                                    },
                                    "mep_amplitude_mv": {
                                        "type": "number",
                                        "description": "Peak-to-peak Motor Evoked Potential amplitude in mV."
                                    },
                                    "stimulus_intensity_pct_rmt": {
                                        "type": "number",
                                        "description": "Stimulus intensity as % of resting motor threshold (default: 120.0)."
                                    },
                                    "muscle_target": {
                                        "type": "string",
                                        "description": "Target muscle name (default: First Dorsal Interosseous)."
                                    },
                                    "patient_age_years": {
                                        "type": "integer",
                                        "description": "Patient age in years (optional)."
                                    }
                                },
                                "required": [
                                    "csp_duration_ms",
                                    "mep_amplitude_mv"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_csp":
                try:
                    out = client.evaluate_csp(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
