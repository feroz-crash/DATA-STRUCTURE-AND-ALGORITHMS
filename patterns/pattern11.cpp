#include<iostream>
using namespace std;
void pattern11(int n){
    for (int i =2;i<=n+1;i++){
        
        for(int j=1;j<i;j++){
            cout<<(i-j)%2;
        }        cout<<endl;
    }
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern11(n);
    return 0;
}