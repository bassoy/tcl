import tcl
import numpy as np
import time
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
a = 48
m = 48
u = 50
w = 50
v = 48
gflops = a*m*u*w*v*2/1e9
A = np.empty((v,w,u,a), order='f', dtype=np.float32)
B = np.empty((m,w,v,u), order='f', dtype=np.float32)
C = np.empty((a,m), order='f', dtype=np.float32)
tcl.randomNumaAwareInit(A)
tcl.randomNumaAwareInit(B)
tcl.randomNumaAwareInit(C)
alpha = 1.0
beta = 0.0
s = time.time()
tcl.tensorMult( alpha, A, "v,w,u,a", B, "m,w,v,u", beta, C, "a,m" )
timeTCL = time.time() - s
s = time.time()
C_ = np.einsum("vwua,mwvu->am", A, B)
timeNP = time.time() - s
print "%.2f GFLOPS %.2f GFLOPS %.2fx"%( gflops/timeTCL, gflops/timeNP, timeNP/ timeTCL)
#if( not tcl.equal(C, C_) ):
#    print "validation:" + FAIL + " failed!!!" + ENDC