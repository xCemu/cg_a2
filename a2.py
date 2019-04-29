import sys

print("--- STL-Creator ---")
print("[1] Quader - [2] Zylinder")
choice = int(input())

if choice == 1:
    type = "cuboid"

elif choice == 2:
    type = "zylinder"

else:
    print("Invalid choice.")
    sys.exit()

output_stl = f"solid {type}"

# create STL

output_stl += f"endsolid {type}"

with open("stl_output.stl", "a+") as f:
    print("Writing STL ...\n")
    f.truncate(0) #  clear file
    for line in output_stl:
        f.write(line)
        print(line)
    
    
