#include "stdlib.h"
#include "stdio.h"
#include "math.h"

#define var __int64_t
#define fmt "%lli\n"
#define lim 50000000
#define nsol 1

var f(var x, var a) {
    return 6*x*a - pow(x, 2) - 5*pow(a, 2);
}

int main() {
    var a = 0;
    var *counter = (var*)malloc(lim * sizeof(var)); // heap
    while (1) {
        a += 1;
        if (2*a+1 > lim && f(5*a-1, a) > lim) { break; }

        // rainbow from left
        for (var x=2*a+1; x<3*a+1; x++) {
            var y = f(x, a);
            if (y >= lim) { break; }
            counter[y] += 1;
        }

        // rainbow from right
        for (var x=5*a-1; x>3*a; x--) {
            var y = f(x, a);
            if (y >= lim) { break; }
            counter[y] += 1;
        }
    }

    var ans = 0;
    for (var i=0; i<lim; i++) {
        ans += counter[i]==nsol;
    }
    printf(fmt, ans);
}
