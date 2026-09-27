"""Integration tests for LeoSatelliteEngine."""

import unittest
from leo_satellite_constellation_kernel.engine import LeoSatelliteEngine


class TestLeoSatelliteEngine(unittest.TestCase):
    def setUp(self):
        self.engine = LeoSatelliteEngine()

    def test_full_benchmark_run(self):
        report = self.engine.run_full_benchmark()

        # 1. ISL Routing
        self.assertGreater(report.isl_path_hops, 0)
        self.assertGreater(report.isl_latency_ms, 0.0)
        self.assertTrue(report.isl_occlusion_free)

        # 2. Beam Hopping
        self.assertGreater(report.beam_served_demand_mbps, 0.0)
        self.assertTrue(report.beam_co_channel_free)

        # 3. Collision Avoidance
        self.assertGreater(report.collision_avoidance_delta_v_mps, 0.0)
        self.assertGreaterEqual(report.collision_post_miss_distance_m, 1200.0)

        # 4. Feeder Handover
        self.assertGreater(report.feeder_total_throughput_gbps, 0.0)
        self.assertGreater(report.feeder_continuity_pct, 0.0)

        # 5. Direct-to-Cell
        self.assertGreater(report.dtc_connected_users, 0)
        self.assertGreater(report.dtc_link_margin_db, 0.0)

        # Total pipeline time
        self.assertLess(report.total_pipeline_time_ms, 1000.0)


if __name__ == "__main__":
    unittest.main()
