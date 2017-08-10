/*
*   Copyright (C) 2017  Paul Springer (springer@aices.rwth-aachen.de)
*
*   This program is free software: you can redistribute it and/or modify
*   it under the terms of the GNU Lesser General Public License as published by
*   the Free Software Foundation, either version 3 of the License, or
*   (at your option) any later version.
*
*   This program is distributed in the hope that it will be useful,
*   but WITHOUT ANY WARRANTY; without even the implied warranty of
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*   GNU General Public License for more details.
*
*   You should have received a copy of the GNU General Public License
*   along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <assert.h>

#include <utils.h>

namespace tcl
{ 

   int getNumThreads(){
      auto tmp = std::getenv("OMP_NUM_THREADS");
      if( tmp ) 
         return std::max(1, atoi(tmp));
      else
         return 1;
   }

   bool isIdentity(const std::vector<int> &perm){
      for(int i=0; i < perm.size(); ++i)
         if( i != perm[i] )
            return false;
      return true;
   }

   template<> 
   void gemm<float>(const char *transa, const char *transb,
         const sizeType *m, const sizeType *n, const sizeType *k,
         const float *alpha, const float *a,
         const sizeType *lda, const float *b, const sizeType *ldb,
         const float *beta, float *c, const sizeType *ldc)
   {
#ifdef DEBUG
      std::cout<< "GEMM: " << transa+'\0' << " "<< transb+'\0' << " "<< *m << " " << *n << " " << *k << std::endl;
#endif
      sgemm_(transa, transb, m, n, k,
            alpha, a, lda, b, ldb,
            beta, c, ldc);
   }

   template<> 
   void gemm<double>(const char *transa, const char *transb,
         const sizeType *m, const sizeType *n, const sizeType *k,
         const double *alpha, const double *a,
         const sizeType *lda, const double *b, const sizeType *ldb,
         const double *beta, double *c, const sizeType *ldc)
   {
#ifdef DEBUG
      std::cout<< "GEMM: " << transa+'\0' << " "<< transb+'\0' << " "<< *m << " " << *n << " " << *k << std::endl;
#endif
      dgemm_(transa, transb, m, n, k,
            alpha, a, lda, b, ldb,
            beta, c, ldc);
   }
}