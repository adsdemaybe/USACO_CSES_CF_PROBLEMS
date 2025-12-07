package Class_Notes;

public class ScopePlay {
    public static void main(String[] args){
        int x = 5;
        {
            x = 10;
            System.out.println(x);
        }
        System.out.println(x);
    }

    
}