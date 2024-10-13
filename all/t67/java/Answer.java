package org.real.temp;

import java.io.File;
import java.util.HashMap;
import java.util.Map;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class Answer {

    /**
     * Parse a XAML file and extract key-value pairs from 'String' elements.
     *
     * @param xamlFile Path to the XAML file.
     * @return A map containing the key-value pairs extracted from 'String' elements.
     */
    public static Map<String, String> parseXamlToDict(String xamlFile) {
        try {
            // Parse the XAML file
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(new File(xamlFile));
            doc.getDocumentElement().normalize();

            // Map to hold the key-value pairs
            Map<String, String> resultMap = new HashMap<>();

            // Iterate through all 'String' elements in the XAML file
            NodeList stringElements = doc.getElementsByTagName("String");
            for (int i = 0; i < stringElements.getLength(); i++) {
                Element element = (Element) stringElements.item(i);
                String key = element.getAttribute("Key");
                if (!key.isEmpty()) {
                    String value = element.getTextContent();
                    resultMap.put(key, value == null ? "" : value.trim());
                }
            }

            return resultMap;

        } catch (ParserConfigurationException | SAXException | java.io.IOException e) {
            System.out.println("Error parsing the XAML file: " + e.getMessage());
            return new HashMap<>();
        } catch (NullPointerException e) {
            System.out.println("Error: The file " + xamlFile + " does not exist.");
            return new HashMap<>();
        }
    }

    public static void main(String[] args) {
        // Example usage
        Map<String, String> result = parseXamlToDict("path/to/your/xaml/file.xaml");
        result.forEach((key, value) -> System.out.println(key + ": " + value));
    }
}