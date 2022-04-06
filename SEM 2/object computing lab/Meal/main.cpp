#include <iostream>
#include "meal.h"
using namespace std;

int main()
{
    Meal m1("kart",210),m2("radha",187),m3;
    m2<<m1;
    m3<<m2;
    m1>>m2;
    return 0;
}
