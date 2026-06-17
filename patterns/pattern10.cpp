//diamond star pattern vertical
#include<iostream>
using namespace std;
void pattern10(int n){
    for (int i =1;i<=2*n-1;i++){
        
        for(int j=1;j<=i;j++){
            if (i>n){
                break;
            }
            cout<<"*";
    
        }
        if (i>n){
            for(int k=2*n-1;k>=i;k--){
                cout<<"*";
            }
        }
        cout<<endl;
    }
    //or
    //it just i
    for (int i =1;i<=2*n-1;i++){
        int star=i;
        if(i>n) star=2*n-i;
        for(int j=1;j<=star;j++){
            cout<<"*";
        }        cout<<endl;
    }

}

int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern10(n);
    return 0;
}