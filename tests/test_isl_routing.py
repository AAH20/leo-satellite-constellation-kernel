"""Unit tests for Optical ISL Routing Solver."""

import unittest
from leo_satellite_constellation_kernel.core.isl_topology_reconfiguration import IslTopologyReconfigurationSolver
from leo_satellite_constellation_kernel.core.models import LaserCrossLink, SatelliteNode


class TestIslRouting(unittest.TestCase):
    def setUp(self):
        self.solver = IslTopologyReconfigurationSolver()
        self.satellites = {
            "sat_a": SatelliteNode("sat_a", 0, 0, 550.0),
            "sat_b": SatelliteNode("sat_b", 0, 1, 550.0),
            "sat_c": SatelliteNode("sat_c", 1, 1, 550.0),
        }
        self.links = [
            LaserCrossLink("l1", "sat_a", "sat_b", True, distance_km=1500.0),
            LaserCrossLink("l2", "sat_b", "sat_c", False, distance_km=1600.0),
        ]

    def test_optimal_isl_path(self):
        res = self.solver.compute_optimal_isl_path("sat_a", "sat_c", self.satellites, self.links)

        self.assertEqual(res.path, ["sat_a", "sat_b", "sat_c"])
        self.assertGreater(res.end_to_end_latency_ms, 0.0)
        self.assertFalse(res.is_occluded_by_earth)
        self.assertTrue(res.is_pointing_feasible)


if __name__ == "__main__":
    unittest.main()
