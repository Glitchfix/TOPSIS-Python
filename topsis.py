import numpy as np

import cx_Oracle
db=cx_Oracle.connect('username','password')
cur2=db.cursor()
cur2.execute('select * from tablename')
res=cur2.fetchall()
cur2.close()
db.close()


#Row/Column size
r=len(res)
c=len(res[0])

#Preference flags
cs=[int(i) for i in raw_input("Insert the flags: ").split()]

#weights
wt=np.array([float(i) for i in raw_input("Weight: ").split()])

import datetime
#Matrix foramation
ar=[]
for j in range(r):
    l=[]
    for i in res[j]:
	if i.count(':')==0:
		l.append(float(i))
	else:
		time=i.split(':')
		dt=datetime.timedelta(hours=time[0],minutes=time[1], seconds=time[-1])
		l.append(float(dt.total_seconds()/3600))
    ar.append(l)
#ar=[list(i) for i in res]
a=np.array(ar)
print a

def n_weight(stt):
    for i in range(len(stt)):
        if stt[i]>=1 and stt[i]<=2:
            stt[i]=9
        elif stt[i]>=3 and stt[i]<=4:
            stt[i]=7
        elif stt[i]>=5 and stt[i]<=6:
            stt[i]=5
        elif stt[i]>=7 and stt[i]<=8:
            stt[i]=9
        else:
            stt[i]=1
    return stt

def stt_weight(stt):
    for i in range(len(stt)):
        if stt[i]>=1 and stt[i]<=2:
            stt[i]=9
        elif stt[i]>=3 and stt[i]<=4:
            stt[i]=7
        elif stt[i]>=5 and stt[i]<=6:
            stt[i]=5
        elif stt[i]>=7 and stt[i]<=8:
            stt[i]=9
        else:
            stt[i]=1
    return stt

def du_weight(stt):
    for i in range(len(stt)):
        if stt[i]>=1 and stt[i]<=2:
            stt[i]=9
        elif stt[i]>=3 and stt[i]<=4:
            stt[i]=7
        elif stt[i]>=5 and stt[i]<=6:
            stt[i]=5
        elif stt[i]>=7 and stt[i]<=8:
            stt[i]=9
        else:
            stt[i]=1
    return stt

def de_weight(stt):
    for i in range(len(stt)):
        if stt[i]>=1 and stt[i]<=2:
            stt[i]=9
        elif stt[i]>=3 and stt[i]<=4:
            stt[i]=7
        elif stt[i]>=5 and stt[i]<=6:
            stt[i]=5
        elif stt[i]>=7 and stt[i]<=8:
            stt[i]=9
        else:
            stt[i]=1
    return stt








def powpow(sq):
	if sq==0:
		return 0
	return sq**2
def sqrt(sq):
	return sq**0.5


nw=n_weight(a[:,0])

sttw=(a[:,3]-a[:,1])/a[:,2]
sttw=stt_weight(sttw)

duw=a[:,2]
duw=du_weight(duw)

dew=a[:,3]
dew=de_weight(dew)
a[:,0]=nw
a[:,1]=sttw
a[:,2]=duw
a[:,3]=dew

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

sst=[]  #S*
sd=[]   #S'
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
'''for k in range(len(c)):
    for i in range(k):
        if c[i]>c[i+1]:
            temp=c[i]
            c[i]=c[i+1]
            c[i+1]=temp'''
print c
pin={}
for i in range(len(c)):
    pin[c[i]]=i
c.sort()
c=c[::-1]
for i in c:
    print pin[i]
