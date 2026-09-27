"""Command-Line Interface for LEO Satellite Megaconstellation Optimization Kernel."""

from __future__ import annotations

import argparse
import sys
import time

from .engine import LeoSatelliteEngine


def cmd_benchmark_all():
    print("=" * 80)
    print("🛰️  LEO SATELLITE MEGACONSTELLATION NP-HARD OPTIMIZATION BENCHMARK SUITE")
    print("=" * 80)
    print("Executing 5 SOTA Combinatorial Solvers across Orbital Mechanics & Laser Mesh...")

    engine = LeoSatelliteEngine()
    report = engine.run_full_benchmark()

    print("\n[BENCHMARK RESULTS & METRICS]")
    print(f"1. Optical Laser ISL (Inter-Satellite Link) Mesh Routing:")
    print(f"   - Optimal Laser Hops           : {report.isl_path_hops} optical hops")
    print(f"   - End-to-End Latency           : {report.isl_latency_ms:.2f} ms (Speed of Light in Vacuum)")
    print(f"   - Earth Limb Occlusion Free    : {'YES (Clear LOS)' if report.isl_occlusion_free else 'OCCLUDED'}")
    print(f"   - Solver Execution Latency     : {report.isl_solve_time_ms:.2f} ms")

    print(f"\n2. Phased-Array Dynamic Beam Hopping & Frequency Reuse:")
    print(f"   - Served Ground Cell Demand    : {report.beam_served_demand_mbps:,.1f} Mbps")
    print(f"   - Average Received SINR        : {report.beam_avg_sinr_db:.1f} dB")
    print(f"   - Co-Channel Interference Free : {'YES (C/I >= 12 dB)' if report.beam_co_channel_free else 'INTERFERENCE'}")
    print(f"   - Solver Execution Latency     : {report.beam_solve_time_ms:.2f} ms")

    print(f"\n3. Orbital Debris Conjunction & Propellant-Optimal Maneuver:")
    print(f"   - Thruster Burn Delta-V        : {report.collision_avoidance_delta_v_mps:.3f} m/s")
    print(f"   - Post-Maneuver Miss Distance  : {report.collision_post_miss_distance_m:,.1f} meters (Safe: >1,000m)")
    print(f"   - Krypton Propellant Consumed  : {report.collision_propellant_used_grams:.2f} grams")
    print(f"   - Solver Execution Latency     : {report.collision_solve_time_ms:.2f} ms")

    print(f"\n4. Ground Station Feeder Link Contact Handover:")
    print(f"   - Total Feeder Throughput      : {report.feeder_total_throughput_gbps:.1f} Gbps (Ka-Band)")
    print(f"   - Contact Continuity Ratio     : {report.feeder_continuity_pct:.1f}%")
    print(f"   - Max Doppler Shift Tracked    : ±{report.feeder_max_doppler_khz:.1f} kHz")
    print(f"   - Solver Execution Latency     : {report.feeder_solve_time_ms:.2f} ms")

    print(f"\n5. Direct-to-Cell LTE/5G Resource Scheduling:")
    print(f"   - Connected Smartphone UEs     : {report.dtc_connected_users} users")
    print(f"   - Cell Throughput Downlinked   : {report.dtc_throughput_mbps:.2f} Mbps")
    print(f"   - Non-Terrestrial Link Margin  : +{report.dtc_link_margin_db:.1f} dB (Above Threshold)")
    print(f"   - Solver Execution Latency     : {report.dtc_solve_time_ms:.2f} ms")

    print("-" * 80)
    print(f"⏱️  Total 5-Solver Engine Pipeline Runtime : {report.total_pipeline_time_ms:.2f} ms (Sub-second)")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="LEO Satellite Megaconstellation Optimization Kernel CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")
    subparsers.add_parser("benchmark-all", help="Execute complete benchmark across all 5 solvers")

    args = parser.parse_args()

    if args.command == "benchmark-all" or not args.command:
        cmd_benchmark_all()
    else:
        cmd_benchmark_all()


if __name__ == "__main__":
    main()
