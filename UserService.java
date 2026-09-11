import java.util.ArrayList;
import java.util.List;

/**
 * Service for managing application users.
 */
public class UserService {

    private List<String> users = new ArrayList<>();

    /**
     * Add a user by name if the name is not null.
     *
     * @param name the user name to add
     */
    public void addUser(String name) {
        if (name == null) {
            return;
        }
        users.add(name);
    }

    /**
     * Return the number of registered users.
     *
     * @return the user count
     */
    public int getCount() {
        return users.size();
    }

    /**
     * Main entry point for demonstration.
     *
     * @param args command-line arguments
     */
    public static void main(String[] args) {
        UserService svc = new UserService();
        svc.addUser("alice");
        svc.addUser("bob");
        svc.addUser("charlie");
        System.out.println(svc.getCount());
    }
}
