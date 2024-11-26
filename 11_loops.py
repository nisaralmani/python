# lerning loops here there are two types while and for loops


# x=0
# while (x<=5):
#     print(x)
#     x=x+1


# for x in range(4, 11):
#     print(x)


#array
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
    # if (d == "Fri"): break #loop stops
    if (d=="Fri"): continue #d skiped
    print(d)