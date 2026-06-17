/*Pattern - 21: Hollow Rectangle Pattern*/
#include<iostream>
using namespace std;
void pattern21(int n){
    for(int i=1; i<=n; i++){
        if(i==1||i==2 || i==n-1||i==n){
            for(int j=1; j<=n; j++){
                cout<<"*";
            }        }else{
            cout<<"**";
            for(int j=1; j<=n-4; j++){
                cout<<" ";

            }
            cout<<"**";
        }
        cout<<endl;
    }
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern21(n);
    return 0;
}