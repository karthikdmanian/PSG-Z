#include <iostream>
#include "point.h"
using namespace std;

int main()
{
    Point p1(3,2),p2(4,5);
    //cout<<p3.isOrigin();
    //cout<<sizeof(bool);
    Point p3=p1+p2;
    p3.disp();
    return 0;
}
