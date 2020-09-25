# 퀴즈.1

for i in range(1,10,1): 
    for j in range(1,10,1):
        print("{:1}x{:1}={:<3}".format(j,i,i*j),end=" ")
    if j==9:
        print()
    
    

# 퀴즈.2
# for i in range(0,5,1):
#     for j in range(0,5,1):
#         print("{}".format(i*j),end=" ")
#     print("\n")

# 퀴즈.3
# for i in range(0,5,1):
#     for j in range(1,6,1):
#         print("{}".format(j+i*5),end="\t")
#     print()
