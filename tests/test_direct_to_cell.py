"""Unit tests for Direct-to-Cell Interconnect Scheduler."""

import unittest
from leo_satellite_constellation_kernel.core.direct_to_cell_interconnect import DirectToCellInterconnectScheduler
from leo_satellite_constellation_kernel.core.models import CellularUser


class TestDirectToCell(unittest.TestCase):
    def setUp(self):
        self.scheduler = DirectToCellInterconnectScheduler()
        self.users = [
            CellularUser(f"u_{i}", 30.0, -90.0, data_rate_kbps=200.0)
            for i in range(20)
        ]

    def test_cellular_allocation_and_link_margin(self):
        report = self.scheduler.allocate_cell_resources(self.users)

        self.assertGreater(report.connected_users_count, 0)
        self.assertGreater(report.aggregate_throughput_mbps, 0.0)
        self.assertTrue(report.doppler_compensated)
        self.assertGreater(report.link_budget_margin_db, 0.0)


if __name__ == "__main__":
    unittest.main()
