x, y, z = map(int, input("Enter three side lengths: ").split())

if x + y > z and x + z > y and y + z > x:
    print("These side lengths can make a triangle.")
else:
    print("These side lengths can't make a triangle.")
