"""Unit tests for Ground Station Handover Optimizer."""

import unittest
from leo_satellite_constellation_kernel.core.ground_station_handover_optimizer import GroundStationHandoverOptimizer
from leo_satellite_constellation_kernel.core.models import GroundStation


class TestGroundStationHandover(unittest.TestCase):
    def setUp(self):
        self.optimizer = GroundStationHandoverOptimizer()
        self.stations = [
            GroundStation("gs1", "Station 1", 30.0, -90.0, capacity_gbps=40.0),
        ]
        self.sats = ["sat_1"]
        self.pos = {"sat_1": (31.0, -89.0)}

    def test_feeder_handover_contact(self):
        plan = self.optimizer.plan_feeder_handovers(self.sats, self.stations, self.pos)

        self.assertIn("sat_1", plan.active_contacts)
        self.assertEqual(plan.total_feeder_throughput_gbps, 40.0)
        self.assertEqual(plan.contact_continuity_pct, 100.0)
        self.assertGreater(plan.max_doppler_shift_khz, 0.0)


if __name__ == "__main__":
    unittest.main()
