// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Represents a hash table
node *hashtable[N];

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        int numfa = hash(word); // звертаємося до функції та надаємо змінній індекс значення першої букви слова з словника

        // Поміщаємо значення у відповідний елемент хеш-таблиці
        node *n = malloc(sizeof(node));
        if (!n)
        {
            return 1;
        }

        // Add word to list
        if (hashtable[numfa] == NULL)
        {
            strcpy(n->word, word); // Копіюємо перше слово у вузол (корзину)
            n->next = NULL;
            hashtable[numfa] = n;
        }
        else
        {
            strcpy(n->word, word); // Копіюємо наступне слово у вузол (корзину)
            n->next = hashtable[numfa];
            hashtable[numfa] = n;
        }
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    int c = 0;
    for (int i = 0; i < N; i++)
    {
        node *ptr = hashtable[i];
        while (ptr != NULL)
        {
            node *next = ptr->next;
            c++;
            ptr = next;
        }
    }
    return c;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int i = hash(word); // викликаємо функцію хешування та визначаємо індекс для слова з тексту
    node *ptr = hashtable[i]; // звертаємося до корзини з відповідним індексом
    while (ptr != NULL)       // цикл пошуку слова в словнику
    {
        // char worddic;
        node *next = ptr->next;
        char *worddic = ptr->word;
        ptr = next;
        // Порівнюємо слово зі словами у словнику
        if (strcasecmp(word, worddic) == 0)
        {
            // Якщо слово знайдено у словнику, повертаємо true
            return true;
        }
    }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++) // Free memory
    {
        node *ptr = hashtable[i];
        while (ptr != NULL)
        {
            node *next = ptr->next;
            free(ptr);
            ptr = next;
        }
    }
    return true;
}
