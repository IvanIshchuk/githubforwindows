#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int shift(char c);

int main(int argc, string key[])

{
    if (argc == 2) // перевірка ключа на валідність
    {
        int chk = 1; // змінна перевірки ключа на наявність інших символів крім літер

        for (int i = 0, lk = strlen(key[1]); i < lk; i++)
        {
            if (!isalpha(key[1][i]) && chk == 1)
            {
                chk = 0;
            }
        }
        if (chk == 1)
        {
            string letter = get_string("plaintext: ");
            printf("ciphertext: ");
            int k = 0; // змінна для перебирання ключа
            for (int i = 0, ll = strlen(letter); i < ll; i++)
            {
                if (isalpha(letter[i])) // початок циклу шифрування
                {
                    int keynum = shift(key[1][k]);
                    int regalpha = isupper(letter[i]) ? 65 : 97;
                    int numalpha = letter[i] - regalpha;
                    int c = ((numalpha + keynum) % 26) + regalpha;
                    printf("%c", c);
                    k++;
                    if (strlen(key[1]) == k)
                    {
                        k = 0;
                    }
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

int shift(char c)
{
    int regalphakey = isupper(c) ? 65 : 97;
    return (int) c - regalphakey;
}
