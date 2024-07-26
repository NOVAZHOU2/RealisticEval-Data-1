//This code is generated by chatGPT-3.5
function generateCombinations(map: Map<string, number[]>): number[][] {
    const keys = Array.from(map.keys());
    const values = Array.from(map.values());
  
    const combinations: number[][] = [];
  
    function generate(currentCombination: number[], currentIndex: number): void {
      if (currentIndex === keys.length) {
        combinations.push(currentCombination.slice());
        return;
      }
  
      const currentKey = keys[currentIndex];
      const currentValues = values[currentIndex];
  
      for (const value of currentValues) {
        currentCombination[currentIndex] = value;
        generate(currentCombination, currentIndex + 1);
      }
    }
  
    generate([], 0);
    return combinations;
  }