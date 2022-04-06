#ifndef SET_H_INCLUDED
#define SET_H_INCLUDED



#endif // SET_H_INCLUDED
class Set
{
    int s[100];
    int count;
    public:
    Set();
    void add(int);
    void displaySet();
    int remove(int);
    Set operator |(Set);
    Set operator &(Set);
};
