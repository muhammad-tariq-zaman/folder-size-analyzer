import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestAnalyzer(unittest.TestCase):
    def test_sizes_and_top_n(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "small.txt"), "w").write("x" * 10)
            sub = os.path.join(d, "sub")
            os.mkdir(sub)
            open(os.path.join(sub, "big.txt"), "w").write("x" * 100)
            r = main.analyze(d, top_n=1)
            self.assertEqual(r["total_bytes"], 110)
            self.assertEqual(r["file_count"], 2)
            self.assertEqual(len(r["largest"]), 1)
            self.assertTrue(r["largest"][0][0] == 100)

    def test_human(self):
        self.assertEqual(main.human(500), "500 B")
        self.assertEqual(main.human(2048), "2.0 KB")


if __name__ == "__main__":
    unittest.main()
