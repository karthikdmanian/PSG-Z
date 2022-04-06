#include<iostream>
#include"time.h"
using namespace std;
Time::Time(int h,int m,int s)
{
    hr=h;
    min=m;
    sec=s;
}
void Time::printTime()
{
    cout<<"The current time is "<<hr<<"hours and "<<min<<" minutes "<<sec<<" seconds."<<endl;
}
Time Time::operator +(Time t)
{
    Time ts(0,0,0);
    ts.hr=this->hr+t.hr;
    ts.min=this->min+t.min;
    ts.sec=this->sec+t.sec;
    return ts;
}
int Time::operator <(Time t)
{
    if(this->hr>t.hr)
    {
        return 0;
    }
    else if(t.hr>this->hr)
    {
        return 1;
    }
    else if(t.hr==this->hr)
    {
        if(this->min>t.min)
        {
            return 0;
        }
        else if(t.min>this->min)
        {
            return 1;
        }
        else if(t.min==this->min)
        {
            if(this->sec>t.sec)
            {
                return 0;
            }
            else if(t.sec>this->sec)
            {
                return 1;
            }
            else
            {
                return 2;
            }
        }
    }
}
