/*Pattern-19: Symmetric-Void Pattern*/


#include<iostream>
using namespace std;
void pattern19(int n){
    for (int i = 1; i <2*n; i++)
    {
        int breakPoint=i;
        if (i>n) breakPoint=2*n-i;
        /* code */
        for (int j=n; j >=breakPoint ; j--)
        {
            /* code */
            cout<<"*";
        }
        for (int k=1; k <=2*breakPoint-2 ; k++)
        {
            /* code */
            cout<<" ";
        }
        for (int l=n; l >=breakPoint ; l--)
        {
            /* code */
            cout<<"*";
        }
        
        cout<<endl;
    }
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern19(n);
    return 0;
}