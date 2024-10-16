/**
 * Parses the first line of an HTTP request response string.
 *
 * This function extracts the HTTP method, request URL, and HTTP version
 * from the given response string. The first line of the response should
 * be formatted as "METHOD URL HTTP/VERSION", followed by a CRLF sequence
 * (carriage return and line feed). If the first line does not conform
 * to this format, the function will return an empty object.
 *
 * @param {string} response - A string containing the HTTP response. It is expected
 *                            to start with a request line that includes the method,
 *                            URL, and HTTP version, ending with CRLF ("\r\n").
 *
 * @return {Object} An object containing three key-value pairs:
 *                  - "method": The HTTP method (e.g., GET, POST).
 *                  - "url": The requested URL (e.g., /index.html).
 *                  - "http_version": The HTTP version (e.g., HTTP/1.1).
 *                  If the request line is malformed or empty, the object may contain
 *                  empty strings or be empty.
 *
 * @note The function does not validate the correctness of the HTTP method,
 *       URL, or version; it only parses the input string.
 */
function parseHttpRequestLine(response) {}