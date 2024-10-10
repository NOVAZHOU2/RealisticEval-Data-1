import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static List<String> compareFiles(String file1Path, String file2Path) throws IOException {
        File file1 = new File(file1Path);
        File file2 = new File(file2Path);

        if (!file1.exists() || !file2.exists()) {
            throw new FileNotFoundException("Either one or both of the files do not exist.");
        }

        List<String> lines1 = readLinesFromFile(file1);
        List<String> lines2 = readLinesFromFile(file2);

        return findDifferences(lines1, lines2);
    }

    private static List<String> readLinesFromFile(File file) throws IOException {
        List<String> lines = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }
        }
        return lines;
    }

    private static List<String> findDifferences(List<String> lines1, List<String> lines2) {
        // TODO: Implement difference finding logic here
        return new ArrayList<>(); // Placeholder
    }
}