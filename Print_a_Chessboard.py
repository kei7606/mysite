import sys

def draw():
    H, W=map(int, input().split())

    if (H==0&W==0):
        sys.exit()
    for y in range(H):
        for x in range(W):
            coord=[x , y]
            if (coord[0]+coord[1])%2==0:
                print("#", end="")
            else:
                print(".", end="")               
        print("\n", end="")

    print("")

while 1:
    draw()