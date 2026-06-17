/*Pattern-14: Increasing Letter Triangle Pattern
Problem Statement: Given an integer N, print the following pattern :*/
#include<iostream>
using namespace std;
void pattern14(int n){
    char ch='A';
    for (int i =1;i<=n;i++){
        
        for(char ch='A';ch<='A'+i;ch++){
            cout<<ch<<" ";

        }        cout<<endl;
    }
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern14(n);
    return 0;
}