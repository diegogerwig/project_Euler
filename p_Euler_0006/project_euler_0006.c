/////////////////////////
//  PROJECT EULER 0006
//  diegogerwig
////////////////////////

/*
Sum square difference
Problem 6
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
*/

#include <stdio.h>

int main(void)
{
    int diff = 0;
    int sum_sq = 0;
    int sq_sum = 0;
    int i = 1;
    int j = 1;
    int sum_j = 0;
    
    while (i<=100)
    {
        sum_sq = sum_sq + (i*i);
        i++;
        printf("%d\n", sum_sq);
    }

    while (j <= 100)
    {
        sum_j = sum_j + j;
        sq_sum = sum_j * sum_j;
        j++;
        printf("%d\n", sq_sum);
    }

    diff = sq_sum - sum_sq;
    printf("La diferencia entre el cuadrado de la suma y la suma de los cuadrados de los 100 primeros números naturales es: %d\n", diff);

    return (0);
}