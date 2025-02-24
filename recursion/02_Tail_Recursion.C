#include<stdio.h>

int funA(int n)
{
    int x = 0;

    if(n>0)
    {
        printf("%d\n", n);
        x = funA(n-1);

        return x;
    }
    else
    {
        return 0;
    }
}


int funB(int n)
{
    while(n>0)
    {
        printf("%d\n", n);
        n--;
    }

    return 0;
}

int main()
{
    int n = 5;

    int x = funA(n);
    int y = funB(n);
    
    return 0;
}