/*Pattern-18: Alpha-Triangle Pattern
Problem Statement: Given an integer N, print the following pattern :*/
#include<iostream>
using namespace std;
void pattern18(int n){
    
    for (int i = n-1; i>=0; i--)
    {
        char ch='A'+i;
        /* code */
        for (int j=n-1; j>i ; j--)
        {
            /* code */
            cout<<ch<<" ";
            ch++;
        }
        cout<<endl;
    }
    
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern18(n);
    return 0;
}