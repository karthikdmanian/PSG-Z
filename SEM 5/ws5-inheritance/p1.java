import java.util.Date;

class Customer{
    String name;
    boolean member;
    String memberType;

    public Customer() {
    }

    public Customer(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public boolean isMember(){
        return this.member;
    }

    public void setMember(boolean member) {
        this.member = member;
    }

    public String getMemberType() {
        return memberType;
    }

    public void setMemberType(String memberType) {
        this.memberType = memberType;
    }

    @Override
    public String toString() {
        return "Customer{" +
                "name='" + name + '\'' +
                ", member=" + member +
                ", memberType='" + memberType + '\'' +
                '}';
    }
}

class Visit extends Customer{
    Date date;
    double serviceExpense;
    double productExpense;

    public Visit(String name) {
        super(name);
    }

    @Override
    public String getName() {
        return super.getName();
    }

    public double getServiceExpense() {
        return serviceExpense;
    }

    public void setServiceExpense(double serviceExpense) {
        this.serviceExpense = serviceExpense;
    }

    public double getProductExpense() {
        return productExpense;
    }

    public void setProductExpense(double productExpense) {
        this.productExpense = productExpense;
    }

    public double getTotalExpense(){
        return serviceExpense+productExpense;
    }

    @Override
    public String toString() {
        return "Visit{" +
                "date=" + date +
                ", serviceExpense=" + serviceExpense +
                ", productExpense=" + productExpense +
                ", name='" + name + '\'' +
                '}';
    }
}



public class p1 {
    public static void main(String[] args) {
        Visit v1 = new Visit("Kennedy");
        System.out.print(v1.toString());
    }
}
