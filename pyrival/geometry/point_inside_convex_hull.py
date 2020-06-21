# (x,y) is the point which is to be tested if present inside convex hull or not.
# "poly" is list of all the points of which convex hull is made of, preferably list of list eg. poly = [[1,1],[1,0],[0,1]]
# Note: this function return false if point is on the boundary, meaning it returns true only if the point is strictly inside.

def point_inside_convex_hull(x,y,poly):
        
    n = len(poly)
    inside = True

    for i in range(n):
        p1x,p1y = poly[i]
        p2x,p2y = poly[(i+1) % n]
        d=(x-p1x)*(p2y-p1y) - (y-p1y)*(p2x-p1x)
        if d>=0:
            return not inside
    return inside
