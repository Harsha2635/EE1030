#include <stdio.h>

int main() {
    // Open the file to write the values of 'a'
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the values of 'a' to the file (a = 1 and a = 2)
    fprintf(file, "1.0\n");
    fprintf(file, "2.0\n");

    // Close the file
    fclose(file);

    printf("Values of 'a' written to data.txt\n");

    return 0;
}

