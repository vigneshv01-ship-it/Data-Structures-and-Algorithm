#include<stdio.h>

/*
Approach 03:
This is based on recursion.

*/
int numberReverse(int x, long long y)
{
    int q = x/10;
    int r = x%10;

    

    if(q > 0)
    {
        y = ((y+r)*10);
        int z = numberReverse(q, y);

        return z;
    }
    else
    {
        int z = (y+r);

        return z;
    }
}

bool isPalindrome(int x){

    if(x<0)
        return false;
    else if(x == 0)
        return true;

    int reverseValue = numberReverse(x, 0);

    if(reverseValue == x)
        return true;
    else
        return false;
}

int main()
{
    int n = 1221;
    bool palindrome = isPalindrome(n);

    printf("The number %d is a palindrome : %d\n", n, palindrome);

    return 0;
}