def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])
    if val == 0: return 0
    return 1 if val > 0 else 2

def jarvis_march(points):
    n = len(points)
    if n < 3: return points 
    
    l = min(range(n), key=lambda i: points[i][0])
    
    hull = []
    p = l
    
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        
        p = q
        
        if p == l:
            break
            
    return hull
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
hull = jarvis_march(points)
print(f"\n Ջարվիս Մարչ.: {hull}") 