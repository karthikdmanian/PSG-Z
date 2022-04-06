//Class Point with Some operations using member function
#include <iostream>
#include "point.h"
using namespace std;
void disp(int);
int main()
{
    Point p1(0,0),p2(3,4);
    int c1=p1.isOrigin(p2);
    int c2=p2.isOrigin(p1);
    disp(c1);
    disp(c2);
    cout<<"The distance is "<<p1.distance(p2)<<" units"<<endl;
    p1.add(p2);
    int f1=p1.checkQuad(p2);
    int f2=p2.checkQuad(p1);
    disp(f1);
    disp(f2);
}
void disp(int ch)
{
    if(ch==10)
        cout<<"THe point lies on X axis"<<endl;
    else if(ch==20)
        cout<<"THe point lies on Y axis"<<endl;
    else if(ch==1||ch==2||ch==3||ch==4)
        cout<<"THe point lies on"<<ch<<"Quadrant"<<endl;
    else if(ch==0)
        cout<<"THe point lies on origin"<<endl;
    else if(ch==5)
        cout<<"THe point does not lie in origin"<<endl;
    if(ch==20)
        cout<<"It lies on Y axis"<<endl;
    else if(ch==10)
        cout<<"It lies on X axis"<<endl;
}
