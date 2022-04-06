#include<math.h>
#include"point.h"
#include<iostream>
using namespace std;
Point::Point(float x,float y)
{
    this->x_co=x;
    this->y_co=y;
}
int Point::isOrigin(Point p)
{
    if(p.x_co==0&&p.y_co==0)
        return 0;
    else
        return 5;
}
float Point::distance(Point p)
{
    float d=pow(pow((p.x_co-this->x_co),2)+pow((p.y_co-this->y_co),2),0.5);
    return d;
}
float Point::mulByInt(int k,Point p)
{
    int c=k;
    float nx=k*p.x_co;
    float ny=k*p.x_co;
    p.display(nx,ny,c);
}
void Point::display(float x,float y,int c)
{
    if(c!=1)
        cout<<"The value after multiplying ("<<this->x_co<<"and"<<this->y_co<<") with"<<c<<"is"<<x<<y<<endl;
    else
        cout<<"The sum is ("<<x<<","<<y<<")"<<endl;
}
float Point::add(Point p)
{
    float sx=p.x_co+this->x_co;
    float sy=p.y_co+this->y_co;
    p.display(sx,sy,1);
}
int Point::checkQuad(Point p)
{
    if(p.x_co==0&&p.y_co==0)
        return 0;
    else if(p.x_co==0&&p.y_co!=0)
        return 20;
    else if(p.x_co!=0&&p.y_co==0)
        return 10;
    else if(p.x_co>0&&p.y_co>0)
        return 1;
    else if(p.x_co<0&&p.y_co>0)
        return 2;
    else if(p.x_co<0&&p.y_co<0)
        return 3;
    else if(p.x_co>0&&p.y_co<0)
        return 4;
}
