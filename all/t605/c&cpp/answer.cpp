#include <iostream>
#include <stdexcept>

/**
 * @brief Calculates the Body Mass Index (BMI) based on weight and height.
 *
 * The BMI is calculated using the formula:
 *
 *      BMI = weight (kg) / (height (m) * height (m))
 *
 * @param weight The weight of the individual in kilograms.
 * @param height The height of the individual in meters.
 *
 * @return The calculated BMI value as a double.
 *
 * @throws std::invalid_argument if weight or height is less than or equal to zero,
 *                                since these values must be positive.
 */
double calculateBMI(double weight, double height) {
    // Validate weight and height
    if (weight <= 0) {
        throw std::invalid_argument("Weight must be greater than zero.");
    }
    if (height <= 0) {
        throw std::invalid_argument("Height must be greater than zero.");
    }

    // Calculate BMI
    double bmi = weight / (height * height);
    return bmi; // Return the calculated BMI value
}