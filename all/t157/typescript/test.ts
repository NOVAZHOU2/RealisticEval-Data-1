describe('bytesToSize', () => {

    test('should convert bytes to KB correctly', () => {
        // @ts-ignore
        expect(bytesToSize(1024)).toBe('1.00 KB');
        // @ts-ignore
        expect(bytesToSize(2048)).toBe('2.00 KB');
    });

    test('should convert bytes to MB correctly', () => {
        // @ts-ignore
        expect(bytesToSize(1048576)).toBe('1.00 MB');
        // @ts-ignore
        expect(bytesToSize(2097152)).toBe('2.00 MB');
    });

    test('should convert bytes to GB correctly', () => {
        // @ts-ignore
        expect(bytesToSize(1073741824)).toBe('1.00 GB');
        // @ts-ignore
        expect(bytesToSize(2147483648)).toBe('2.00 GB');
    });

    test('should convert bytes to TB correctly', () => {
        // @ts-ignore
        expect(bytesToSize(1099511627776)).toBe('1.00 TB');
        // @ts-ignore
        expect(bytesToSize(2199023255552)).toBe('2.00 TB');
    });
});
