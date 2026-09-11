/**
 * Simple Hello World example.
 */
public class HelloWorld {
    /**
     * Main entry point.
     *
     * @param args command-line arguments
     */
    public String getGreeting() {
        String greeting = "Hello, World!";
        return greeting.toUpperCase();
    }

    public static void main(String[] args) {
        HelloWorld app = new HelloWorld();
        app.getGreeting();
    }
}
