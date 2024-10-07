#include <stdio.h>

int main() {
    // Values determined for our scenario
    double a_values[] = {1.0, 2.0};  // Just dummy values
    FILE *file = fopen("data.txt", "w");
    
    if (file == NULL) {
        fprintf(stderr, "Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < 2; i++) {
        fprintf(file, "%f\n", a_values[i]);
    }

    fclose(file);
    return 0;
}

