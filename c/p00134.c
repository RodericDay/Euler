#include "stdio.h"
#include "math.h"

#define N 1000100
#define var __int64_t

var S(var p1, var p2) {
    if (p1==-1 || p1==3) { return 0; }

    var pad = pow(10, ceil(log10(p1)));

    for(var i=0; 1; i++) {
        // k * p2 = B * 10^n + p1
        var m = i*pad+p1;
        if (m % p2 == 0) {
            return m;
        }
    }
}

int main() {

    int sieve[N] = {0};
    for (var i=2; i<N; i++) {sieve[i] = 1;}
    for (var i=2; i<N; i++) {
        if (sieve[i]) { for (var p=2*i; p<N; p+=i) { sieve[p] = 0; } }
    }

    var sum = 0;
    var p2 = -1;
    for (var i=3; i<N; i++) {
        if (sieve[i]) {
            var p1 = p2;
            if (p1>=1000000) {
                break;
            }
            p2 = i;
            sum += S(p1, p2);
        }
    }

    printf("%lli\n", sum);

    return 0;
}
