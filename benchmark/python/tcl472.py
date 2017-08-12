import tcl
import numpy as np
import time
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
a = 480
m = 24
o = 24
n = 24
u = 24
v = 24
gflops = a*m*o*n*u*v*2/1e9
A = np.empty((m,v,n,o,u), order='f', dtype=np.float32)
B = np.empty((v,u,a), order='f', dtype=np.float32)
C = np.empty((m,o,a,n), order='f', dtype=np.float32)
tcl.randomNumaAwareInit(A)
tcl.randomNumaAwareInit(B)
tcl.randomNumaAwareInit(C)
alpha = 1.0
beta = 0.0
s = time.time()
tcl.tensorMult( alpha, A, "m,v,n,o,u", B, "v,u,a", beta, C, "m,o,a,n" )
timeTCL = time.time() - s
s = time.time()
C_ = np.einsum("mvnou,vua->moan", A, B)
timeNP = time.time() - s
print "%.2f GFLOPS %.2f GFLOPS %.2fx"%( gflops/timeTCL, gflops/timeNP, timeNP/ timeTCL)
#if( not tcl.equal(C, C_) ):
#    print "validation:" + FAIL + " failed!!!" + ENDC