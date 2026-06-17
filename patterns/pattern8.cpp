//reverse star pyramid vertical
#include<iostream>
using namespace std;
void pattern8(int n){
    for (int i =n;i>=1;i--){

        for(int j=n;j>i;j--){
            cout<<" ";
        }  
        for(int k=2*(i)-1;k>=1;k--){
            cout<<"*";
        }
        for(int l=n;l>i;l--){
            cout<<" ";
        }
        cout<<endl;
    } 
}

int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern8(n);
    return 0;
}