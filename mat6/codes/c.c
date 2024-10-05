#include <stdio.h>

int main() {
    // Define parameters for the ellipse and line
    double a = 5.0, b = 3.0;  // Semi-major and semi-minor axes of the ellipse
    double h = 1.0, k = 2.0;  // Center of the ellipse
    double V[2][2] = {{1.0, 0.0}, {0.0, 1.0}};  // Ellipse matrix (identity matrix for simplicity)
    double slope = 0.5;  // Slope of the line
    double intercept = 1.0;  // Y-intercept of the line
    
    // Create and open a .txt file for writing the data
    FILE *file = fopen("data.txt", "w");
    
    // Write ellipse parameters and line parameters to the file
    if (file != NULL) {
        // Writing ellipse parameters a, b, h, k
        fprintf(file, "%.2f\n", a);
        fprintf(file, "%.2f\n", b);
        fprintf(file, "%.2f\n", h);
        fprintf(file, "%.2f\n", k);
        
        // Writing the ellipse matrix V
        fprintf(file, "%.2f\n", V[0][0]);
        fprintf(file, "%.2f\n", V[0][1]);
        fprintf(file, "%.2f\n", V[1][0]);
        fprintf(file, "%.2f\n", V[1][1]);
        
        // Writing the line parameters: slope and intercept
        fprintf(file, "%.2f\n", slope);
        fprintf(file, "%.2f\n", intercept);
        
        fclose(file);
        printf("Data has been written to data.txt\n");
    } else {
        printf("Error opening the file!\n");
    }
    
    return 0;
}

