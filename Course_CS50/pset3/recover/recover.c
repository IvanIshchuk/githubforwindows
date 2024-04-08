#include <stdio.h>
#include <stdlib.h>

// Зразок для порівняння перших трьох байтів (1 - 0xFF, 2 - 0xD8, 3 - 0xFF)
// Зразок для порівняння четвертого байту (0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee,
// 0xef)

int main(int argc, char *argv[])
{
    // перевіряємо наявність необхідного аргумента
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image \n");
        return 1;
    }
    // open input file
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    char buffer[512];  // Буфер для зчитаних даних
    size_t read_bytes; // кількість прочитанних байтів в блокові
    int n = -1;        // лічильник знайдених співпадінь та відкритих файлі
    FILE *repcrfile;   // оголошення файлу для запису

    do // Зчитуємо 512 байт даних з файлу
    {
        read_bytes = fread(buffer, 1, sizeof(buffer), infile);
        if (read_bytes == 0)
        {
            fclose(infile);
            return 0;
        }
        else // Беремо перші чотири байти з відрізку в буфері
        {
            unsigned char first_byte = buffer[0];
            unsigned char second_byte = buffer[1];
            unsigned char third_byte = buffer[2];
            unsigned char fourth_byte = buffer[3];

            // Порівняння кожного з перших трьох байтів зі зразком

            if (first_byte == 0xFF && second_byte == 0xD8 && third_byte == 0xFF)
            {

                // Порівняння четвертого байта зі зразком за допомогою операції "і"
                unsigned char pattern[] = {0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7,
                                           0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee, 0xef};
                for (int i = 0; i < 16; i++)
                {
                    if (fourth_byte == pattern[i])
                    {
                        // знайдено співпадіння

                        if (n != -1) // Закриваємо файл з відновленним попереднім зображенням
                        {
                            fclose(repcrfile);
                        }

                        n++;
                        char filename[10]; // Рядок для імені файлу

                        // Сформувати ім'я файлу
                        sprintf(filename, "%03d.jpg", n);

                        // Відкрити файл для запису
                        repcrfile = fopen(filename, "w");
                        if (repcrfile == NULL)
                        {
                            fprintf(stderr, "Помилка відкриття файлу\n");
                            return 3;
                        }
                    }
                }
            }
            if (n != -1)
            {
                fwrite(buffer, sizeof(char), read_bytes, repcrfile);
            }
        }
    }
    while (read_bytes > 0);
}
