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

    def test_add_sorted_lat_insertion(self):
        '''
        Test that the add method maintains sorted order by latitude.
        '''
        n1 = sift.geo.GeoNode(1, 0)
        n2 = sift.geo.GeoNode(0, 1)
        self.geolist.add(n1)
        self.geolist.add(n2)
        self.assertIs(self.geolist[0], n2)
        self.assertIs(self.geolist[1], n1)

    def test_add_sorted_lng_insertion(self):
        n1 = sift.geo.GeoNode(0, 0)
        n2 = sift.geo.GeoNode(3, 2)
        n3 = sift.geo.GeoNode(3, 1)
        self.geolist.add(n1)
        self.geolist.add(n2)
        self.geolist.add(n3)
        self.assertIs(self.geolist[0], n1)
        self.assertIs(self.geolist[1], n3)
        self.assertIs(self.geolist[2], n2)

    def text_box(self):
        '''
        Test that the box method correctly returns a generator that,
        upon iteration, yields all nodes that are inside the given
        box (inclusive).
        '''
        n1 = sift.geo.GeoNode(0, 0)
        n2 = sift.geo.GeoNode(1, 1)
        n3 = sift.geo.GeoNode(2, 2)
        n4 = sift.geo.GeoNode(3, 3)
        self.geolist.add(n1)
        self.geolist.add(n2)
        self.geolist.add(n3)
        self.geolist.add(n4)

        nodes = [node for node in self.geolist.box((1, 2.5, 2.5, 1))]
        self.assertIn(n2, nodes)
        self.assertIn(n3, nodes)
        self.assertNotIn(n1, nodes)
        self.assertNotIn(n4, nodes)

    def test_iter_length(self):
        '''
        Test that calling iter() on a GeoList object will result in an
        iterable object with the correct number of iterations.
        '''
        ITERATION_COUNT = 3

        node = sift.geo.GeoNode(0, 0)
        for _ in range(0, ITERATION_COUNT):
            self.geolist.add(node)
        iterable = iter(self.geolist)

        count = 0
        for each in iterable:
            self.assertIs(each, node)
            count += 1
        self.assertEqual(count, ITERATION_COUNT)
