/////////////////////////
//  PROJECT EULER 0003
//  diegogerwig
////////////////////////

/*
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600 851 475 143 ?
*/

#include <stdio.h>

int main()
{
    //long long n = 13195;
    long long n = 600851475143;
    
    long long div = 2, max_prime;

    printf("Para el número %lli\n", n);
    while (n != 0)
    {
        if (n % div != 0)
            div = div + 1;
        else
        {
            max_prime = n;
            n = n / div;
            if (n == 1)
            {
                printf("el mayor número primo divisor es %d !", max_prime);
                break;
            }
        }
    }
    return 0;
}
