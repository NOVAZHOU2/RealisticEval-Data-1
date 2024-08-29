describe('computePi', () => {
    test('should calculate pi to 5 decimal places correctly', () => {
        const digits = 5;
        const expected = '3.14159';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 10 decimal places correctly', () => {
        const digits = 10;
        const expected = '3.1415926536';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 15 decimal places correctly', () => {
        const digits = 15;
        const expected = '3.141592653589793';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 20 decimal places correctly', () => {
        const digits = 20;
        const expected = '3.14159265358979323846';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 30 decimal places correctly', () => {
        const digits = 30;
        const expected = '3.141592653589793238462643383280';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });
});
import {Decimal} from 'decimal.js'

/**
 * This code isn't totally correct! But for the sake of the example, it's good enough.
 * (Generated by ChatGPT)
 *
 * @param {number} digits
 */
export function computePi(digits) {
  Decimal.set({precision: digits + 2})

  const one = new Decimal(1)
  const two = new Decimal(2)
  const four = new Decimal(4)

  let a = one
  let b = one.dividedBy(new Decimal(2).sqrt())
  let t = one.dividedBy(new Decimal(4))
  let p = one

  for (let i = 0; i < digits + 5; i++) {
    let a_next = a.plus(b).dividedBy(two)
    let b_next = a.times(b).sqrt()
    let t_next = t.minus(p.times(a.minus(a_next).pow(2)))
    let p_next = p.times(two)

    a = a_next
    b = b_next
    t = t_next
    p = p_next
  }

  const pi = a.plus(b).pow(2).dividedBy(t.times(4))
  return pi.toFixed(digits)
}