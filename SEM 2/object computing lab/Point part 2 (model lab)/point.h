#ifndef POINT_H_INCLUDED
#define POINT_H_INCLUDED



#endif // POINT_H_INCLUDED
#include<iostream>
using namespace std;
class Point
{
    private:
    float x_co,y_co;
    public:
    Point(float,float);
    int isOrigin(Point);
    float distance(Point);
    float mulByInt(int,Point);
    float add(Point);
    int sub(Point,Point);
    int checkQuad(Point);
    void display(float,float,int);
};
