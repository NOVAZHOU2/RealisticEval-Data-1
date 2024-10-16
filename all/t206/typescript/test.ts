describe('Testing circleIntersectionArea function', () => {
    const tolerance = 1e-5;

    test('No overlap, circles far apart', () => {
        expect(circleIntersectionArea(0.0, 0.0, 3.0, 10.0, 10.0, 3.0)).toBeCloseTo(0.0, 5);
    });

    test('No overlap, circles just touching', () => {
        expect(circleIntersectionArea(0.0, 0.0, 3.0, 6.0, 0.0, 3.0)).toBeCloseTo(0.0, 5);
    });

    test('One circle inside the other', () => {
        const area = circleIntersectionArea(0.0, 0.0, 5.0, 2.0, 0.0, 3.0);
        expect(area).toBeCloseTo(28.2743, 5); // Area of smaller circle
    });

    test('Identical circles, full overlap', () => {
        const area = circleIntersectionArea(0.0, 0.0, 3.0, 0.0, 0.0, 3.0);
        expect(area).toBeCloseTo(28.2743, 5); // Area of one circle
    });
});