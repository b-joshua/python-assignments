import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--radius', help = 'Radius size', required = True, type = int)
args = parser.parse_args()
radius = args.radius

pi = 3.14

area = pi * (radius**2)
print("Circle area: ", area)

circumference = pi * 2 * radius
print("Circle circumference: ", circumference)