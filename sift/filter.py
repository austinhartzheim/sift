

class Filter():
    '''
    A generic filter class defining a base interface for other classes
    performing filtering operations.
    '''
    pass


class BoxFilter(Filter):
    def __init__(self, box, access_lat, access_lng):
        '''
        :param box: a tuple or Box object defining the area to select
          inside as part of the filter. This is defined with two
          points: the top left (x1) and the bottom-right (x2) in the
          following order for a tuple::

              (x1.lat, x1.lng, x2.lat, x2.lng)
        :param lambda access_lat: a lambda function for accessing the
          latitude of a supplied data element.
        :param lambda access_lng: a lambda function for accessing the
          longiude of a supplied data element.
        '''
        self.box = box  # TODO: convert to Box class
        self.access_lat = access_lat
        self.access_lng = access_lng


class ImposmBoxFilter(BoxFilter):
    def __init__(self, box):
        '''
        :param box: a tuple or Box object defining the area to select
          inside as part of the filter. This is defined with two
          points: the top left (x1) and the bottom-right (x2) in the
          following order for a tuple::

              (x1.lat, x1.lng, x2.lat, x2.lng)
        '''
        super().__init__(box, lambda node: node[2][0], lambda node: node[2][1])
