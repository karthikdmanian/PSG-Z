package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        System.out.println("Hello");

        Scanner myObj = new Scanner(System.in);

        System.out.println("Enter Username:");

        String username = myObj.nextLine();
        System.out.println("Vamos "+ username);

    }
}
