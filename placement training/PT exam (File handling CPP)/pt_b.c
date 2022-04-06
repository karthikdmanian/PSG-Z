#include<iostream>
#include<fstream>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

int main(){

    ifstream inFile;
    string s;
    vector<string> strVec;
    //int i=0;
    string take;
    //cout<<"enter the string to be searched?";
    //cin>>s;

    inFile.open("CP.txt");

    while(!(inFile.eof())){

        inFile>> take;

        strVec.push_back(take);

    }

    inFile.close();

    std::sort(strVec.begin(),strVec.end()-1);

    for(int i=0;i<strVec.size()-1;i++){
        cout<<strVec[i]<<endl;
    }

    return 0;
}
