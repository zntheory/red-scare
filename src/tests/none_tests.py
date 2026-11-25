import unittest
import os
from algorithms.none import none

DATAPATH = os.path.dirname(os.path.realpath("data/*.txt"))

containsNoSol = [
    "bht",
    "commons-1-20",
    "commons-2-20",
]

containsSol = [
    "dodecahedron",
    "G-ex",
    "gnm-10-15-0"
]

class TestNoneSuccess(unittest.TestCase):
    def test_g_ex(self):
        want = 4
        file = f"{DATAPATH}/G-ex.txt"
        with open(file, "r") as f:
            res = none(f)
            self.assertEqual(res, want)

class TestNoneFailure(unittest.TestCase):
    @unittest.expectedFailure
    def test_commons(self):
        want = -1
        for file in os.listdir(DATAPATH):
            if file.startswith("common-"):
                with open(f"{DATAPATH}/{file}", "r") as f:
                    res = none(f)
                    self.assertEqual(res, want)

if __name__ == '__main__':
    unittest.main()
