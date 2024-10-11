describe('canCompleteCircuit', () => {
  it('should return the correct starting gas station\'s index', () => {
    const gas = [1,2,3,4,5];
    const cost = [3,4,5,1,2];
    expect(canCompleteCircuit(gas, cost)).toBe(3);
  });

  it('should return -1 when it cannot complete the circuit', () => {
    const gas = [2,3,4];
    const cost = [3,4,3];
    expect(canCompleteCircuit(gas, cost)).toBe(-1);
  });
});