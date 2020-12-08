import java.util.Scanner;

public class IsUnique {

    public static boolean isUniqueChars(final String str) {
        if (str.length() > 128)
            return false;
        boolean[] charSet = new boolean[128];
        for (int i = 0; i < str.length(); i++) {
            int charVal = str.charAt(i);
            if (charSet[charVal]) {
                return false;
            }
            charSet[charVal] = true;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(isUniqueChars(str));
        sc.close();
    }
}