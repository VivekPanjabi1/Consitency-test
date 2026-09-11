import java.util.HashMap;
import java.util.Map;

/**
 * Service for managing inventory items and stock totals.
 */
public class InventoryService {

    private Map<String, Integer> stock = new HashMap<>();

    /**
     * Add an item to the inventory with the given ID and quantity.
     *
     * @param id  the item identifier
     * @param qty the item quantity
     */
    public void addItem(String id, int qty) {
        if (qty < 0) {
            return;
        }
        stock.put(id, qty);
    }

    /**
     * Return the total quantity across all inventory items.
     *
     * @return the sum of all item quantities
     */
    public int getTotal() {
        int total = 0;
        for (Integer qty : stock.values()) {
            total += qty;
        }
        return total;
    }

    /**
     * Remove an item from the inventory by ID.
     *
     * @param id the item identifier to remove
     */
    public void removeItem(String id) {
        if (stock.containsKey(id)) {
            stock.remove(id);
        }
    }

    /**
     * Main entry point for demonstration.
     *
     * @param args command-line arguments
     */
    public static void main(String[] args) {
        final int qty1 = 5;
        final int qty2 = 10;

        InventoryService svc = new InventoryService();
        svc.addItem("A1", qty1);
        svc.addItem("A2", qty2);
        svc.removeItem("A1");
        System.out.println(svc.getTotal());
    }
}
