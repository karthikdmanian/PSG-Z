import java.lang.*;
import java.util.*;

public class Stack {
    public static void main(String[] args) {
        StackOfIntegers soi1 = new StackOfIntegers(2);
        soi1.push(1);
        soi1.push(2);
        System.out.println(soi1.elements.toString());
    }
}

class StackOfIntegers {
    public int[] elements;
    private int size;

    public StackOfIntegers() {

    }
    public StackOfIntegers(int capacity) {
        this.elements = new int[capacity];
        this.size = capacity;
    }

    public boolean empty() {
        if (this.size == 0) {
            return true;
        }
        return false;
    }

    public int peek() {
        return this.elements[this.size-1];
    }

    public void push(int element) {
        this.elements = Arrays.copyOf(this.elements, this.size+1);
        this.elements[this.size-1] = element;
    }

    public int pop() {
        int popped = this.peek();
        this.elements = Arrays.copyOf(this.elements, this.size-1);
        return popped;
    }

    public int getSize() {
        return this.size;
    }
}
