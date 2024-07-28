/**
 * @author:  trieunvt
 * @file:    string_cleaner.c
 * @date:    29 Jul 2024
 * @version: v1.0.0
 * @brief:   String cleaner
**/

#include <stdio.h>
#include <string.h>

/* User-defined macros */
#define DATA_SIZE 1024

/* String cleaner */
char* clean_string(char *p_input, const char *p_trash) {
    char *p_cleaner, *p_anchor;
    p_cleaner = p_input;
    p_anchor = p_input;

    while(*p_cleaner) {
        if(NULL == strchr(p_trash, *p_cleaner)) {
            *p_anchor = *p_cleaner;
            ++p_anchor;
        }

        ++p_cleaner;
    }

    *p_anchor = 0;
    return p_input;
}

/* The main program */
int main(int argc, char const *argv[]) {
    char data[DATA_SIZE] = "a b\rc\nd\texf";

    printf("Before: %s\r\n", data);
    clean_string(data, " \r\n\tx");
    printf("After: %s\r\n", data);

    return 0;
}
