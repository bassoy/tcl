import tcl
import numpy as np
import time
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
a = 288
m = 20
n = 20
u = 16
w = 20
v = 20
gflops = a*m*n*u*w*v*2/1e9
A = np.empty((u,v,w,a), order='f', dtype=np.float32)
B = np.empty((u,n,v,m,w), order='f', dtype=np.float32)
C = np.empty((a,m,n), order='f', dtype=np.float32)
tcl.randomNumaAwareInit(A)
tcl.randomNumaAwareInit(B)
tcl.randomNumaAwareInit(C)
alpha = 1.0
beta = 0.0
s = time.time()
tcl.tensorMult( alpha, A, "u,v,w,a", B, "u,n,v,m,w", beta, C, "a,m,n" )
timeTCL = time.time() - s
s = time.time()
C_ = np.einsum("uvwa,unvmw->amn", A, B)
timeNP = time.time() - s
print "%.2f GFLOPS %.2f GFLOPS %.2fx"%( gflops/timeTCL, gflops/timeNP, timeNP/ timeTCL)
#if( not tcl.equal(C, C_) ):
#    print "validation:" + FAIL + " failed!!!" + ENDC