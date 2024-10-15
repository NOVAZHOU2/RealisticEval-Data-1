#include <iostream>
#include <stdexcept>
#include <iomanip>
#include <cmath>

double calculateDiscount(double originalPrice, double actualPrice) {
    // Validate input
    if (originalPrice <= 0) {
        throw std::invalid_argument("Original price must be greater than zero.");
    }
    if (actualPrice < 0) {
        throw std::invalid_argument("Actual price cannot be negative.");
    }

    // Calculate the discount
    double discountAmount = originalPrice - actualPrice;
    double discountPercentage = (discountAmount / originalPrice) * 100;

    // Return the discount percentage, rounded to two decimal places
    return std::round(discountPercentage * 100.0) / 100.0;
}

int main() {
    try {
        double originalPrice = 100.0; // Example original price
        double actualPrice = 75.0;     // Example actual price paid
        double discount = calculateDiscount(originalPrice, actualPrice);
        
        std::cout << std::fixed << std::setprecision(2) << "Discount Percentage: " << discount << "%" << std::endl;
    } catch (const std::invalid_argument &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}