#Kiah Johnson
#CS 536

import math
import sys

def control_points(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            x = list(map(float, line.split()))
            points.append(x)
    return points

def bezier_curve(points, u):
    n = len(points) - 1
    point = [0, 0, 0]
    for i in range(n + 1):
        coefficient = math.factorial(n) / (math.factorial(i) * math.factorial(n - i))
        q = coefficient * ((1 - u) ** (n - i)) * (u ** i)
        for j in range(3):
            point[j] += points[i][j] * q
    return point

def main():
    filename = sys.argv[2]
    n = sys.argv[4]
    radius = sys.argv[6]

    if filename == 'filename':
        filename = 'cpts_in.txt'

    if n == 'n':
        n = 20
    else:
        n = int(sys.argv[4])

    if radius == 'radius':
        radius = 0.1
    else:
        radius = float(sys.argv[6])

    control_pts = control_points(filename)
    du = 1 / n

    print('#Inventor V2.0 ascii\n\n')
    print('Separator {LightModel {model BASE_COLOR} Material {diffuseColor 1.0 1.0 1.0}')
    print('Coordinate3 {\tpoint [')
        
    for k in range (n + 1):
        u = k * du
        pt = bezier_curve(control_pts, u)
        print(f'{pt[0]} {pt[1]} {pt[2]},')

    print(']}')
    print('IndexedLineSet {coordIndex [')

    for k in range(n + 1):
        print(f'{k}, ', end='')
    print('-1\n]}}')

    for i in control_pts:
        print('Separator {LightModel {model PHONG}Material {	diffuseColor 1.0 1.0 1.0}')
        print('Transform {translation')
        print(' '.join(map(str, i)))
        print(f'}}Sphere {{\tradius {radius} }}}}')

if __name__ == '__main__':
    main()