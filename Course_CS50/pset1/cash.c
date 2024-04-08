//Program count of money

#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float change;
    do //input coorect date <0
    {
        change = get_float("Change owed: ");
    }
    while(change<=0);

    int cash = round(change * 100);

        int m25 = cash / 25;
        cash = cash % 25;
        int m10 = cash / 10;
        cash = cash % 10;
        int m5 = cash / 5;
        cash = cash % 5;

        int coins = cash + m25 + m10 +m5;
        printf("%i\n", coins);
}
