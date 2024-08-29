/**
 * 
 * @param {number} debt 
 * @param {number} monthlyInterestRate 
 * @param {number} totalPayments 
 * @returns 
 */
const calculateRemainingPayment = (debt, monthlyInterestRate, totalPayments) => {
  return (debt * monthlyInterestRate) /
    (1 - Math.pow(1 + monthlyInterestRate, -totalPayments));
}

// 重新计算后的测试样例
const testSamples = [
  { principal: 1000, interestRate: 0.01, numberOfPayments: 12, expected: 88.85 },
  { principal: 5000, interestRate: 0.02, numberOfPayments: 24, expected: 264.36 }, // 重新检查后可能需要更新
  { principal: 1500, interestRate: 0.015, numberOfPayments: 36, expected: 54.23 }, // 重新检查后可能需要更新
  { principal: 3000, interestRate: 0.01, numberOfPayments: 60, expected: 66.73 }, // 重新检查后可能需要更新
  { principal: 2500, interestRate: 0.025, numberOfPayments: 48, expected: 90.01 }, // 重新检查后可能需要更新
];

// Function to run tests and determine if they are correct
const runTests = () => {
  testSamples.forEach(sample => {
      const remainingPayment = calculateRemainingPayment(sample.principal, sample.interestRate, sample.numberOfPayments).toFixed(2);
      const isCorrect = Math.abs(remainingPayment - sample.expected) < 0.01; // Allow for minor floating point differences
      const resultString = `Principal: $${sample.principal}, Interest Rate: ${sample.interestRate * 100}%, Payments: ${sample.numberOfPayments}, ` +
                           `Calculated Payment: $${remainingPayment}, Expected: $${sample.expected}, Test Passed: ${isCorrect}`;
      console.log(resultString);
  });
}

// Execute the tests
runTests();
