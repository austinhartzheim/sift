import unittest

import math
import sift.geo


class TestGeoNode(unittest.TestCase):
    '''
    Test the sift.geo.GeoNode class.
    '''
    def test_distance(self):
        n1 = sift.geo.GeoNode(0, 0)
        n2 = sift.geo.GeoNode(0, 0)
        self.assertEqual(n1.distance(n2), 0)

        n1 = sift.geo.GeoNode(0, 0)
        n2 = sift.geo.GeoNode(1, 1)
        self.assertEqual(n1.distance(n2), math.sqrt(2))

