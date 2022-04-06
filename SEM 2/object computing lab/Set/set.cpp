#include"set.h"
#include<iostream>
using namespace std;
Set::Set()
{
    count=0;
}
void Set::add(int k)
{
    this->s[count]=k;
    this->count++;
}
int Set::remove(int k)
{
    int f=0;
    for(int i=0;i<this->count;i++)
    {
        if(k==s[i])
        {
            f=1;
            for(int j=i;j<this->count;j++)
            {
                s[j]=s[j+1];
            }
            this->count--;
        }
    }
    return f;
}
void Set::displaySet()
{
    cout<<"The set is : {";
    for(int i=0;i<this->count;i++)
    {
        cout<<s[i]<<",";
    }
    cout<<"}"<<endl;
}
Set Set::operator |(Set s2)
{
    Set r;
    int c;
    if(this->count>s2.count)
    {
        c=this->count;
    }
    else if(s2.count>this->count)
    {
        c=s2.count;
    }
    else
    {
        c=this->count;
    }
    for(int i=0;i<c;i++)
    {
        if(c==this->count)
        {
            r.s[r.count]=this->s[i];
            r.count++;
        }
        else
        {
            r.s[r.count]=s2.s[i];
            r.count++;
        }
    }
    for(int i=0;i<c;i++)
    {
        if(c==this->count)
        {
            if(s2.s[i]!=this->s[i])
            {
                r.s[r.count]=s2.s[i];
                r.count++;
            }
        }
        else
        {
            if(this->s[i]!=s2.s[i])
            {
                r.s[r.count]=this->s[i];
                r.count++;
            }
        }
    }
    return r;
}
Set Set::operator &(Set s2)
{
    Set r;
    for(int i=0;i<this->count;i++)
    {
        if(this->s[i]==s2.s[i])
        {
            r.s[r.count]=this->s[i];
            r.count++;
        }
    }
    return r;
}
