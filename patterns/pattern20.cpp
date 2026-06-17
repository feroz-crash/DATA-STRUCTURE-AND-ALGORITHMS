/*Pattern - 20: Symmetric-Butterfly Pattern*/
#include<iostream>
using namespace std;
void pattern20(int n){
    int space=2*n-2;
    int star;
    for (int i = 1; i <=2*n-1; i++)
    {
        if(i>n){
            star=2*n-i;
        }else{
            star=i;
        }
        for(int j=1; j<=star; j++){
            cout<<"*";
        }
        for(int j=1; j<=space; j++){
            cout<<" ";
        }
        for(int j=1; j<=star; j++){
            cout<<"*";
        }
        if(i<n){
            space-=2;
        }else{
            space+=2;
        }        
        cout<<endl;
    }
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern20(n);
    return 0;
}