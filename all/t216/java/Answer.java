package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Answer {

    /**
     * Retrieve the local IP address from the specified network interface.
     *
     * @param interfaceName The network interface to query. Default is 'wlan0'.
     * @return The local IP address, or throw an exception indicating no IP was found.
     * @throws RuntimeException If the process execution encounters an error or if no suitable IP is found.
     */
    public static String getLocalIp(String interfaceName) {
        String defaultInterface = "wlan0";
        interfaceName = (interfaceName == null || interfaceName.isEmpty()) ? defaultInterface : interfaceName;

        try {
            // Execute the command to get the IP addresses from the specified interface
            ProcessBuilder pb = new ProcessBuilder("ip", "addr", "show", interfaceName);
            Process process = pb.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder output = new StringBuilder();

            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            int exitCode = process.waitFor();
            if (exitCode != 0) {
                throw new RuntimeException("Failed to retrieve IP address: Exit code " + exitCode);
            }

            // Regular expression to match IPv4 addresses, excluding the loopback address
            Pattern ipPattern = Pattern.compile("inet (\\d+\\.\\d+\\.\\d+\\.\\d+)/\\d+");
            Matcher matcher = ipPattern.matcher(output.toString());

            // Find the first valid IP address
            while (matcher.find()) {
                return matcher.group(1); // Return the first valid IP found
            }
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException("Failed to retrieve IP address: " + e.getMessage());
        }

        throw new RuntimeException("No local IP found");
    }

    // Example usage
    public static void main(String[] args) {
        try {
            System.out.println(getLocalIp("wlan0"));
        } catch (RuntimeException e) {
            System.err.println(e.getMessage());
        }
    }
}