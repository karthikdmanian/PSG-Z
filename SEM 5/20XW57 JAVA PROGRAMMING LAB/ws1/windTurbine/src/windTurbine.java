
import java.io.*;

public class windTurbine {

    public static void main(){
        double speed=0,eff=0,radius=0;


        BufferedReader input = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("Enter the speed of the turbine:");
        try{
            String inputString = input.readLine();
            speed = Double.parseDouble ( inputString );
        }catch (IOException e){
            System.out.println("exception");
        }




        //getting efficiency
        System.out.println("Enter the efficiency of the turbine (0..1):");
        try{
            String inputString1 = input.readLine();
            eff = Double.parseDouble(inputString1);
        }catch (IOException e){
            System.out.println("exception");
        }


        //getting radius
        System.out.println("Enter the radius of the turbine:");
        try{
            String inputString2 = input.readLine();
            radius = Double.parseDouble(inputString2);
        }catch (IOException e){
            System.out.println("exception");
        }


        //Area of the circle covered by the turbine
        double pi = 3.14159265359;
        double area = pi*Math.pow(radius,2);

        //calculating power
        double maxPower = 0.5*1.2*area*Math.pow(speed,3);
        System.out.println("The maximum power is L "+maxPower);
        System.out.println("The actual power is  L"+maxPower*eff);
    }
}
