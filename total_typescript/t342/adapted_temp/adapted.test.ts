describe('parseMarkdownTitles', () => {
    test('should correctly parse a single heading', () => {
        const markdown = '# Heading 1';
        const expected = [{title: 'Heading 1', sub: []}];
        expect(parseMarkdownTitles(markdown)).toEqual(expected);
    });

    test('should correctly parse multiple headings at the same level', () => {
        const markdown = '# Heading 1\n# Heading 2';
        const expected = [
            {title: 'Heading 1', sub: []},
            {title: 'Heading 2', sub: []}
        ];
        expect(parseMarkdownTitles(markdown)).toEqual(expected);
    });

    test('should correctly parse nested headings', () => {
        const markdown = '# Heading 1\n## Subheading 1.1\n## Subheading 1.2';
        const expected = [
            {
                title: 'Heading 1', sub: [
                    {title: 'Subheading 1.1', sub: []},
                    {title: 'Subheading 1.2', sub: []}
                ]
            }
        ];
        expect(parseMarkdownTitles(markdown)).toEqual(expected);
    });

    test('should handle headings with inconsistent nesting', () => {
        const markdown = '# Heading 1\n## Subheading 1.1\n### Subheading 1.1.1';
        const expected = [
            {
                title: 'Heading 1', sub: [
                    {
                        title: 'Subheading 1.1', sub: [
                            {title: 'Subheading 1.1.1', sub: []}
                        ]
                    }
                ]
            }
        ];
        expect(parseMarkdownTitles(markdown)).toEqual(expected);
    });

    test('should correctly parse a complex nested structure with mixed headings', () => {
        const markdown = '# Heading 1\n## Subheading 1.1\n### Sub-subheading 1.1.1\n#### Sub-sub-subheading 1.1.1.1\n## Subheading 1.2';
        const expected = [
            {
                title: 'Heading 1', sub: [
                    {
                        title: 'Subheading 1.1', sub: [
                            {
                                title: 'Sub-subheading 1.1.1', sub: [
                                    {title: 'Sub-sub-subheading 1.1.1.1', sub: []}
                                ]
                            }
                        ]
                    },
                    {title: 'Subheading 1.2', sub: []}
                ]
            }
        ];
        expect(parseMarkdownTitles(markdown)).toEqual(expected);
    });
});

interface MarkdownTitleExtractResult {
    title: string;
    sub: MarkdownTitleExtractResult[];
}

function parseMarkdownTitles(markdown: string): MarkdownTitleExtractResult[] {
    const lines = markdown.split('\n').filter(line => line.trim() !== '');
    const titles: MarkdownTitleExtractResult[] = [];
    const currentContext: (MarkdownTitleExtractResult | null)[] = [null, null, null, null];

    lines.forEach(line => {
        line = line.trim();
        const match = line.match(/^(#{1,4}) (.*)/);

        if (match) {
            const level = match[1].length; // Level is determined by the number of '#'
            const title = {title: match[2], sub: []};

            if (level === 1) {
                titles.push(title);
            } else {
                // Find the nearest upper-level context
                for (let i = level - 2; i >= 0; i--) {
                    if (currentContext[i]) {
                        currentContext[i]!.sub.push(title);
                        break;
                    }
                }
            }

            // Update the current context for this level and clear deeper levels
            currentContext[level - 1] = title;
            currentContext.fill(null, level); // Clear all deeper contexts
        }
    });

    return titles;
}