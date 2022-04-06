#include"point.h"
#include<iostream>
using namespace std;
//int Point::count=0;
Point::Point()
{
    //int Point::count=0;
    count++;
}
Point::Point(int x,int y)
{
    x_co=x;
    y_co=y;
}
bool Point::isOrigin()
{
    if(x_co==0&&y_co==0)
        return true;
    else
        return false;
}
Point Point::operator +(Point p1)
{
    Point s;
    s.x_co=this->x_co+p1.x_co;
    s.y_co=this->y_co+p1.y_co;
    return s;
}
void Point::disp()
{
    cout<<"the added point is ("<<this->x_co<<","<<this->y_co<<")"<<endl;
}
