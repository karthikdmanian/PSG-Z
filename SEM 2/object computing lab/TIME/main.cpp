#include <iostream>
#include "time.h"
using namespace std;

int main()
{
    Time t1(10,10,0),t2(10,0,0);
    Time t3=t1+t2;
    t1.printTime();
    t2.printTime();
    int f=t1<t2;
    if(f==0)
    {
        cout<<"The time T1 is greater"<<endl;
    }
    else if(f==1)
    {
        cout<<"The time T2 is greater"<<endl;
    }
    else if(f==2)
    {
        cout<<"Equal Time"<<endl;
    }
    return 0;
}
