#include<iostream>
using namespace std;
void pattern6(int n){
    for (int i =1;i<=n;i++){
        
        for(int j=n;j>=i;j--){
            cout<<n-j+1;
        }        cout<<endl;
    }
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern6(n);
    return 0;
}