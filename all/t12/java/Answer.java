package org.real.temp;

import java.util.Map;

public class Answer {
    /*
    * Calculates the Euclidean distance between two agents based on their coordinates in the observations.
    *
    * @param agent1 The string representation of agent1's identifier.
    * @param agent2 The string representation of agent2's identifier.
    * @param observations A map containing observation questions with agent identifiers as keys. Each value is a map with 'x' and 'y' keys representing coordinates.
    * @return The Euclidean distance between the two agents.
    */
    public static double calculateDistance(String agent1, String agent2, Map<String, Map<String, Double>> observations) {
        if (!observations.containsKey(agent1) || !observations.containsKey(agent2)) {
            throw new IllegalArgumentException("One or both agents are not present in the observations.");
        }

        Map<String, Double> agent1Coords = observations.get(agent1);
        Map<String, Double> agent2Coords = observations.get(agent2);

        double x1 = agent1Coords.get("x");
        double y1 = agent1Coords.get("y");

        double x2 = agent2Coords.get("x");
        double y2 = agent2Coords.get("y");

        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }
}