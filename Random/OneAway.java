import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class OneAway {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        System.out.println(checkOneAway(a, b));
    }

    private static boolean checkOneAway(String a, String b) {
        if (Math.abs(a.length() - b.length()) > 1)
            return false;

        String s1 = a.length() < b.length() ? a : b;
        String s2 = a.length() < b.length() ? b : a;

        int index1 = 0;
        int index2 = 0;
        boolean foundDifference = false;
        while (index1 < s1.length() && index2 < s2.length()) {
            if (s1.charAt(index1) != s2.charAt(index2)) {
                if (foundDifference)
                    return false;
                foundDifference = true;
                index1++;
            } else {
                index1++;
            }
            index2++;
        }

        return true;
    }

}
