"""Unit tests for Orbital Collision Maneuver Solver."""

import unittest
from leo_satellite_constellation_kernel.core.models import DebrisConjunction
from leo_satellite_constellation_kernel.core.orbital_collision_maneuver import OrbitalCollisionManeuverSolver


class TestOrbitalCollision(unittest.TestCase):
    def setUp(self):
        self.solver = OrbitalCollisionManeuverSolver()
        self.conjunction = DebrisConjunction(
            conjunction_id="conj_1",
            sat_id="sat_101",
            debris_id="deb_99",
            miss_distance_m=20.0,
            collision_probability=0.01,
            time_to_closest_approach_sec=14400.0,
        )

    def test_avoidance_maneuver(self):
        plan = self.solver.plan_avoidance_maneuver(self.conjunction)

        self.assertTrue(plan.collision_eliminated)
        self.assertGreater(plan.delta_v_mps, 0.0)
        self.assertGreaterEqual(plan.post_maneuver_miss_distance_m, 1200.0)
        self.assertGreater(plan.propellant_used_grams, 0.0)


if __name__ == "__main__":
    unittest.main()
