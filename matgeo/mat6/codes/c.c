#include <stdio.h>

int main() {
    // Define parabola and circle parameters
    // Parabola y^2 = 4x is always of the form x = y^2 / (4 * p)
    double p = 1.0; // Parabola parameter (y^2 = 4px)

    // Circle (x - h)^2 + (y - k)^2 = r^2
    double r = 1.5; // Radius of the circle
    double h = 0.0; // Center of the circle (x-coordinate)
    double k = 0.0; // Center of the circle (y-coordinate)

    // Open the file to write the parameters
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the parabola parameter to the file
    fprintf(file, "%f\n", p); // Parabola parameter (4p)

    // Write the circle parameters to the file
    fprintf(file, "%f\n", r); // Circle radius
    fprintf(file, "%f\n", h); // Circle center x-coordinate
    fprintf(file, "%f\n", k); // Circle center y-coordinate

    // Close the file
    fclose(file);

    printf("Data written to data.txt\n");

    return 0;
}

