import math


class GeoNode():
    '''
    A class that contains the most basic information about a node.
    That is, the latitude and longitude.
    '''
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def distance(self, node):
        return math.sqrt(math.pow(self.lat - node.lat, 2) +
                         math.pow(self.lng - node.lng, 2))


class GeoContainer():

    def __init__(self, access_lat, access_lng):
        '''
        :param lambda access_lat: a lambda function for accessing the
          latitude of a supplied data element.
        :param lambda access_lng: a lambda function for accessing the
          longiude of a supplied data element.
        '''
        self.access_lat = access_lat
        self.access_lng = access_lng

    def nearby(self, point, distance):
        '''
        Return nodes in this GeoContainer that are nearby the given
        point (within the specified distance).

        :param point: a Point object or tuple defining the point to
          search around.
        :param float distance: a distance to search around the point
          defined in terms of the latitude and longitude.
        :returns: a :class:`set` of nodes that are nearby the `point`.
        '''
        raise NotImplemented()


class GeoList(GeoContainer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes = []

    def add(self, node):
        '''
        Add a node to the GeoList, maintaining sorted order.
        '''
        index = 0
        while index < len(self.nodes):
            if self.access_lat(node) < self.access_lat(self.nodes[index]):
                self.nodes.insert(index, node)
                break
            elif self.access_lat(node) == self.access_lat(self.nodes[index]):
                if self.access_lng(node) < self.access_lng(self.nodes[index]):
                    self.nodes.insert(index, node)
                    break

            index += 1
        self.nodes.append(node)

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes)

    def __getitem__(self, index):
        return self.nodes[index]
