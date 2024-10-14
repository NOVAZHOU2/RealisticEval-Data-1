package org.real.temp;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Comparator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    public static void main(String[] args) {
        renameFiles("path/to/directory");
    }

    /**
     * Renames PNG files in a specified directory by appending a sequence number to each file.
     * The files are sorted alphabetically, and each base name is assigned sequential numbers.
     *
     * @param directory The path to the directory containing PNG files to be renamed.
     */
    public static void renameFiles(String directory) {
        // Convert directory to Path object for easier handling
        Path dirPath = Paths.get(directory);

        if (!Files.isDirectory(dirPath)) {
            throw new IllegalArgumentException("The directory '" + directory + "' does not exist or is not a directory.");
        }

        // Get list of PNG files in the directory
        File[] pngFiles = dirPath.toFile().listFiles((dir, name) -> name.toLowerCase().endsWith(".png"));

        if (pngFiles == null) {
            throw new IllegalArgumentException("No PNG files found in the directory '" + directory + "'.");
        }

        // Sort files alphabetically by their names
        Arrays.sort(pngFiles, Comparator.comparing(File::getName));

        // Print the sorted list of files (for debugging)
        System.out.println("Sorted files:");
        for (File file : pngFiles) {
            System.out.println(file.getName());
        }

        // Rename files with sequence numbers
        String prevBaseName = null;
        int count = 1;

        Pattern pattern = Pattern.compile("(\\d{3})(-\\d)?(?=\\.png$)");

        for (File file : pngFiles) {
            // Extract base name without postfix and number
            String fileName = file.getName();
            String baseName = fileName.substring(0, fileName.lastIndexOf('.'));
            Matcher matcher = pattern.matcher(baseName);
            if (matcher.find()) {
                baseName = matcher.replaceAll("");
            }

            if (!baseName.equals(prevBaseName)) {
                count = 1;
            }

            String newFileName = baseName + String.format("%03d", count) + ".png";
            Path newFilePath = dirPath.resolve(newFileName);

            try {
                Files.move(file.toPath(), newFilePath);
                System.out.println("Renaming " + fileName + " to " + newFileName);
            } catch (IOException e) {
                System.err.println("Failed to rename " + fileName + " to " + newFileName);
                e.printStackTrace();
            }

            prevBaseName = baseName;
            count++;
        }
    }
}
