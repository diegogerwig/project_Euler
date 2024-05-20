/////////////////////////
//  PROJECT EULER 0005
//  diegogerwig
////////////////////////

/*
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

#include <stdio.h>


int main(void)
{
    int small_numb = 20;

    int smallest = 0;

    while (smallest == 0)
    {
        if (
            small_numb % 1 == 0 && 
            small_numb % 2 == 0 && 
            small_numb % 3 == 0 && 
            small_numb % 4 == 0 && 
            small_numb % 5 == 0 && 
            small_numb % 6 == 0 && 
            small_numb % 7 == 0 && 
            small_numb % 8 == 0 && 
            small_numb % 9 == 0 && 
            small_numb % 10 == 0 && 
            small_numb % 11 == 0 && 
            small_numb % 12 == 0 && 
            small_numb % 13 == 0 && 
            small_numb % 14 == 0 && 
            small_numb % 15 == 0 && 
            small_numb % 16 == 0 && 
            small_numb % 17 == 0 && 
            small_numb % 18 == 0 && 
            small_numb % 19 == 0 && 
            small_numb % 20 == 0)
        {
            smallest = small_numb;
        }
        else
        {
            small_numb += 20;
        }
    }

    printf("El mínimo común múltiplo de 1 a 20 es: %d", small_numb);
    return (0);
}