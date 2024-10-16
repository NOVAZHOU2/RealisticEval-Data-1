describe('convFlags Test Cases', () => {
    test('convFlags(0x0000001F) should return "FFFFFFE0"', () => {
        expect(convFlags(0x0000001F)).toBe("FFFFFFE0");
    });

    test('convFlags(0x00000015) should return "FFFFFFEA"', () => {
        expect(convFlags(0x00000015)).toBe("FFFFFFEA");
    });

    test('convFlags(0xFFFFFFFF) should return "0"', () => {
        expect(convFlags(0xFFFFFFFF)).toBe("0");
    });

    test('convFlags(0x12345678) should return "EDCBA987"', () => {
        expect(convFlags(0x12345678)).toBe("EDCBA987");
    });

    test('convFlags(0x00000001) should return "FFFFFFFE"', () => {
        expect(convFlags(0x00000001)).toBe("FFFFFFFE");
    });

    test('convFlags(0x00000003) should return "FFFFFFFC"', () => {
        expect(convFlags(0x00000003)).toBe("FFFFFFFC");
    });

    test('convFlags(0x00000008) should return "FFFFFFF7"', () => {
        expect(convFlags(0x00000008)).toBe("FFFFFFF7");
    });

    test('convFlags(0xABCDEF01) should return "543210FE"', () => {
        expect(convFlags(0xABCDEF01)).toBe("543210FE");
    });
});