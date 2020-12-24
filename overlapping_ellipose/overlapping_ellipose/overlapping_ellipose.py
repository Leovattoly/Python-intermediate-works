from matplotlib import pyplot as plt
from shapely.geometry.point import Point
from shapely import affinity
from matplotlib.patches import Polygon
import numpy as np

class Point:
    def __init__(self,x,y):
        self.X = x
        self.Y = y

class Ellipse:
    def __init__(self,p1,p2,long_axis_width):
        self.x1,self.y1 =p1.X , p1.Y
        self.x2,self.y2 =p2.X , p2.Y
        self.Long_axis_width =long_axis_width

    def create_ellipse(center, lengths, angle=0):
       circ = Point(center).buffer(1)
       ell = affinity.scale(circ, int(lengths[0]), int(lengths[1]))
       ellr = affinity.rotate(ell, angle)
       return ellr


#def computeOverlapOfEllipse(e1,e2):
e1 = Ellipse()
ellipse1 = e1.create_ellipse((0,0),(2,4),10)
verts1 = np.array(ellipse1.exterior.coords.xy)
#patch1 = Polygon(verts1.T, color = 'blue', alpha = 0.5)
#ax.add_patch(patch1)

e2 = Ellipse()
ellipse2 = e2.create_ellipse((1,-1),(3,2),50)
verts2 = np.array(ellipse2.exterior.coords.xy)

intersect = ellipse1.intersection(ellipse2)
verts3 = np.array(intersect.exterior.coords.xy)
print('area of intersect:',intersect.area)



