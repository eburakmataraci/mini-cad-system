# math_3d.py
import math

def normalize(v):
    length = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return [0, 0, 0] if length == 0 else [v[0]/length, v[1]/length, v[2]/length]

def cross_product(v1, v2):
    return [
        v1[1]*v2[2] - v1[2]*v2[1], 
        v1[2]*v2[0] - v1[0]*v2[2], 
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def shade_color(hex_color, intensity):
    intensity = max(0.2, min(1.0, intensity))
    try:
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6: return "#000000"
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return f'#{int(r*intensity):02x}{int(g*intensity):02x}{int(b*intensity):02x}'
    except ValueError:
        return "#000000"