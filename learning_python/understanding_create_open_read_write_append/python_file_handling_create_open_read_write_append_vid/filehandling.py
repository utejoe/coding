f = open("chienvh.txt", "a+") # open file in mode: w, r, a, b, +
for num in range(3):
    f.write("Hello World from ChienVH %d\r" %(num + 1))
f.close()
