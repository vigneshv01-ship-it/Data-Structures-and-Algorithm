#include<stdio.h>

int factorial(int n)
{
    int x = 1;
    int y = 1;

    while(x<=n)
    {
        y = y * x;
        x++;    
    }

    return y;
}

int main()
{
    int i = factorial(1);
    printf("%d\n", i);

    return 0;
}