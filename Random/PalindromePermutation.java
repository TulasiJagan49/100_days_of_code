import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class PalindromePermutation {

    public static boolean check(String str) {
        int n = str.length();
        Map<Character, Integer> map = new HashMap<Character, Integer>();

        for (int i = 0; i < n; i++) {
            map.putIfAbsent(str.charAt(i), 0);
            map.put(str.charAt(i), map.get(str.charAt(i)) + 1);
        }

        int countOddCharacters = 0;
        for (int i : map.values()) {
            if (i % 2 == 1)
                countOddCharacters++;
        }

        return countOddCharacters == 1 ? true : false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next().toLowerCase();
        System.out.println(check(str));
    }
}