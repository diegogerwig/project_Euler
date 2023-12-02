/////////////////////////
//  PROJECT EULER 0004
//  diegogerwig
////////////////////////

/*
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
*/

#include <stdio.h>

int is_palindrome(int n)
{
  int copy = n;
  int complement = 0;

  while (copy>0){
        complement = complement * 10 + copy % 10;
        copy/=10;
  }
  if (complement==n)
        return 1;
    return 0;
}

int main(void)
{
    int i = 1;
    int j = 1;
    int number = 0;
    int max_palin = 0;

    while(i<1000)
        {
            while(j<1000)
            {
                number = i * j;   
                if (is_palindrome(number) && number > max_palin)
                    max_palin = number;
                j++;
            }
        i++;
        j = i;
        }
    printf("%d\n", max_palin);    
    return (0);
}