#include <iostream>
#include "set.h"
using namespace std;

int main()
{
    Set s1,s2;
    s1.add(1);
    s1.add(2);
    s1.add(3);
    s2.add(2);
    s2.add(3);
    s1.displaySet();
    s2.displaySet();
    int f=s1.remove(2);
    if(f==0)
    {
        cout<<"The specified ele doesnt exi"<<endl;
    }
    else if(f==1)
    {
        cout<<"The elt is removed "<<endl;
    }
    s1.displaySet();
    Set U=s1|s2;
    Set IN=s1&s2;
    cout<<"The union is "<<endl;
    U.displaySet();
    cout<<"The intersection is"<<endl;
    IN.displaySet();
    return 0;
}
