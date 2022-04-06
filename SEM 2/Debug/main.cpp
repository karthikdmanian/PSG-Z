	#include <iostream>

using namespace std;

class A
{
public:
int *i;
A(int *j = new int(0))
                {
                   i = j;
                }
};

void newval(A &a)
{
int i = *a.i;
a.i = &(++i);
}
int main()
{
        A a;
a.i = 0;
if (a.i)
        {
newval(a);
        }
cout<< *a.i;
return 0;

}
