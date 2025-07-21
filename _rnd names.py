from random import choice
n=[]
#for i in 
a=['tommy','pamela','james']
b=['henderson','johnson','lewis','baxter','mason','akbar']
for i in range(0,7):
    rname=(choice(a),choice(b))
    n.append (rname)
    print (rname)
    print ((n))
    print(set(n))
    h=n.count(rname)
print ('number of unique names in list is  ',h)

#want count of set...above not working.