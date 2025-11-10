#include <stdio.h>

void addTask() {
    FILE *file = fopen("tasks.txt", "a");
    char task[256];
    printf("Enter task: ");
    fgets(task, sizeof(task), stdin);
    fprintf(file, "%s", task);
    fclose(file);
}

void listTasks() {
    char line[256];
    FILE *file = fopen("tasks.txt", "r");
    while(fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }
    fclose(file);
}

int main() {
    char cmd[10];
    while(1) {
        printf("Enter command (add, list, exit): ");
        fgets(cmd, sizeof(cmd), stdin);
        if(strncmp(cmd, "add", 3) == 0) addTask();
        else if(strncmp(cmd, "list", 4) == 0) listTasks();
        else if(strncmp(cmd, "exit", 4) == 0) break;
    }
    return 0;
}
