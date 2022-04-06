#include<iostream>
#include"meal.h"
using namespace std;
Meal::Meal()
{
    name="Man";
    cal=180;
}
Meal::Meal(string s,int calo)
{
    name=s;
    cal=calo;
}
void Meal::operator <<(Meal m)
{
    cout<<"Name :"<<m.name<<endl<<"calories:"<<m.cal<<endl;
}
void Meal::operator >>(Meal m)
{
    cout<<"Enter the name :";
    cin>>m.name;
    cout<<"Enter the amount of calories:";
    std::cin.clear();
    cin>>m.cal;
}
