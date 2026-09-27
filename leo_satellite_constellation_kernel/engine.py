"""LEO Satellite Megaconstellation Optimization Engine."""

from __future__ import annotations

from dataclasses import dataclass
import time
from typing import Dict, List, Tuple

from .core.models import (
    CellularUser,
    DebrisConjunction,
    GroundCellDemand,
    GroundStation,
    LaserCrossLink,
    SatelliteNode,
)
from .core.isl_topology_reconfiguration import IslTopologyReconfigurationSolver
from .core.phased_array_beam_hopping import PhasedArrayBeamHoppingScheduler
from .core.orbital_collision_maneuver import OrbitalCollisionManeuverSolver
from .core.ground_station_handover_optimizer import GroundStationHandoverOptimizer
from .core.direct_to_cell_interconnect import DirectToCellInterconnectScheduler


@dataclass
class LeoSatelliteBenchmarkReport:
    """Consolidated KPI report across all 5 LEO Satellite Megaconstellation Solvers."""
    # 1. Optical Laser ISL Routing
    isl_path_hops: int
    isl_latency_ms: float
    isl_occlusion_free: bool
    isl_solve_time_ms: float
    # 2. Phased-Array Beam Hopping
    beam_served_demand_mbps: float
    beam_avg_sinr_db: float
    beam_co_channel_free: bool
    beam_solve_time_ms: float
    # 3. Orbital Debris Collision Avoidance
    collision_avoidance_delta_v_mps: float
    collision_post_miss_distance_m: float
    collision_propellant_used_grams: float
    collision_solve_time_ms: float
    # 4. Ground Station Handover
    feeder_total_throughput_gbps: float
    feeder_continuity_pct: float
    feeder_max_doppler_khz: float
    feeder_solve_time_ms: float
    # 5. Direct-to-Cell LTE/5G
    dtc_connected_users: int
    dtc_throughput_mbps: float
    dtc_link_margin_db: float
    dtc_solve_time_ms: float
    # Total
    total_pipeline_time_ms: float


class LeoSatelliteEngine:
    """Unified Orchestration Engine for LEO Satellite Megaconstellation Solvers."""

    def __init__(self):
        self.isl_solver = IslTopologyReconfigurationSolver()
        self.beam_scheduler = PhasedArrayBeamHoppingScheduler()
        self.collision_solver = OrbitalCollisionManeuverSolver()
        self.handover_optimizer = GroundStationHandoverOptimizer()
        self.dtc_scheduler = DirectToCellInterconnectScheduler()

    def run_full_benchmark(self) -> LeoSatelliteBenchmarkReport:
        """Executes full benchmark suite across all 5 space megaconstellation solvers."""
        t0 = time.perf_counter()

        # 1. Optical Laser ISL Routing Benchmark (Trans-Oceanic Laser Cross-Link)
        satellites = {
            f"sat_{p}_{i}": SatelliteNode(f"sat_{p}_{i}", plane_id=p, index_in_plane=i, altitude_km=550.0)
            for p in range(4)
            for i in range(8)
        }
        links = [
            LaserCrossLink("isl_0_1", "sat_0_0", "sat_0_1", is_intra_plane=True, distance_km=1400.0),
            LaserCrossLink("isl_1_2", "sat_0_1", "sat_1_1", is_intra_plane=False, distance_km=1650.0),
            LaserCrossLink("isl_2_3", "sat_1_1", "sat_2_2", is_intra_plane=False, distance_km=1800.0),
            LaserCrossLink("isl_3_4", "sat_2_2", "sat_3_3", is_intra_plane=True, distance_km=1450.0),
        ]
        isl_res = self.isl_solver.compute_optimal_isl_path("sat_0_0", "sat_3_3", satellites, links)

        # 2. Phased-Array Beam Hopping Benchmark (Steerable Spot Beams over High-Density Ground Cells)
        ground_demands = [
            GroundCellDemand("cell_nyc", lat_deg=40.7, lon_deg=-74.0, demand_mbps=850.0, priority=2),
            GroundCellDemand("cell_bos", lat_deg=42.3, lon_deg=-71.0, demand_mbps=600.0, priority=1),
            GroundCellDemand("cell_phl", lat_deg=39.9, lon_deg=-75.1, demand_mbps=450.0, priority=1),
            GroundCellDemand("cell_dc", lat_deg=38.9, lon_deg=-77.0, demand_mbps=700.0, priority=2),
        ]
        beam_res = self.beam_scheduler.schedule_beams("sat_0_0", ground_demands, num_steerable_beams=8)

        # 3. Orbital Debris Collision Avoidance Benchmark
        conjunction = DebrisConjunction(
            conjunction_id="conj_cosmos_1408",
            sat_id="sat_0_0",
            debris_id="debris_track_88219",
            miss_distance_m=34.0,  # Critical hazard (<50m)
            collision_probability=0.008,
            time_to_closest_approach_sec=21600.0,  # 6 hours
        )
        coll_res = self.collision_solver.plan_avoidance_maneuver(conjunction)

        # 4. Ground Station Handover Benchmark (Ka-band 40 Gbps Teleport Contact)
        ground_stations = [
            GroundStation("gs_hawaii", "Hawaii Gateway", 19.8, -155.5),
            GroundStation("gs_redmond", "Redmond Gateway", 47.6, -122.1),
        ]
        visible_sats = ["sat_0_0", "sat_0_1"]
        sat_pos = {"sat_0_0": (20.5, -154.0), "sat_0_1": (48.0, -121.5)}
        feeder_res = self.handover_optimizer.plan_feeder_handovers(visible_sats, ground_stations, sat_pos)

        # 5. Direct-to-Cell LTE/5G Benchmark (Standard Smartphone Connections from Space)
        users = [
            CellularUser(f"ue_{i}", lat_deg=35.0 + (i * 0.01), lon_deg=-115.0, data_rate_kbps=250.0)
            for i in range(80)
        ]
        dtc_res = self.dtc_scheduler.allocate_cell_resources(users)

        total_pipeline_time_ms = (time.perf_counter() - t0) * 1000.0

        return LeoSatelliteBenchmarkReport(
            isl_path_hops=len(isl_res.path) - 1 if isl_res.path else 0,
            isl_latency_ms=isl_res.end_to_end_latency_ms,
            isl_occlusion_free=(not isl_res.is_occluded_by_earth),
            isl_solve_time_ms=isl_res.solve_time_ms,
            beam_served_demand_mbps=beam_res.served_demand_mbps,
            beam_avg_sinr_db=beam_res.average_sinr_db,
            beam_co_channel_free=beam_res.co_channel_interference_free,
            beam_solve_time_ms=beam_res.solve_time_ms,
            collision_avoidance_delta_v_mps=coll_res.delta_v_mps,
            collision_post_miss_distance_m=coll_res.post_maneuver_miss_distance_m,
            collision_propellant_used_grams=coll_res.propellant_used_grams,
            collision_solve_time_ms=coll_res.solve_time_ms,
            feeder_total_throughput_gbps=feeder_res.total_feeder_throughput_gbps,
            feeder_continuity_pct=feeder_res.contact_continuity_pct,
            feeder_max_doppler_khz=feeder_res.max_doppler_shift_khz,
            feeder_solve_time_ms=feeder_res.solve_time_ms,
            dtc_connected_users=dtc_res.connected_users_count,
            dtc_throughput_mbps=dtc_res.aggregate_throughput_mbps,
            dtc_link_margin_db=dtc_res.link_budget_margin_db,
            dtc_solve_time_ms=dtc_res.solve_time_ms,
            total_pipeline_time_ms=round(total_pipeline_time_ms, 2),
        )
