#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int count;
     do
    {
       count = get_int("Height: ");
    }
    while(count<1 || count>8);

    for(int y = 1; y<=count; y++)
    {
        int c = count-y;
        while(c>0)
        {
           printf(" ");
           c--;
        }
        for(int x = 1; x<=y; x++)
        {
         printf("#");
        }
         printf("  ");
         for(int x = 1; x<=y; x++)
        {
         printf("#");
        }
     printf("\n");
    }
}
