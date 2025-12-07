import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])
    
    if val == 0: return 0 
    return 1 if val > 0 else 2  

def distSq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def graham_scan(points):
    n = len(points)
    if n < 3: return points

    p0 = min(points, key=lambda p: (p[1], p[0]))
    
    current_points = points[:]
    if p0 in current_points:
        current_points.remove(p0)
    
    def angle_sort_key(p):
        angle = math.atan2(p[1] - p0[1], p[0] - p0[0])
        return (angle, -distSq(p0, p))

    current_points.sort(key=angle_sort_key)
    
    
    m = 1
    for i in range(1, len(current_points)):
        while i < len(current_points) - 1 and orientation(p0, current_points[i], current_points[i + 1]) == 0:
            i += 1
        current_points[m] = current_points[i]
        m += 1
    
    if m < 2: 
        if n == 1: return points
        if n == 2: return points
        return [p0, current_points[0]] if m == 1 and current_points else [p0]

    hull = [p0, current_points[0]]
    
    for i in range(1, m): 
        while len(hull) > 1 and orientation(hull[-2], hull[-1], current_points[i]) != 2:
            hull.pop() 
        hull.append(current_points[i])
        
    return hull

points_gs = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
hull_gs = graham_scan(points_gs)
print(f"\n Գրեհեմ Սկան: {hull_gs}")