#include <stdio.h>
#include <cs50.h>

int main(void)
{
  string nic = get_string("How your name ?\n");
  printf("Hello, %s\n", nic);
}
