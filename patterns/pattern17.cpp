/*Pattern-17: Alpha-Hill Pattern
Problem Statement: Given an integer N, print the following pattern :*/
#include<iostream>
using namespace std;
void pattern17(int n){
    for (int i = 1; i <=n; i++)
    {
            
        for (int j=1; j <=n-i; j++)
        {

            cout<<" ";
        }
        char ch='A';
        int breakPoint=(2*i+1)/2;
        for (int k=1; k <=2*i-1; k++)
        {

            cout<<ch;
            if (k<breakPoint)
            {
    
                ch++;
            }
            else{
                ch--;
            }
        }
        for (int j=1; j <=n-i; j++)
        {

            cout<<" ";
        }
        cout<<endl;
    }
    
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern17(n);
    return 0;
}