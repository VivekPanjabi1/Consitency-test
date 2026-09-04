import java.util.*;

public class UserService {

    private List<String> users = new ArrayList();

    public void addUser(String name) {
        if (name == null)
            return;
        users.add(name);
    }

    public int getCount() {
        return users.size();
    }

    public static void main(String[] args) {
        UserService svc = new UserService();
        svc.addUser("alice");
        svc.addUser("bob");
        System.out.println(svc.getCount());
    }
}
