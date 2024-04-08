// Recize BMP file

#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

int main(int argc, char *argv[])
{
    // перевіряємо наявність необхідних аргументів
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize n filein fileout \n");
        return 1;
    }
     int n = atoi(argv[1]);
     if(n < 1 || n > 100)
     {
        fprintf(stderr, "Usage: ./resize n filein fileout \n");
        return 1;
     }

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    //визначаємо нові розміри картинки
    int inbiWidth = bi.biWidth;
    int inbiHeight = bi.biHeight;
    int outbiWidth = inbiWidth * n;
    int outbiHeight = inbiHeight * n;

     // determine padding for inscanlines and outscalines
    int inpadding = (4 - (inbiWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int outpadding = (4 - (outbiWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    bi.biWidth = outbiWidth;
    bi.biHeight = outbiHeight;
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * outbiWidth) + outpadding) * abs(outbiHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    //оголошення масиву для рядка та визначення його розміру
    RGBTRIPLE scanline[outbiWidth * sizeof(RGBTRIPLE)];

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(inbiHeight); i < biHeight; i++)
    {
        // iterate over pixels in scanline
        for (int j = 0; j < inbiWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            //read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            //створення рядка з новим розміром
            for(int k = 0; k < n; k++)
            {
                scanline[(j * n) + k] = triple;
            }
        }

        // skip over padding, if any перескакуємо через вирівнювання
        // у вихідному файлі, якщо воно є
        fseek(inptr, inpadding, SEEK_CUR);


        //друкуємо розтягнутий рядок n раз
        for (int k = 0; k < n; k++)
        {
            fwrite(&scanline, sizeof(RGBTRIPLE), outbiWidth, outptr);

        //добавляємо вирівнювання
        for(int x = 0; x < outpadding; x++)
            fputc(0x00, outptr);
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
