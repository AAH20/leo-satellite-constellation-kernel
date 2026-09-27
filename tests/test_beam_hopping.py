"""Unit tests for Phased-Array Beam Hopping Scheduler."""

import unittest
from leo_satellite_constellation_kernel.core.models import GroundCellDemand
from leo_satellite_constellation_kernel.core.phased_array_beam_hopping import PhasedArrayBeamHoppingScheduler


class TestBeamHopping(unittest.TestCase):
    def setUp(self):
        self.scheduler = PhasedArrayBeamHoppingScheduler()
        self.demands = [
            GroundCellDemand("c1", 40.0, -74.0, 500.0, priority=2),
            GroundCellDemand("c2", 40.1, -74.1, 400.0, priority=1),  # Very close to c1 (same freq will interfere)
            GroundCellDemand("c3", 45.0, -80.0, 300.0, priority=1),  # Far away
        ]

    def test_beam_allocation_and_interference(self):
        report = self.scheduler.schedule_beams("sat1", self.demands, num_steerable_beams=4)

        self.assertTrue(report.co_channel_interference_free)
        self.assertGreater(report.served_demand_mbps, 0.0)
        self.assertGreater(report.average_sinr_db, 10.0)


if __name__ == "__main__":
    unittest.main()
