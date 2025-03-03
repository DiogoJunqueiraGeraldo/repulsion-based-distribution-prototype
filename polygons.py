from enum import Enum

class PolygonType(Enum):
    CHEVRON = 1
    NOTCHED_RECTANGLE = 2
    STARFISH = 3
    CROISSANT = 4
    SAWTOOTH_HEXAGON = 5
    COMPLEX_GEAR = 6
    STAR = 7
    DIAMOND = 8

# Configuration of polygons (coordinates without closing point)
POLYGON_SHAPES = {
    PolygonType.CHEVRON: [
        (1, 1), (3, 5), (5, 1), (3, 3)
    ],
    PolygonType.NOTCHED_RECTANGLE: [
        (0, 0), (5, 0), (5, 5), (3, 5), (3, 3), (0, 3)
    ],
    PolygonType.STARFISH: [
        (3, 0), (5, 4), (1, 2), (5, 2), (1, 4)
    ],
    PolygonType.CROISSANT: [
        (2, 0), (5, 2), (4, 5), (1, 5), (0, 2)
    ],
    PolygonType.SAWTOOTH_HEXAGON: [
        (0, 2), (2, 0), (4, 0), (6, 2), (4, 4), (2, 4)
    ],
    PolygonType.COMPLEX_GEAR: [
        (2,0), (3,1), (4,0), (5,2), (6,0), (5,4), 
        (4,3), (2,5), (0,4), (1,4), (0,2), (1,1)
    ],
    PolygonType.STAR: [
        (3, 0), (4, 2), (6, 3), (4, 4), (5, 7),
        (3, 5), (1, 7), (2, 4), (0, 3), (2, 2)
    ],
    PolygonType.DIAMOND: [
        (1, 3), (2.5, 4), (4.5, 4), (6, 3), (3, 0)
    ]
}

def get_polygon_coords(polygon_type: PolygonType):
    """Returns coordinates for the specified polygon type"""
    return POLYGON_SHAPES[polygon_type]