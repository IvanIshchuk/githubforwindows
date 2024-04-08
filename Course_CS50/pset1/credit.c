//Program for credit card

#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
        long ccnum; //- number of credit card,
        int ccdigitl = 0; //- last digit of credit card,
        int counter = 0; //- counter of digits,
        int sum1 = 0; //- summa of first digits
        int sum2 = 0; // - resuit of second digit * 2
        int sum3 = 0; // - summa of second digits
        int sumtotal = 0; // - summa all of digits
        int firstdigit = 0; // first two digits of credit card

        ccnum = get_long("Number: ");

        while (ccnum > 0)
        {
        ccdigitl = ccnum % 10;
        counter++;
                if (counter % 2 != 0)
                {
                        sum1 += ccdigitl;
                }
                else
                {
                        sum2 = ccdigitl*2;
                        sum3 = sum3 + sum2 / 10 + sum2 % 10;
                }

                if(ccnum / 100 == 0 && firstdigit == 0)
                {
                        firstdigit = ccnum;
                }

        ccnum = ccnum / 10;
        }
        sumtotal = sum1 + sum3;

        if(sumtotal % 10 == 0 && counter == 15 && (firstdigit == 34 || firstdigit == 37))
        {
                printf("AMEX\n");
        }
        else if(sumtotal %10 == 0 && counter == 16 && firstdigit >=51 && firstdigit <=55)
        {
                printf("MASTERCARD\n");
        }
        else if(sumtotal %10 == 0 && (counter == 13 || counter == 16) && firstdigit / 10 == 4)
        {
                printf("VISA\n");
        }
        else
        {
                printf("INVALID\n");
        }
}
