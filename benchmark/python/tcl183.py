import tcl
import numpy as np
import time
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
a = 12
b = 8
m = 12
o = 8
n = 12
p = 12
u = 128
gflops = a*b*m*o*n*p*u*2/1e9
A = np.empty((u,p,o,n,m), order='f', dtype=np.float32)
B = np.empty((b,a,u), order='f', dtype=np.float32)
C = np.empty((o,m,n,b,p,a), order='f', dtype=np.float32)
tcl.randomNumaAwareInit(A)
tcl.randomNumaAwareInit(B)
tcl.randomNumaAwareInit(C)
alpha = 1.0
beta = 0.0
s = time.time()
tcl.tensorMult( alpha, A, "u,p,o,n,m", B, "b,a,u", beta, C, "o,m,n,b,p,a" )
timeTCL = time.time() - s
s = time.time()
C_ = np.einsum("uponm,bau->omnbpa", A, B)
timeNP = time.time() - s
print "%.2f GFLOPS %.2f GFLOPS %.2fx"%( gflops/timeTCL, gflops/timeNP, timeNP/ timeTCL)
#if( not tcl.equal(C, C_) ):
#    print "validation:" + FAIL + " failed!!!" + ENDC