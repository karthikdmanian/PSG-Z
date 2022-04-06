#ifndef POINT_H_INCLUDED
#define POINT_H_INCLUDED
class Point
{
    private:
    int x_co;
    int y_co;
    public:
    int count;
    Point();
    Point(int x,int y);
    Point operator +(Point);
    void disp();
    bool isOrigin();
};


#endif // POINT_H_INCLUDED
