import sys

print("--- STL-Creator ---")
print("[1] Quader - [2] Zylinder")
choice = int(input())

if choice == 1:
    type = "cuboid"
    print("Seitenlänge x:")
    x = int(input())
    print("Seitenlänge y:")
    y = int(input())
    print("Seitenlänge z:")
    z = int(input())

if choice == 2:
    type = "zylinder"
    raise NotImplementedError

CUBOID_STL_TEMPLATE = f"""solid {type}
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
endsolid {type}"""

with open("stl_output.stl", "w") as f:
    f.write(CUBOID_STL_TEMPLATE)

print("STL written.")