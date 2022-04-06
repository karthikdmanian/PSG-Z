#ifndef TIME_H_INCLUDED
#define TIME_H_INCLUDED



#endif // TIME_H_INCLUDED
class Time
{
    int hr,min,sec;
    public:
    Time(int,int,int);
    void printTime();
    Time operator +(Time);
    int operator <(Time);
};
