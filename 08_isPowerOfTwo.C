#include<stdio.h>

bool isPowerOfTwo(int n) {
    
    if(n==0)
        return false;
    else if(n == 1)
        return true;

    if(n>0)
    {
        if(n%2 == 0)
            return true;
        else
            return false;
    }
    else
    {
        int x = 1/n;

        if(x%2 == 0)
            return true;
        else
            return false;
    }
}

int main()
{
    bool i = isPowerOfTwo(0);

    printf("%d\n", i);

    return 0;
}