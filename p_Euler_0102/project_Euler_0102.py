"""
Project Euler Problem 102: Triangle Containment

Find the number of triangles for which the interior contains the origin.
Method: Compare the area of the main triangle with the sum of the areas
of the three triangles formed by joining the vertices to the origin.
"""

import urllib.request
import os

def solve_triangle_containment():
    # 1. Download/Read the file
    filename = 'p102_triangles.txt'
    url = 'https://projecteuler.net/project/resources/p102_triangles.txt'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading: {e}")
            return

    def get_double_area(x1, y1, x2, y2, x3, y3):
        """
        Calculates 2 * Area of a triangle defined by three coordinates.
        Using 2*Area allows us to stick to integer arithmetic.
        Formula: |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
        """
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    origin_count = 0

    with open(filename, 'r') as f:
        for line in f:
            # Parse coordinates: x1, y1, x2, y2, x3, y3
            coords = list(map(int, line.strip().split(',')))
            
            x1, y1 = coords[0], coords[1]
            x2, y2 = coords[2], coords[3]
            x3, y3 = coords[4], coords[5]
            
            # Calculate Area of the full triangle ABC
            area_orig = get_double_area(x1, y1, x2, y2, x3, y3)
            
            # Calculate Areas of sub-triangles with Origin (0,0)
            # Triangle OBC
            area1 = get_double_area(0, 0, x2, y2, x3, y3)
            # Triangle OAC
            area2 = get_double_area(x1, y1, 0, 0, x3, y3)
            # Triangle OAB
            area3 = get_double_area(x1, y1, x2, y2, 0, 0)
            
            # Check containment
            if area_orig == (area1 + area2 + area3):
                origin_count += 1
                
    print(f"Triangles containing the origin: {origin_count}")

if __name__ == "__main__":
    solve_triangle_containment()