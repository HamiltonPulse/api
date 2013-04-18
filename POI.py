#
# POI.py
#   ORM class representing a point of interest in the API.  A point of interest
#   has a latitude and longitude associated as well as an id and a name.  This
#   base class should be extended by any data objects that build abstractions on
#   top of POIS.
#
from sqlalchemy import Column, String, Enum, Numeric

class POI(object):

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    latitude = Column(Numeric, nullable=False)
    longitude = Column(Numeric, nullable=False)

    def __init__(self, id, name, latitude, longitude):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<POI(%s, %s, %s, %s)>' % \
            (self.id, self.name, str(self.latitude), str(self.longitude))
