a=40
b=36
c=30
d=a-b
e=b-c
if d>e:                          #running training is more important
    print("running training is more important")
elif d<e:                        #strength training is more important
    print("strength training is more important")
else:                            #no difference
    print("no difference")

X=True
Y=False
print(not X==Y)
#    A     B      W
#   T      T      F
#   T      F      T
#   F      T      T
#   F      F      F