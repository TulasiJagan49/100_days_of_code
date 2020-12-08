import java.util.Scanner;

public class CheckPermutation {

    public static boolean checkPermutation(String s1, String s2) {
        if (s1.length() != s2.length())
            return false;
        int[] arr = new int[128];
        int n = s1.length();
        for (int i = 0; i < n; i++) {
            arr[s1.charAt(i)]++;
            arr[s2.charAt(i)]--;
        }

        for (int i = 0; i < 128; i++) {
            if (arr[i] != 0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.next();
        String s2 = sc.next();
        System.out.println(checkPermutation(s1, s2));
        sc.close();
    }
}