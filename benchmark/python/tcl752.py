import tcl
import numpy as np
import time
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
a = 24
b = 27
m = 24
o = 27
n = 27
u = 768
gflops = a*b*m*o*n*u*2/1e9
A = np.empty((u,b,a), order='f', dtype=np.float32)
B = np.empty((m,u,n,o), order='f', dtype=np.float32)
C = np.empty((a,o,b,m,n), order='f', dtype=np.float32)
tcl.randomNumaAwareInit(A)
tcl.randomNumaAwareInit(B)
tcl.randomNumaAwareInit(C)
alpha = 1.0
beta = 0.0
s = time.time()
tcl.tensorMult( alpha, A, "u,b,a", B, "m,u,n,o", beta, C, "a,o,b,m,n" )
timeTCL = time.time() - s
s = time.time()
C_ = np.einsum("uba,muno->aobmn", A, B)
timeNP = time.time() - s
print "%.2f GFLOPS %.2f GFLOPS %.2fx"%( gflops/timeTCL, gflops/timeNP, timeNP/ timeTCL)
#if( not tcl.equal(C, C_) ):
#    print "validation:" + FAIL + " failed!!!" + ENDC