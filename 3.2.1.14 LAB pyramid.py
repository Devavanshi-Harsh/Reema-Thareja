blocks=int(input("enter your blocks"))
bricks=0
layer=0
while bricks<=blocks:
    layer+=1
    bricks+=layer
    if bricks>blocks:
        bricks-=layer
        layer-=1
        break
print("The height of the pyramid: ",layer, "in", bricks,"bricks")
