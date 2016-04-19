#include <stdio.h>
#include <math.h>
#define var __int64_t

double G = (1+sqrt(5))/2;

// 74049690
int main() {
    int i = 0;
    var max = 0;
    double maxf;
    for (var d=1; d<10000000; d++) {
        for (var n=maxf*d; n*G<d; n++) {
            var N = n*d;
            var D = d*d-n*d-n*n;
            if (N%D==0) {
                var A = N/D;
                if (A > max) {
                    max = A;
                    maxf = 1.*n/d;
                    printf("%i %lli %lli %lli %f\n", ++i, A, n, d, maxf);
                }
            }
        }
    }
}
