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


class TestGeoList(unittest.TestCase):
    '''
    Test the sift.geo.GeoList class.
    '''
    def setUp(self):
        self.geolist = sift.geo.GeoList(lambda n: n.lat, lambda n: n.lng)

    def test_add_empty_list(self):
        '''
        Test that the add method properly inserts into an empty list.
        '''
        node = sift.geo.GeoNode(0, 0)
        self.geolist.add(node)
        self.assertEqual(len(self.geolist), 1)

    def test_add_shorted_insertion(self):
        '''
        Test that the add method maintains sorted order by latitude.
        '''
        n1 = sift.geo.GeoNode(1, 0)
        n2 = sift.geo.GeoNode(0, 1)
        self.geolist.add(n1)
        self.geolist.add(n2)
        self.assertIs(self.geolist[0], n2)
        self.assertIs(self.geolist[1], n1)
