import { Dictionary, List } from "typescript";

/**
 * Convert strings in nested structures (e.g., dictionaries, arrays) to numbers (integers or floating-point numbers) as much as possible.
 *
 * @param data - The input data before conversion.
 * @returns The converted data.
 */
function convertStringsToNumbers(data: Dictionary<any> | List<any>): Dictionary<any> | List<any> {
    if (typeof data === 'object' && !Array.isArray(data) && data !== null) {
        return Object.entries(data).reduce((acc, [key, value]) => {
            acc[key] = convertStringsToNumbers(value);
            return acc;
        }, {} as Dictionary<any>);
    } else if (Array.isArray(data)) {
        return data.map(item => convertStringsToNumbers(item));
    } else if (typeof data === 'string') {
        try {
            // Try converting to float first, then to int if possible
            const num = parseFloat(data);
            if (!isNaN(num)) {
                if (data.includes('.')) {
                    return num;
                } else {
                    return parseInt(data, 10);
                }
            }
        } catch (error) {
            // Ignore error
        }
    }
    return data; // Return data unchanged if it's not a string
}

// Example usage
const exampleData = {
    name: "John",
    age: "30",
    height: "5.9",
    children: ["Alice", "Bob"],
    nested: {
        inner: "42"
    }
};

console.log(convertStringsToNumbers(exampleData));