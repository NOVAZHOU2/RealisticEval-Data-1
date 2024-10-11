describe('findNthWeekdayOfSpecificYear', () => {
    it('should return the correct date for the nth weekday of a specific year', () => {
      expect(findNthWeekdayOfSpecificYear(2023, 4, 1, 0)).toEqual(new Date(2023, 3, 3)); // April 3, 2023 (Monday)
      expect(findNthWeekdayOfSpecificYear(2023, 4, 2, 0)).toEqual(new Date(2023, 3, 10)); // April 10, 2023 (Monday)
      expect(findNthWeekdayOfSpecificYear(2023, 4, 3, 0)).toEqual(new Date(2023, 3, 17)); // April 17, 2023 (Monday)
      expect(findNthWeekdayOfSpecificYear(2023, 4, 4, 0)).toEqual(new Date(2023, 3, 24)); // April 24, 2023 (Monday)
      expect(findNthWeekdayOfSpecificYear(2023, 4, 5, 0)).toEqual(new Date(2023, 3, 31)); // April 31, 2023 (Monday)
  
      expect(findNthWeekdayOfSpecificYear(2023, 4, 1, 6)).toEqual(new Date(2023, 3, 30)); // April 30, 2023 (Sunday)
      expect(findNthWeekdayOfSpecificYear(2023, 4, 2, 6)).toEqual(new Date(2023, 3, 23)); // April 23, 2023 (Sunday)
      expect(findNthWeekdayOfSpecificYear(2023, 4, 3, 6)).toEqual(new Date(2023, 3, 16)); // April 16, 2023 (Sunday)
      expect(findNthWeekdayOfSpecificYear(2023, 4, 4, 6)).toEqual(new Date(2023, 3, 9)); // April 9, 2023 (Sunday)
      expect(findNthWeekdayOfSpecificYear(2023, 4, 5, 6)).toEqual(new Date(2023, 3, 2)); // April 2, 2023 (Sunday)
    });
  
    it('should return the last occurrence of the weekday if the nth occurrence does not exist', () => {
      expect(findNthWeekdayOfSpecificYear(2023, 2, 1, 0)).toEqual(new Date(2023, 1, 27)); // February 27, 2023 (Monday)
      expect(findNthWeekdayOfSpecificYear(2023, 2, 2, 0)).toEqual(new Date(2023, 1, 27)); // February 27, 2023 (Monday)
      expect(findNthWeekdayOfSpecificYear(2023, 2, 3, 0)).toEqual(new Date(2023, 1, 27)); // February 27, 2023 (Monday)
      expect(findNthWeekdayOfSpecificYear(2023, 2, 4, 0)).toEqual(new Date(2023, 1, 27)); // February 27, 2023 (Monday)
      expect(findNthWeekdayOfSpecificYear(2023, 2, 5, 0)).toEqual(new Date(2023, 1, 27)); // February 27, 2023 (Monday)
    });
  });