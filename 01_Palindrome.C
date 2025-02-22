/*
Approach 01:
This involves identifying the length of the number by variable 'l'.
Then based on the variable 'l', loop through the number by division and work with Quotient and remainder accordingly.

The approach uses loops twice, one to identify the number of digits and the other to get the reverse value of the provided number.

*/

#include<stdio.h>
#include<math.h>

bool isPalindrome(int x) {
    if (x < 0)
{
    return false;
}
else if (x == 0)
{
    return true;
}

int l = 0;

//Find the number of digits in the number
int y = x;
while (y != 0)
{
    y = y / 10;
    l++;
}

if (l == 1)
{
    return true;
}

int divRange = l-1;
int i = x;
int j = 0;

while (divRange >= 0)
{
    int q = i / 10;
    int rem = i % 10;

    i = q;
    j = j + (rem * (pow(10, divRange)));

    divRange--;
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