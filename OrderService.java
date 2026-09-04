import java.util.*;

public class OrderService {

    private Map<String, Integer> orders = new HashMap();

    public void addOrder(String id, int qty) {
        if (qty < 0)
            return;
        orders.put(id, qty);
    }

    public int getTotal() {
        int total = 0;
        for (Integer qty : orders.values()) {
            total += qty;
        }
        return total;
    }

    public static void main(String[] args) {
        OrderService svc = new OrderService();
        svc.addOrder("A1", 5);
        svc.addOrder("A2", 10);
        System.out.println(svc.getTotal());
    }
}
