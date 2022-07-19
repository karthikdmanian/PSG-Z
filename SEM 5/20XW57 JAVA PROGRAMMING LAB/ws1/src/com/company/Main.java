//package com.company;
//
//public class Main {
//
//    public static void main(String[] args) {
//	    System.out.println("Hello World");
//    }
//}

package com.company;
//
//import java.io.*;
//
//public class Main {
//
//    public static void main(String[] args){
//        double speed=0,eff=0,radius=0;
//
//
//        BufferedReader input = new BufferedReader (new InputStreamReader(System.in));
//        System.out.println("Enter the speed of the turbine:");
//        try{
//            String inputString = input.readLine();
//            speed = Double.parseDouble ( inputString );
//        }catch (IOException e){
//            System.out.println("exception");
//        }
//
//
//
//
//        //getting efficiency
//        System.out.println("Enter the efficiency of the turbine (0..1):");
//        try{
//            String inputString1 = input.readLine();
//            eff = Double.parseDouble(inputString1);
//        }catch (IOException e){
//            System.out.println("exception");
//        }
//
//
//        //getting radius
//        System.out.println("Enter the radius of the turbine:");
//        try{
//            String inputString2 = input.readLine();
//            radius = Double.parseDouble(inputString2);
//        }catch (IOException e){
//            System.out.println("exception");
//        }
//
//
//        //Area of the circle covered by the turbine
//        double pi = 3.14159265359;
//        double area = pi*Math.pow(radius,2);
//
//        //calculating power
//        double maxPower = 0.5*1.2*area*Math.pow(speed,3);
//        System.out.println("The maximum power is L "+maxPower);
//        System.out.println("The actual power is  L"+maxPower*eff);
//    }
//}

//import java.io.*;
//
//public class Main {
//
//    public static void main(String[] args){
//        double mass = 0;
//        int age = 0;
//        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
//        System.out.println("Enter the mass of the tree (per yr) : ");
//        try{
//            String inputString = input.readLine();
//            mass = Double.parseDouble(inputString);
//        }catch (IOException e){
//            System.out.println("Exception");
//        }
//
//        //getting tree age
//        System.out.println("Enter the age of the tree:");
//        try{
//            String inputstring2 = input.readLine();
//            age = Integer.parseInt(inputstring2);
//        }catch(IOException e){
//            System.out.println("Exception");
//        }
//
//        System.out.println("You've entered a mass of"+ mass +"and an age of " + age +"years");
//
//        for(int i=age; i<age+10;i++){
//            System.out.printf("At age %d years, the appx height of the tree is %.2f\n",i,Math.pow(i*mass,0.25));
//        }
//    }
//}

//import java.io.*;
//
//public class Main{
//
//    public static void main(String[] args){
//        int currentvol=0,finalvol=0,keypresses=0;
//        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
//        //inputs
//        try{
//            String inputstring = input.readLine();
//            String[] arr = inputstring.split(" ");
//            currentvol = Integer.parseInt(arr[0]);
//            finalvol = Integer.parseInt(arr[1]);
//        }catch(IOException e){
//            System.out.println("Exception");
//        }
//
//        System.out.printf("the current vol is %d the volume required is %d",currentvol,finalvol);
//
//        //how can this be done?
//    }
//}

//import java.io.*;
//
//public class Main{
//
//    public static void main(String[] args){
//        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
//        int[] initialscore;
//        int[] finalscore;
//        initialscore = new int[2];
//        finalscore = new int[2];
//
//        try{
//            String inputstring = input.readLine();
//            String[] arr=inputstring.split(" ");
//            initialscore[0]=Integer.parseInt(arr[0]);
//            initialscore[1]=Integer.parseInt(arr[1]);
//        }catch(IOException e){
//            System.out.println("exc");
//        }
//
//        try{
//            String inputstring = input.readLine();
//            String[] arr=inputstring.split(" ");
//            finalscore[0]=Integer.parseInt(arr[0]);
//            finalscore[1]=Integer.parseInt(arr[1]);
//        }catch(IOException e){
//            System.out.println("exc");
//        }
//
////        System.out.printf("the initial score is %d:%d",initialscore[0],initialscore[1]);
//
//        if(initialscore[0]>finalscore[0] || initialscore[1]>finalscore[1]){
//            System.out.println("IMPOSSIBLE");
//        }
//        else{
//            System.out.println("POSSIBLE");
//        }
//    }
//}

import java.io.*;

public class Main {
    public static void main(String[] args){
        int friends=0;
        int lshoes=0;

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        try{
            String inputstring = input.readLine();
            String[] arr = inputstring.split(" ");
            friends = Integer.parseInt(arr[0]);
            lshoes = Integer.parseInt(arr[1]);
        }catch (IOException e){
            System.out.println("exec");
        }

        int toBuy=0;
        if(lshoes>friends){
            toBuy = friends;
        }else{
            toBuy = friends*2-lshoes;
        }

        System.out.println(toBuy);
    }
}

//6th prob
//import java.util.Scanner;
//
//public class Main{
//
//    public static void main(String[] args){
//        Scanner input = new Scanner(System.in);
//        System.out.println("enter the no of hours worked");
//        String inputstring = input.nextLine();
//        int hrs= Integer.parseInt(inputstring);
//        System.out.println("Enter the basic pay");
//        String inputstring1= input.nextLine();
//        double bp = Double.parseDouble(inputstring1);
//
//        if(hrs<40){
//            System.out.printf("the salary is %f", hrs*bp);
//        }
//        else if(hrs>40 && hrs<=60){
//            double bonus;
//            if(1.5*bp<8){
//                bonus=8;
//            }
//            else{
//                bonus=1.5*bp;
//            }
//            System.out.printf("The salaray is %f", 40*bp+(hrs-40)*bonus);
//        }
//        else{
//            System.out.println("Error hrs greater than 60");
//        }
//
//    }
//}
//public class Main {
//    public static void main(String[] args) {
//        System.out.printf("%d",(3521/1000));
//    }
//}