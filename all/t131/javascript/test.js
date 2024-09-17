/**
 * @jest-environment jsdom
 */

let cssRuleExistsForHighlight = false;
describe('checkCSSHighlightAndAdd', () => {
    beforeEach(() => {
        // Reset the global variable and clean up the document head before each test.js
        cssRuleExistsForHighlight = false;
        document.head.innerHTML = '';
    });

    test('should add a new style element with the highlight CSS rule if it does not exist', () => {
        checkCSSHighlightAndAdd();

        // Check that a style element was added to the document head
        const styleElement = document.querySelector('style');
        expect(styleElement).not.toBeNull();

        // Check that the style element contains the correct CSS rule
        expect(styleElement.textContent).toContain('::highlight(search-model_answer_result-highlight)');
        expect(styleElement.textContent).toContain('background-color: yellow;');
        expect(styleElement.textContent).toContain('color: black;');
    });

    test('should set cssRuleExistsForHighlight to true after adding the CSS rule', () => {
        checkCSSHighlightAndAdd();

        // Check that the flag is set to true after the rule is added
        expect(cssRuleExistsForHighlight).toBe(true);
    });

    test('should not add a new style element if the CSS rule already exists', () => {
        cssRuleExistsForHighlight = true;

        checkCSSHighlightAndAdd();

        // Check that no new style element is added
        const styleElements = document.querySelectorAll('style');
        expect(styleElements.length).toBe(0);
    });

    test('should add only one style element even if called multiple times', () => {
        checkCSSHighlightAndAdd();
        checkCSSHighlightAndAdd();  // Call the function again

        // Check that only one style element is present
        const styleElements = document.querySelectorAll('style');
        expect(styleElements.length).toBe(1);
    });

    test('should correctly append the style element to the document head', () => {
        checkCSSHighlightAndAdd();

        // Check that the style element is indeed appended to the head
        const styleElement = document.head.querySelector('style');
        expect(styleElement).not.toBeNull();
        expect(document.head.contains(styleElement)).toBe(true);
    });
});