/**
 * Simple Hello World example.
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

    /**
     * Main entry point.
     *
     * @param args command-line arguments
     */
    public static void main(String[] args) {
        HelloWorld app = new HelloWorld();
        System.out.println(app.getGreeting());
    }
}
