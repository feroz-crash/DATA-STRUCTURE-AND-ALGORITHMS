#include<iostream>
using namespace std;
void pattern15(int n){
    for (int i = n; i >=1; i--)
    {
        /* code */
        for (char j='A'; j <'A' + i; j++)
        {
            /* code */
            cout<<j<<" ";
        }
        cout<<endl;
    }
    
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern15(n);
    return 0;
}