//star pyramid vertical
#include<iostream>
using namespace std;
void pattern7(int n){
    for (int i =1;i<=n;i++){
        
        for(int j=n;j>i;j--){
            cout<<" ";
        }  
        for(int k=2*i-1;k>=1;k--){
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
    pattern7(n);
    return 0;
}