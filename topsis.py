import numpy as np
import warnings
class topsis:
	a=None #Matrix
	w=None #Weight matrix
	r=None #Normalisation matrix 
	m=None #Number of rows
	n=None #Number of columns
	aw=[] #worst alternative
	ab=[] #best alternative
	diw=None
	dib=None
	siw=None
	sib=None	
	
	#Return a numpy array with float items
	def floater(self,a):
		ax=[]
		for i in a:
			try:
				ix=[]
				for j in i:
					ix.append(float(j))
			except:
				ix=float(i)
				pass
			ax.append(ix)
		return np.array(ax)

	def __init__(self,a,w,j):
		self.a=self.floater(a)
		self.m=len(a)
		self.n=len(a[0])
		self.w=self.floater(w)
		print self.a
		self.w=self.w/sum(self.w)
		self.j=np.array(j)
		#print self.a
		#print self.w
		#print self.j

	#Step 2
	def step2(self):
		self.r=self.a
		for i in range(self.m):
			nm=sum(self.a[i,:]**2)**0.5
			for j in range(self.n):
				self.r[i,j]=self.a[i,j]/nm
	#Step 3
	def step3(self):
		self.t=self.r*self.w
	
	#Step 4
	def step4(self):
		for i in range(self.n):
			if self.j[i]==1:
				self.aw.append(min(self.t[:,i]))
				self.ab.append(max(self.t[:,i]))
			else:
				self.aw.append(max(self.t[:,i]))
				self.ab.append(min(self.t[:,i]))
	#Step 5			
	def step5(self):
		self.diw=(self.t-self.aw)**2
		self.dib=(self.t-self.ab)**2
		#print 'lol'
		#print self.diw
		"""for j in range(self.n):
			self.diw[:,j]=(self.diw[:,j]-self.aw[j])**2
			self.dib[:,j]=(self.dib[:,j]-self.ab[j])**2
		print self.diw"""
		self.dw=[]
		self.db=[]
		for j in range(self.m):
			self.dw.append(sum(self.diw[j,:])**0.5)
			self.db.append(sum(self.dib[j,:])**0.5)
		print self.dw
		self.dw=np.array(self.dw)
		self.db=np.array(self.db)
		print self.dw
		#print self.db

	#Step 6
	def step6(self):
		np.seterr(all='ignore')
		self.siw=self.dw/(self.dw+self.db)
		#print self.siw
		x=0
		m=None
		for i in range(self.m):
			print self.siw[i]
			if self.siw[i]>m or m==None:
				m=self.siw[i]
				x=i
		print 'Choice',x+1,'is the best'
	
	def calc(self):
		self.step2()
		self.step3()
		self.step4()
		self.step5()
		self.step6()
