#include<iostream>
using namespace std;
void pattern16(int n){
    char ch='A';
    for (int i = 1; i <=n; i++)
    {
        /* code */
        for (int j=1; j <=i ; j++)
        {
            /* code */
            cout<<ch<<" ";
        }
        ch++;
        cout<<endl;
    }
    
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern16(n);
    return 0;
}