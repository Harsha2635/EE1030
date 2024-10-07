#include <stdio.h>
#include <math.h>

int main() {
    double AB, BC, angleB_rad, AC;

    // Ask user to input the sides AB and BC and angle B
    printf("Enter the length of side AB (in cm): ");
    scanf("%lf", &AB);

    printf("Enter the length of side BC (in cm): ");
    scanf("%lf", &BC);

    printf("Enter the angle B (in degrees): ");
    double angleB;
    scanf("%lf", &angleB);

    // Convert angle B to radians (as math functions in C use radians)
    angleB_rad = angleB * M_PI / 180.0;

    // Calculate the length of AC using Pythagoras theorem (since angle B = 90 degrees)
    AC = sqrt(AB * AB + BC * BC);

    // Display the result
    printf("The length of side AC is: %.2lf cm\n", AC);

    // Create and open a file named 'values.tex' for writing
    FILE *file = fopen("values.tex", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(file, "AB: %.2lf\n", AB);
    fprintf(file, "BC: %.2lf\n", BC);
    fprintf(file, "B: %.2lf\n", angleB);
    fclose(file);

    printf("The values.tex file has been created successfully.\n");

    return 0;
}

