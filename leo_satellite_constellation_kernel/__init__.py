"""LEO Satellite Megaconstellation Optimization Kernel.

Production-grade algorithmic solvers for the 5 Apex NP-Hard and Non-Convex problems
across optical laser cross-links, phased-array beam hopping, and orbital mechanics.
"""

from .core import (
    AvoidanceManeuverPlan,
    BeamHoppingScheduleReport,
    CellularUser,
    DebrisConjunction,
    DirectToCellInterconnectScheduler,
    DirectToCellReport,
    FeederHandoverPlan,
    GroundCellDemand,
    GroundStation,
    GroundStationHandoverOptimizer,
    IslRoutingResult,
    IslTopologyReconfigurationSolver,
    LaserCrossLink,
    OrbitalCollisionManeuverSolver,
    PhasedArrayBeamHoppingScheduler,
    SatelliteNode,
    SpotBeamAllocation,
)

__version__ = "0.1.0"

__all__ = [
    "IslTopologyReconfigurationSolver",
    "PhasedArrayBeamHoppingScheduler",
    "OrbitalCollisionManeuverSolver",
    "GroundStationHandoverOptimizer",
    "DirectToCellInterconnectScheduler",
    # Models
    "SatelliteNode",
    "LaserCrossLink",
    "IslRoutingResult",
    "GroundCellDemand",
    "SpotBeamAllocation",
    "BeamHoppingScheduleReport",
    "DebrisConjunction",
    "AvoidanceManeuverPlan",
    "GroundStation",
    "FeederHandoverPlan",
    "CellularUser",
    "DirectToCellReport",
]
