#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


int main(int argc, string key[])

{
    if (argc == 2)   //перевірка ключа на валідність
    {
        int chk = 1; //змінна перевірки ключа на наявність інших символів крім цифр

        for(int i = 0, lk = strlen(key[1]); i < lk; i++)
            {
            if(!isdigit(key[1][i]) && chk == 1)
                {
                    chk = 0;
                }
            }
        if (chk == 1)
        {
            int keynum = atoi(key[1]);
            string letter = get_string("plaintext: ");
            printf("ciphertext: ");
            for(int i = 0, ll = strlen(letter); i < ll; i++)
            {
                if (isalpha(letter[i])) //початок циклу шифрування
                {
                    int regalpha = isupper(letter[i]) ? 65 : 97;
                    int numalpha = letter[i] - regalpha;
                    int c = ((numalpha + keynum) % 26) + regalpha;
                    printf("%c", c);
                }
                else
                {
                    printf("%c", letter[i]);
                }
            }
            printf("\n");
        }
         else
    {
        printf("Usage: ./ceaser key\n");
        return 1;
    }
    }
    else
    {
        printf("Usage: ./ceaser key\n");
        return 1;
    }
}
