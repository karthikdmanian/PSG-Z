import java.util.Scanner;

class Bank{
//    members
    String Name;
    int code;
    String address;
    Account[] acc;
    Atm[] atms;

//    constructor

    public Bank() {
    }

    public Bank(String Name, int code, String address, Account[] acc, Atm[] atms) {
        this.code = code;
        this.address = address;
        this.acc = acc;
        this.Name = Name;
        this.atms = atms;
    }

    //    methods
    void manages(){
        System.out.printf("This %s bank manages the following accounts.\n",Name);

        for (int i = 0; i < acc.length; i++) {
            System.out.println(acc[i].toString());
        }
    }

    void maintains(){
        System.out.printf("This %s bank maintains the following ATMs.\n",Name);

        for (int i = 0; i < atms.length; i++) {
            System.out.println(atms[i].toString());
        }
    }
}
class Atm{
    String location;

    public Atm(String location) {
        this.location = location;
    }

    @Override
    public String toString() {
        return "Atm{" +
                "location='" + location + '\'' +
                '}';
    }
}

class AtmTransaction{
    int transactionID;
    String date;
    String type;
    float postBalance;

    public AtmTransaction() {
    }

    public AtmTransaction(int transactionID, String date, String type,float postBalance) {
        this.transactionID = transactionID;
        this.date = date;
        this.type = type;
        this.postBalance = postBalance;
    }

    @Override
    public String toString() {
        return "AtmTransaction{" +
                "transactionID=" + transactionID +
                ", date='" + date + '\'' +
                ", type='" + type + '\'' +
                ", postBalance=" + postBalance +
                '}';
    }
}
class Customer{
    String name;
    String address;
    String dob;
    long cardNumber;
    int pin;
    Account[] acc; // association

//    constructor
    public Customer(String name, String address, String dob, long cardNumber, int pin, Account[] acc) {
        this.name = name;
        this.address = address;
        this.dob = dob;
        this.cardNumber = cardNumber;
        this.pin = pin;
        this.acc = acc;
    }

    //    method
    boolean verifyPassword(int enteredPin){
        if ( enteredPin == pin){
            return true;
        }
        else{
            return false;
        }
    }

    void hasAccounts(){
        System.out.println("This customer with these details has the following accounts.");
        System.out.println(toString());
        for (int i = 0; i < acc.length; i++) {
            System.out.println(acc[i].toString());
        }
    }
    @Override
    public String toString() {
        return "Customer{" +
                "name='" + name + '\'' +
                ", address='" + address + '\'' +
                ", dob='" + dob + '\'' +
                ", cardNumber=" + cardNumber +
                '}';
    }
}
class Account{
//    members
    int number;
    float balance;

    AtmTransaction t;
//    constructor
    public Account() {
    }

    public Account(int number, float balance) {
        this.number = number;
        this.balance = balance;
    }

    //    getter
    public float getBalance() {
        return balance;
    }

//    methods
    void deposit(float amount){
        balance+=amount;
    }

    void withdraw(float amount){
        if(balance-amount>0){
            balance-=amount;
            System.out.printf("Withdrawal successful current balance is %f",balance);
        }
        else{
            System.out.println("Insufficient Balance.");
        }
    }

    void createTransaction(){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the no. of transactions:");
        int tc = input.nextInt();
        int i =0;
        int tid = 10000;
        AtmTransaction[] tcs = new AtmTransaction[tc];
        while(i<tc){
            System.out.println("Select the option:");
            System.out.printf("1.Deposit\n2.Withdrawal");
            int opt = input.nextInt();
            String option = "";
            if(opt==1){
                option = "Deposit";
                System.out.println("Enter the amount");
                int amt = input.nextInt();
                deposit(amt);

            } else if (opt==2) {
                option = "Withdrawal";
                System.out.println("Enter the amount");
                int amt = input.nextInt();
                withdraw(amt);
            }
            AtmTransaction t1 = new AtmTransaction(tid,"6/9/2022",option,balance);
            tcs[i] = t1;
            tid++;
            i++;
        }

        System.out.println("the transactions");
        for (int j = 0; j < tcs.length; j++) {
            System.out.println(tcs[j].toString());
        }
    }

    @Override
    public String toString() {
        return "Account{" +
                "number=" + number +
                ", balance=" + balance +
                '}';
    }
}
class CurrentAccount extends Account{
    String companyName;

    public CurrentAccount(int number, float balance, String companyName) {
        super(number, balance);
        this.companyName = companyName;
    }

    @Override
    public String toString() {
        return "CurrentAccount{" +
                "companyName='" + companyName + '\'' +
                ", number=" + number +
                ", balance=" + balance +
                '}';
    }
}

public class Catest1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.printf("This is a lab test zzzz \n");

        //bank details
        Account a1 = new Account(12345,0);
        Account a2 = new Account(12346,100);
        Account[] accounts = new Account[2];
        accounts[0] = a1;
        accounts[1] = a2;

        Atm atm1 = new Atm("Peelamedu");
        Atm atm2 = new Atm("Dubai M.road");
        Atm[] atms = new Atm[2];
        atms[0] = atm1;
        atms[1] = atm2;

        Bank b1 = new Bank("SBI",641004,"peelamedu, cbe",accounts,atms);

        //std outs
        b1.manages();
        System.out.println("\n");
        b1.maintains();

        //Customer
        Account acc1  = new Account(00001,150);
        Account acc2  = new CurrentAccount(00002,10000,"DELL enterprises.");
        Account[] accs = new Account[2];
        accs[0] = acc1;
        accs[1] = acc2;
        Customer c1 = new Customer(
                "Regis Mam",
                "peelamedu , cbe",
                "6/9/1987",
                1234567,
                1987,
                accs
            );

        //stdouts
        System.out.println("\n");
        c1.hasAccounts();

        //transaction
        System.out.println("You have entered the atm .");
        System.out.printf("1. For a transaction\n2. Check balance\n enter:");
        int opt = input.nextInt();

        if (opt == 1){
            c1.acc[0].createTransaction();
        } else if (opt ==2) {
            System.out.println(c1.acc[0].toString());
        }
        else {
            System.out.println("You have violated the rules for selecting the options.");
        }

    }
}
