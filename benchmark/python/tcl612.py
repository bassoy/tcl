import tcl
import numpy as np
import time
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
a = 3240
m = 64
n = 54
u = 54
v = 64
gflops = a*m*n*u*v*2/1e9
A = np.empty((v,u,n,m), order='f', dtype=np.float32)
B = np.empty((a,u,v), order='f', dtype=np.float32)
C = np.empty((m,n,a), order='f', dtype=np.float32)
tcl.randomNumaAwareInit(A)
tcl.randomNumaAwareInit(B)
tcl.randomNumaAwareInit(C)
alpha = 1.0
beta = 0.0
s = time.time()
tcl.tensorMult( alpha, A, "v,u,n,m", B, "a,u,v", beta, C, "m,n,a" )
timeTCL = time.time() - s
s = time.time()
C_ = np.einsum("vunm,auv->mna", A, B)
timeNP = time.time() - s
print "%.2f GFLOPS %.2f GFLOPS %.2fx"%( gflops/timeTCL, gflops/timeNP, timeNP/ timeTCL)
#if( not tcl.equal(C, C_) ):
#    print "validation:" + FAIL + " failed!!!" + ENDC