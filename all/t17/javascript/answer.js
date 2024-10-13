function haversineDistance(lat1, lon1, lat2, lon2) {
    /**
     * Calculate the distance between two points on the Earth using the Haversine formula.
     *
     * @param {number} lat1 - Latitude of the first point in degrees.
     * @param {number} lon1 - Longitude of the first point in degrees.
     * @param {number} lat2 - Latitude of the second point in degrees.
     * @param {number} lon2 - Longitude of the second point in degrees.
     * @returns {number} Distance between the two points in kilometers.
     */
    // Radius of the Earth in kilometers
    const R = 6371.0;

    // Convert latitude and longitude from degrees to radians
    const lat1Rad = (lat1 * Math.PI) / 180;
    const lon1Rad = (lon1 * Math.PI) / 180;
    const lat2Rad = (lat2 * Math.PI) / 180;
    const lon2Rad = (lon2 * Math.PI) / 180;

    // Differences in coordinates
    const dlat = lat2Rad - lat1Rad;
    const dlon = lon2Rad - lon1Rad;

    // Haversine formula
    const a = Math.sin(dlat / 2) ** 2 + Math.cos(lat1Rad) * Math.cos(lat2Rad) * Math.sin(dlon / 2) ** 2;
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    // Distance in kilometers
    const distance = R * c;

    return distance;
}