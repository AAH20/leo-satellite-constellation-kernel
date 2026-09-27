"""Strongly-typed data models for LEO Satellite Megaconstellation Kernel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple


# ============================================================================
# 1. Optical ISL (Inter-Satellite Link) Models
# ============================================================================

@dataclass
class SatelliteNode:
    sat_id: str
    plane_id: int
    index_in_plane: int
    altitude_km: float = 550.0
    true_anomaly_deg: float = 0.0


@dataclass
class LaserCrossLink:
    link_id: str
    sat1: str
    sat2: str
    is_intra_plane: bool
    distance_km: float
    capacity_gbps: float = 100.0
    gimbal_pointing_error_deg: float = 0.0


@dataclass
class IslRoutingResult:
    path: List[str]
    end_to_end_latency_ms: float
    is_occluded_by_earth: bool
    is_pointing_feasible: bool
    solve_time_ms: float


# ============================================================================
# 2. Phased-Array Beam Hopping Models
# ============================================================================

@dataclass
class GroundCellDemand:
    cell_id: str
    lat_deg: float
    lon_deg: float
    demand_mbps: float
    priority: int = 1


@dataclass
class SpotBeamAllocation:
    beam_id: int
    sat_id: str
    cell_id: str
    carrier_freq_ghz: float
    sinr_db: float


@dataclass
class BeamHoppingScheduleReport:
    allocations: List[SpotBeamAllocation]
    served_demand_mbps: float
    unserved_demand_mbps: float
    average_sinr_db: float
    co_channel_interference_free: bool
    solve_time_ms: float


# ============================================================================
# 3. Orbital Debris Collision Avoidance Models
# ============================================================================

@dataclass
class DebrisConjunction:
    conjunction_id: str
    sat_id: str
    debris_id: str
    miss_distance_m: float
    collision_probability: float
    time_to_closest_approach_sec: float


@dataclass
class AvoidanceManeuverPlan:
    conjunction_id: str
    sat_id: str
    delta_v_mps: float
    burn_duration_sec: float
    post_maneuver_miss_distance_m: float
    propellant_used_grams: float
    collision_eliminated: bool
    solve_time_ms: float


# ============================================================================
# 4. Ground Station Feeder Handover Models
# ============================================================================

@dataclass
class GroundStation:
    gs_id: str
    name: str
    lat_deg: float
    lon_deg: float
    capacity_gbps: float = 40.0


@dataclass
class FeederHandoverPlan:
    active_contacts: Dict[str, str]  # sat_id -> gs_id
    total_feeder_throughput_gbps: float
    contact_continuity_pct: float
    max_doppler_shift_khz: float
    solve_time_ms: float


# ============================================================================
# 5. Direct-to-Cell LTE/5G Models
# ============================================================================

@dataclass
class CellularUser:
    ue_id: str
    lat_deg: float
    lon_deg: float
    data_rate_kbps: float


@dataclass
class DirectToCellReport:
    connected_users_count: int
    aggregate_throughput_mbps: float
    doppler_compensated: bool
    link_budget_margin_db: float
    solve_time_ms: float
