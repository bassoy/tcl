import tcl
import numpy as np
import time
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
a = 32
u = 32
m = 30
o = 32
n = 32
gflops = a*u*m*o*n*2/1e9
A = np.empty((n,o,m,u), order='f', dtype=np.float32)
B = np.empty((a,u), order='f', dtype=np.float32)
C = np.empty((o,n,a,m), order='f', dtype=np.float32)
tcl.randomNumaAwareInit(A)
tcl.randomNumaAwareInit(B)
tcl.randomNumaAwareInit(C)
alpha = 1.0
beta = 0.0
s = time.time()
tcl.tensorMult( alpha, A, "n,o,m,u", B, "a,u", beta, C, "o,n,a,m" )
timeTCL = time.time() - s
s = time.time()
C_ = np.einsum("nomu,au->onam", A, B)
timeNP = time.time() - s
print "%.2f GFLOPS %.2f GFLOPS %.2fx"%( gflops/timeTCL, gflops/timeNP, timeNP/ timeTCL)
#if( not tcl.equal(C, C_) ):
#    print "validation:" + FAIL + " failed!!!" + ENDC