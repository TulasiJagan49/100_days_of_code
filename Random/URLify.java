import java.util.Scanner;

public class URLify {

    public static char[] url(char[] arr, int trueLength) {
        int spacecount = 0;
        int index = 0;
        for (int i = 0; i < trueLength; i++) {
            if (arr[i] == ' ')
                spacecount++;
        }
        index = trueLength + spacecount * 2;
        if (trueLength < arr.length)
            arr[trueLength] = '\0';
        for (int i = trueLength - 1; i >= 0; i--) {
            if (arr[i] == ' ') {
                arr[index - 1] = '0';
                arr[index - 2] = '2';
                arr[index - 3] = '%';
                index = index - 3;
            } else {
                arr[index - 1] = arr[i];
                index--;
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int i = Integer.parseInt(sc.nextLine());
        System.out.println(url("Mr John Smith      ".toCharArray(), 13));
        sc.close();
    }
}