// Sample class that intentionally violates the coding standards.
// Each violation is marked with a '// VIOLATION:' comment.
// Used to test lint / consistency tooling. Do NOT copy this style.

import java.util.*;
import java.util.ArrayList;  // VIOLATION: wildcard import above + duplicate import

public class BadExample {  // VIOLATION: missing class Javadoc

    private int magicNumber = 42;  // VIOLATION: magic number, not a named constant

    public static void main(String[] args) {  // VIOLATION: missing method Javadoc
        if (args.length > 0)
            System.out.println("Hello " + args[0]);  // VIOLATION: missing braces, System.out used

        for (int i = 0; i < 10; i++)  // VIOLATION: missing braces
            System.out.println(i);

        List<String> list = new ArrayList();
        list.add("a"); list.add("b");  // VIOLATION: multiple statements on one line
    }

    public int calculateTotal(int x, int y)  // VIOLATION: missing method Javadoc
    {
        return x + y;  // VIOLATION: brace style (opening brace on new line)
    }
}
// VIOLATION: trailing whitespace and no final newline handling below    
