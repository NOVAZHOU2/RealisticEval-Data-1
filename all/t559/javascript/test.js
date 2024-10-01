describe('isCppHeaderFile', () => {
    test('returns true for a .h file', () => {
        expect(isCppHeaderFile('example.h')).toBe(true);
    });

    test('returns true for a .hpp file', () => {
        expect(isCppHeaderFile('example.hpp')).toBe(true);
    });

    test('returns true for a .hh file', () => {
        expect(isCppHeaderFile('example.hh')).toBe(true);
    });

    test('returns true for a .hxx file', () => {
        expect(isCppHeaderFile('example.hxx')).toBe(true);
    });

    test('returns false for a non-header file extension', () => {
        expect(isCppHeaderFile('example.txt')).toBe(false);
    });

    test('returns false for a file without an extension', () => {
        expect(isCppHeaderFile('example')).toBe(false);
    });

    test('returns false for a .c file', () => {
        expect(isCppHeaderFile('example.c')).toBe(false);
    });

    test('returns true for a .H file (uppercase)', () => {
        expect(isCppHeaderFile('example.H')).toBe(true);
    });
});