import numpy as np

#Row/Column size
r,c=[int(i) for i in raw_input("Insert Row and Column: ").split()]	#Row and Columns


#Preference flags
cs=[int(i) for i in raw_input("Insert the flags: ").split()]


#Weights
wt=np.array([float(i) for i in raw_input("Weight: ").split()])


#Matrix foramation
ar=[]
for i in range(r):
    l=[float(i) for i in raw_input("Row "+str(i)+": ").split()]
    ar.append(l)

a=np.array(ar)

def powpow(sq):
	if sq==0:
		return 0
	return sq**2
def sqrt(sq):
	return sq**0.5
pewpew=np.vectorize(powpow)
pepe=np.vectorize(sqrt)
#Step 1(a)
ap=pewpew(a)
x=[]
for i in range(c):
    x.append(sum(ap[:,i])**0.5)

#Step 1(b) and Step 2
for i in range(c):
	for j in range(r):
		a[j,i]*=(wt[i]/x[i])
    

#Step 3(a) and Step 3(b)
ast=[]	#A*
ad=[]	#A'
for i in range(c):
    if cs[i]==0:
       ad.append(min(a[:,i]))
       ast.append(max(a[:,i]))
    else:
        ad.append(min(a[:,i]))
        ast.append(max(a[:,i]))

#Step 4(a)
ast=np.array([ast]*r)
ad=np.array([ad]*r)

a_sst=ast-a
a_sd=ad-a
a_sst=pewpew(a_sst)
a_sd=pewpew(a_sd)

sst=[]
sd=[]
for i in range(r):
	u=a_sst[i].sum()
	p=a_sd[i].sum()
	sst.append(u)
	sd.append(p)

sst=np.array(sst)
sd=np.array(sd)
sst=pepe(sst)
sd=pepe(sd)

#Step 5
c=[]
for i in range(r):
    m=sd[i]/(sst[i]+sd[i])
    c.append(m)

mx=max(c)

#Answer
print '\nBest precentile:',mx,"\nBest choice index:",c.index(mx)
