/**
 * Simple Hello World example demonstrating a compliant greeting service.
 * This class provides a greeting without using System.out in library code.
 */
public class HelloWorld {
    /**
     * Return the greeting message in uppercase.
     *
     * @return the uppercase greeting string
     */
    public String getGreeting() {
        String greeting = "Hello, World!";
        return greeting.toUpperCase();
    }
}
