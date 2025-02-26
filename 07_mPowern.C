#include<stdio.h>
#include<stdlib.h>

// Recursion Approach
double powerByRecursion(double x, int n)
{
    double m = 1;
    int i = 0;

    if(n==0)
        return 1;
    else if(n == 1)
        return x;
    else 

    if(x==0 || x==1)
        return x;

    if(n<0)
    {
        int j = -2;
        unsigned int k;

        k = ~j;
        // j *= -1;
        // n *= -1;
        x = 1/x;
    }

    if(i%2==0)
    {
        m = powerByRecursion(x*x, i/2);
    }
    else
    {
        m= powerByRecursion(x,i-1)*x;
    }

    return m;
}

// Loop
double powerByLoop(double x, int n)
{
    double i = 1;

    while(n>0)
    {
        i = i*x;
        n--;
    }

    if(n<0)
    {
        while(n<0)
        {
            i = i*x;
            n++;
        }

        i=1/i;
    }

    return i;
}

int main()
{
    double i = powerByRecursion(2.00000,-2147483648);

    printf("%f\n", i);

    // double j = powerByLoop(2.00000, -2);

    // printf("%f\n", j);

    return 0;
}