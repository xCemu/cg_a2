import sys
from math import cos, sin, pi

def generate_cuboid_stl(x, y, z):
  cuboid_stl = f"""solid cuboid
  facet normal 0 0 1
    outer loop
      vertex 0 {y} {z}
      vertex {x} 0 {z}
      vertex {x} {y} {z}
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex {x} 0 {z}
      vertex 0 {y} {z}
      vertex 0 0 {z}
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0 0 0
      vertex {x} {y} 0
      vertex {x} 0 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex {x} {y} 0
      vertex 0 0 0
      vertex 0 {y} 0
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 0 0 0
      vertex {x} 0 {z}
      vertex 0 0 {z}
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex {x} 0 {z}
      vertex 0 0 0
      vertex {x} 0 0
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex {x} 0 {z}
      vertex {x} {y} 0
      vertex {x} {y} {z}
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex {x} {y} 0
      vertex {x} 0 {z}
      vertex {x} 0 0
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex {x} {y} 0
      vertex 0 {y} {z}
      vertex {x} {y} {z}
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 0 {y} {z}
      vertex {x} {y} 0
      vertex 0 {y} 0
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 0 0 0
      vertex 0 {y} {z}
      vertex 0 {y} 0
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 0 {y} {z}
      vertex 0 0 0
      vertex 0 0 {z}
    endloop
  endfacet
  endsolid cuboid"""
  return cuboid_stl

def calculate_vertices(r):
  side_num = 6  # Seitenanzahl
  start_angle = 0  # Startwinkel
  i = 0
  xs = []
  ys = []
  while i < side_num:
    t = 2*pi*(i/side_num+start_angle)
    x = round(cos(t)*r, 5)
    y = round(sin(t)*r, 5)
    xs.append(x)
    ys.append(y)
    i += 1
  return xs, ys

def generate_cylinder_stl(r, h):
  cylinder_stl = "solid cylinder\n"
  xs, ys = calculate_vertices(r)
  for n in range(len(xs)):
    cylinder_stl += f"{xs[n]}, {ys[n]}\n"
  cylinder_stl += "endsolid cylinder\n"
  return cylinder_stl


if __name__ == "__main__":

  print("--- STL-Creator ---")
  print("[1] Quader - [2] Zylinder")
  choice = int(input())

  if choice == 1:
      print("Seitenlänge x:")
      x = int(input())
      print("Seitenlänge y:")
      y = int(input())
      print("Seitenlänge z:")
      z = int(input())
      output = generate_cuboid_stl(x, y, z)

  if choice == 2:
      print("Radius r:")
      r = int(input())
      print("Höhe h:")
      h = int(input())
      output = generate_cylinder_stl(r, h)
      
  with open("stl_output.stl", "w") as f:
    f.write(output)

  print("STL written.")