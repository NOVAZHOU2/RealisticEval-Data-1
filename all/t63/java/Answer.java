package org.real.temp;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class Answer {

    /**
     * Converts a DataFrame (represented as a List of Lists) to a Markdown file.
     * 
     * @param data The data represented as a List of Lists, where each inner list represents a row.
     * @param columns The column names of the DataFrame.
     * @param mdPath The path to the Markdown file to write to.
     * @return The generated Markdown string.
     */
    public static String dataframeToMarkdown(List<List<String>> data, List<String> columns, String mdPath) {
        StringBuilder markdown = new StringBuilder();

        // Construct the header row
        markdown.append("| ").append(String.join(" | ", columns)).append(" |\n");

        // Construct the separator row
        String separator = "| " + String.join(" | ", new String[columns.size()]) + " |\n";
        separator = separator.replace(" ", "---");
        markdown.append(separator);

        // Build markdown table body
        for (List<String> row : data) {
            markdown.append("| ").append(String.join(" | ", row)).append(" |\n");
        }

        // Write markdown to file
        try (FileWriter writer = new FileWriter(mdPath)) {
            writer.write(markdown.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }

        return markdown.toString();
    }

    public static void main(String[] args) {
        // Example usage
        List<List<String>> data = List.of(
            List.of("1", "2", "3"),
            List.of("4", "5", "6")
        );
        List<String> columns = List.of("Column1", "Column2", "Column3");
        String mdPath = "output.md";

        String markdown = dataframeToMarkdown(data, columns, mdPath);
        System.out.println(markdown);
    }
}