#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

class Note {
public:
    static std::string transpose(const std::string& note, const std::string& interval) {
        // Define the musical scale and intervals
        const std::unordered_map<std::string, int> noteMap = {
            {"C", 0}, {"C#", 1}, {"Db", 1}, {"D", 2}, {"D#", 3}, {"Eb", 3},
            {"E", 4}, {"F", 5}, {"F#", 6}, {"Gb", 6}, {"G", 7}, {"G#", 8},
            {"Ab", 8}, {"A", 9}, {"A#", 10}, {"Bb", 10}, {"B", 11}
        };

        // Transpose by perfect fifth (P5) which is 7 half steps
        int steps = 7;

        auto it = noteMap.find(note);
        if (it == noteMap.end()) {
            throw std::invalid_argument("Invalid note");
        }

        int newNoteIndex = (it->second + steps) % 12;
        for (const auto& pair : noteMap) {
            if (pair.second == newNoteIndex) {
                return pair.first;
            }
        }

        throw std::runtime_error("Failed to transpose note");
    }
};

std::vector<std::string> createCircleOfFifths(const std::string& startingNote) {
    std::string currentNote = startingNote;  // Initialize with the starting note
    std::vector<std::string> circle;          // Start the circle

    // Start with the initial note
    circle.push_back(currentNote);

    // Loop to generate the next 11 notes in the circle
    for (int i = 0; i < 11; i++) {
        // Transpose the current note up by a perfect fifth (P5)
        currentNote = Note::transpose(currentNote, "P5");
        circle.push_back(currentNote);  // Add the transposed note to the circle
    }

    return circle;  // Return the full Circle of Fifths
}