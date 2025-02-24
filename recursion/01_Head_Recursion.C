#include<stdio.h>

int fun(int n)
{
    int x = 0;

    if(n>0)
    {
        x = fun(n-1);
        printf("%d\n", x);

        return n;
    }
    else
    {
        return n;
    }

    return 0;
}

int main()
{
    int n = 5;
    n = fun(n);

    return 0;
}