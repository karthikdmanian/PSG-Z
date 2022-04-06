#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int main(){

    ifstream inFile;
    string s;
    int i=0;
    string take;
    cout<<"enter the string to be searched?";
    cin>>s;

    inFile.open("dummy.txt");

    while(!(inFile.eof())){
        //take="";

        inFile>> take;
        /*while((getc(inFile)>="A" && getc(inFile)<="Z") || (getc(inFile)>="a" && getc(inFile)<="z") ){
            take[i]=getc(inFile);
        }*/

        //cout<<take<<"\n";
        if(take==s){
            i++;
        }
    }

    inFile.close();

    cout<<"the no of occurance of "<<s<<" is:"<<i<<" times.";



    return 0;
}
