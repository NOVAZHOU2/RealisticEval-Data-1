describe('removePartsOfString', () => {
    it('should return the string without parts before the first uppercase and lowercase letters', () => {
      expect(removePartsOfString('1234AbCde5678')).toBe('AbCde5678');
      expect(removePartsOfString('1234aBcDe5678')).toBe('bCDe5678');
      expect(removePartsOfString('1234ABcDe5678')).toBe('BCDe5678');
      expect(removePartsOfString('1234abcDE5678')).toBe('abcDE5678');
      // Add more test cases as needed
    });
  
    it('should handle empty string correctly', () => {
      expect(removePartsOfString('')).toBe('');
    });
  
    it('should handle single character strings correctly', () => {
      expect(removePartsOfString('A')).toBe('A');
      expect(removePartsOfString('a')).toBe('a');
    });
  
    it('should handle strings with no uppercase or lowercase letters correctly', () => {
      expect(removePartsOfString('1234567890')).toBe('1234567890');
    });
  });