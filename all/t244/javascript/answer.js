function methodArgTypeCheck(methodObj, ...args) {
    // Get the string representation of the function
    let funcStr = methodObj.toString();

    // Extract the parameters from the function string
    let paramsMatch = funcStr.match(/\((.*?)\)/);
    if (!paramsMatch) throw new Error('Invalid function format');
    let params = paramsMatch[1].split(',').map(param => param.trim());

    // Check each argument against its expected type
    params.forEach((param, index) => {
        let arg = args[index];

        // Ignore undefined or null arguments
        if (arg === undefined || arg === null) return;

        // Determine the expected type based on the parameter name
        let expectedType = 'any';
        if (/^\w+$/.test(param)) {
            expectedType = param;
        } else if (/^\w+ \?\=/.test(param)) {
            expectedType = param.split(' ')[0];
        }

        // Check if the actual type matches the expected type
        if (typeof arg !== expectedType) {
            throw new TypeError(`Argument ${index} must be of type ${expectedType}, but got ${typeof arg}`);
        }
    });
}