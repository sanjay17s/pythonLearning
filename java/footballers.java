package java;
import java.util.ArrayList;
import java.util.List;

public class footballers {
    public static void main(String[] args) {
        List<String> footballers = new ArrayList<>();
        footballers.add("Messi");
        footballers.add("Ronaldo");
        footballers.add("Maradona");
        footballers.add(0,"neymar");
       String removed =  footballers.remove(0);
       System.out.println(removed);
      //  System.out.println(footballers);

        
    }
}
