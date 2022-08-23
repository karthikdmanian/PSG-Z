public class Event {
//    attributos
    String name;
    String detail;
    String type;
    String organiser;
    Integer attendeesCount;
    Double projectedExpense;
    static Integer eventCount;

    public void addEvent(Event[] eventArray,Event eventIns){
        eventArray[eventCount]=eventIns;
        eventCount++;
    }

//    public Event[] searchEvents(Event[] eventArray,String type){
//        for (int i = 0; i < eventArray.length; i++) {
//            if(eventArray[i].type==type){
//                return eventArray[i];
//            }
//        }
//        return
//    }

    public void displayAll(Event[] eventArray){
        System.out.println("The details of the events are :");
        for (int i = 0; i < eventArray.length; i++) {
            System.out.println(eventArray[i].detail);
        }
    }

//    getters and setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDetail() {
        return detail;
    }

    public void setDetail(String detail) {
        this.detail = detail;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getOrganiser() {
        return organiser;
    }

    public void setOrganiser(String organiser) {
        this.organiser = organiser;
    }

    public Integer getAttendeesCount() {
        return attendeesCount;
    }

    public void setAttendeesCount(Integer attendeesCount) {
        this.attendeesCount = attendeesCount;
    }

    public Double getProjectedExpense() {
        return projectedExpense;
    }

    public void setProjectedExpense(Double projectedExpense) {
        this.projectedExpense = projectedExpense;
    }

//    constructor

    public Event(String name, String detail, String type, String organiser, Integer attendeesCount, Double projectedExpense) {
        this.name = name;
        this.detail = detail;
        this.type = type;
        this.organiser = organiser;
        this.attendeesCount = attendeesCount;
        this.projectedExpense = projectedExpense;
    }

}

