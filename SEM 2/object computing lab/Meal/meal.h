#ifndef MEAL_H_INCLUDED
#define MEAL_H_INCLUDED
#include<string>


#endif // MEAL_H_INCLUDED
class Meal
{
    std::string name;
    int cal;
    public:
    Meal();
    Meal(std::string,int);
    void operator <<(Meal);
    void operator >>(Meal);
    Meal operator +();
};

