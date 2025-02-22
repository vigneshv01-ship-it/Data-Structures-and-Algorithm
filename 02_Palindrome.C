/*

Approach 02:
This is an improvement of the approach 01. This involves using the loop once. 
There is no need to lookup for the number of digits in 'x'. Instead it goes through the loop until the quotient value is 0.

This has showm improved time complexity than approach 01.

*/

#include<stdio.h>

bool isPalindrome(int x) {

if (x < 0)
{
    return false;
}
else if (x == 0)
{
    return true;
}

int y = x;
int i = x;
long long j = 0;

while (i != 0)
{
    int q = i / 10;
    int rem = i % 10;

    i = q;
    j = (j + rem);

    if(i != 0)
    {
        j = j * 10;
    }
}

if (j == x)
    return true;
else
    return false;
}

int main()
{

    int n = 1234567899;
    bool palindrome = isPalindrome(n);

    printf("The number %d is a palindrome : %d\n", n, palindrome);

    return 0;
}