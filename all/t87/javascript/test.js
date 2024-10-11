describe('timestampToReadableDate', () => {
    test('should convert UNIX timestamp to readable format', () => {
        const timestamp = 1696516800;
        expect(timestampToReadableDate(timestamp)).toBe('Oct 5, 22:40');
    });

    test('should handle timestamp at the start of the year', () => {
        const timestamp = 1672531200;
        expect(timestampToReadableDate(timestamp)).toBe('Jan 1, 8:00');
    });

    test('should handle timestamp at the end of the year', () => {
        const timestamp = 1672531199;
        expect(timestampToReadableDate(timestamp)).toBe('Jan 1, 7:59');
    });

    test('should handle timestamps in the leap year', () => {
        const timestamp = 1583020800;
        expect(timestampToReadableDate(timestamp)).toBe('Mar 1, 8:00');
    });

    test('should convert timestamp to readable format with single-digit day', () => {
        const timestamp = 1675190400;
        expect(timestampToReadableDate(timestamp)).toBe('Feb 1, 2:40');
    });


    test('should handle zero UNIX timestamp', () => {
        const timestamp = 0;
        expect(timestampToReadableDate(timestamp)).toBe('Jan 1, 8:00');
    });
});