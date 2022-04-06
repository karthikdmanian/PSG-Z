#include<iostream>
using namespace std;
class ex
{
    int x;
    friend void fun(ex);
    public:
    ex()
    {
        x=1;
    }
};
void fun(ex e)
{
    cout<<e.x;
}
/*ex::ex()
{
    x=1;
}*/
int main()
{
    ex e1;
    fun(e1);
}
