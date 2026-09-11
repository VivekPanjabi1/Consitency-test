import java.util.*;

public class InventoryService {

    private Map<String, Integer> stock = new HashMap();

    public void addItem(String id, int qty) {
        if (qty < 0)
            return;
        stock.put(id, qty);
    }

    public int getTotal() {
        int total = 0;
        for (Integer qty : stock.values()) {
            total += qty;
        }
        return total;
    }

    public void removeItem(String id) {
        if (stock.containsKey(id)) {
            stock.remove(id);
        }
    }

    public static void main(String[] args) {
        InventoryService svc = new InventoryService();
        svc.addItem("A1", 5);
        svc.addItem("A2", 10);
        svc.removeItem("A1");
        System.out.println(svc.getTotal());
    }
}
