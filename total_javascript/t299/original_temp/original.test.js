
/* function created using chatGPT */
function calculateAge(birthDateString) {
    if (!birthDateString || isNaN(Date.parse(birthDateString))) {
        return '';
    }
    var today = new Date();
    var birthDate = new Date(birthDateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var monthDifference = today.getMonth() - birthDate.getMonth();
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return birthDateString + ' (' + age + ')';
}


// Function to run test.js samples and check results
function runTests() {
    const testSamples = [
        { input: '2000-08-23', expected: '2000-08-23 (24)' }, // Sample 1: Birthday today, should be 24 years old
        { input: '1990-01-15', expected: '1990-01-15 (34)' }, // Sample 2: Birthday has passed this year, should be 34 years old
        { input: '1985-12-31', expected: '1985-12-31 (38)' }, // Sample 3: Birthday at the end of the year, should be 38 years old
        { input: '2023-05-05', expected: '2023-05-05 (1)' }, // Sample 4: Recently turned 1 year old this year
        { input: 'invalid-date', expected: '' },              // Sample 5: Invalid date input should return an empty string
    ];

    testSamples.forEach((sample, index) => {
        const result = calculateAge(sample.input);
        const isCorrect = result === sample.expected;

        console.log(`Test ${index + 1}:`);
        console.log(`Input: ${sample.input}`);
        console.log(`Expected: ${sample.expected}`);
        console.log(`Result: ${result}`);
        console.log(`Test Passed: ${isCorrect}`);
        console.log('-------------------------------');
    });
}

// Execute the tests
runTests();
