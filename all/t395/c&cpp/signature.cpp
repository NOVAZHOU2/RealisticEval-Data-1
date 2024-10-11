/**
 * Sums up calibration values extracted from the document.
 * Each calibration value is formed by combining the first and last digits of numbers found in each line
 * into a two-digit number.
 *
 * @param calibrationDocument A vector of strings, each representing a line of text.
 * @return The total sum of all calibration values.
 */
int sumCalibrationValues(const std::vector<std::string>& calibrationDocument);