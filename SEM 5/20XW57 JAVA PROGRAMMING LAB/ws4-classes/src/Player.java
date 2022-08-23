public class Player {
    String name;
    int age;
    String country;

//    getters and setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public Player(String name, int age, String country) {
        this.name = name;
        this.age = age;
        this.country = country;
    }

    public Player() {
//        default constructor goes here
    }

    public String toString(){
        return "Name:"+this.name+"Age:"+this.age;
    }

}

class Main{
    public static void main(String[] args) {
        Player p1 = new Player();
        Player p2 = new Player("Messi",34,"Argentina");
        System.out.println(p2.toString());
    }
}