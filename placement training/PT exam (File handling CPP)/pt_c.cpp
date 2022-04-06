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

    inFile.open("CP.txt");

    while(!(inFile.eof())){
        //take="";

        inFile>> take;
        /*while((getc(inFile)>="A" && getc(inFile)<="Z") || (getc(inFile)>="a" && getc(inFile)<="z") ){
            take[i]=getc(inFile);
        }*/

        //cout<<take<<"\n";
        if(take==s){
            i=1;
            break;
        }
    }

    inFile.close();

    //cout<<"the no of occurance of "<<s<<" is:"<<i<<" times.";

    if(i==0){
        cout<<"the word "<<s<<"does not exist in the file!"<<endl<<"the value returned is ="<<i;
    }
    else if(i==1){
        cout<<"the word "<<s<<"does exist in the file!"<<endl<<"the value returned is ="<<i;
    }


    return 0;
}

