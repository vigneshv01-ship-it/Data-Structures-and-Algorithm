#include<stdio.h>

int sumOfNNumbers(int n)
{
    int x;

    while(n>0)
    {
        x = x+n;
        n--;
    }

    return x; 
}


int main()
{
    int i = sumOfNNumbers(5);

    printf("%d\n", i);

    return 0;
}