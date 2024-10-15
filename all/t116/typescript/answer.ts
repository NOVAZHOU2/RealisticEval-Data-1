interface Point {
    x: number;
    y: number;
}

function toroidalDiff(thisPoint: Point, otherPoint: Point, width: number, height: number): [number, number] {
    let dx = thisPoint.x - otherPoint.x;
    let dy = thisPoint.y - otherPoint.y;

    // Handle wraparound for the x dimension
    if (Math.abs(dx) > width / 2) {
        dx = dx > 0 ? dx - width : dx + width;
    }

    // Handle wraparound for the y dimension
    if (Math.abs(dy) > height / 2) {
        dy = dy > 0 ? dy - height : dy + height;
    }

    return [dx, dy];
}