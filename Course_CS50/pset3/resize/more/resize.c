// Recize BMP file more

#include "bmp.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // перевіряємо наявність необхідних аргументів
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize f filein fileout \n");
        return 1;
    }

    float f;
    sscanf(argv[1], "%f", &f);

    if (f < 0 || f > 100)
    {
        fprintf(stderr, "Usage: ./resize f filein fileout \n");
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
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    // визначаємо нові розміри зображення
    int inbiWidth = bi.biWidth;
    int inbiHeight = bi.biHeight;
    int outbiWidth = round(inbiWidth * f);
    int outbiHeight = round(inbiHeight * f);

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

    // determine ratio
    double widthRatio = (double) inbiWidth / (double) outbiWidth;
    double heightRatio = (double) inbiHeight / (double) outbiHeight;

    // allocate a memory to store one scanline
    RGBTRIPLE scanline[inbiWidth * sizeof(RGBTRIPLE)];
    int cachedScanline = -1;

    // for all rows in the new image
    for (int i = 0, biHeight = abs(outbiHeight); i < biHeight; i++)
    {
        // compute the Y coordinate of the corresponding row in the old image
        int row = i * heightRatio;

        // read the corresponding scanline from the old image unless it's cached
        if (cachedScanline != row)
        {
            fseek(inptr,
                  sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + (((sizeof(RGBTRIPLE) * inbiWidth) + inpadding) * row),
                  SEEK_SET);
            fread(scanline, sizeof(RGBTRIPLE), inbiWidth, inptr);
            cachedScanline = row;
        }

        // for all columns in the new image
        for (int j = 0; j < outbiWidth; j++)
        {
            // compute the X coordinate of the corresponding column in the old image
            int column = j * widthRatio;
            fwrite(&scanline[column], sizeof(RGBTRIPLE), 1, outptr);
        }

        // write new padding
        for (int j = 0; j < outpadding; j++)
        {
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
