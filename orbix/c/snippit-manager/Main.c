#include <stdio.h>
#include <string.h>

void addSnippet() {
    char title[100], code[500];
    FILE *file = fopen("snippets.txt", "a");
    printf("Enter snippet title: ");
    fgets(title, sizeof(title), stdin);
    printf("Enter snippet code: ");
    fgets(code, sizeof(code), stdin);
    fprintf(file, "Title:%sCode:%s\n", title, code);
    fclose(file);
    printf("Snippet added!\n");
}

void listSnippets() {
    char line[600];
    FILE *file = fopen("snippets.txt", "r");
    while(fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }
    fclose(file);
}
