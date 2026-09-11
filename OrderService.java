import java.util.HashMap;
import java.util.Map;

/**
 * Service for managing customer orders and calculating totals.
 */
public class OrderService {

    private Map<String, Integer> orders = new HashMap<>();

    /**
     * Add an order with the given ID and quantity.
     *
     * @param id  the order identifier
     * @param qty the order quantity
     */
    public void addOrder(String id, int qty) {
        if (qty < 0) {
            return;
        }
        orders.put(id, qty);
    }

    /**
     * Return the total quantity across all orders.
     *
     * @return the sum of all order quantities
     */
    public int getTotal() {
        int total = 0;
        for (Integer qty : orders.values()) {
            total += qty;
        }
        return total;
    }

    /**
     * Main entry point for demonstration.
     *
     * @param args command-line arguments
     */
    public static void main(String[] args) {
        final int qty1 = 5;
        final int qty2 = 10;
        final int qty3 = 15;
        final int qty4 = 20;

        OrderService svc = new OrderService();
        svc.addOrder("A1", qty1);
        svc.addOrder("A2", qty2);
        svc.addOrder("A3", qty3);
        svc.addOrder("A4", qty4);
        System.out.println(svc.getTotal());
    }
}
