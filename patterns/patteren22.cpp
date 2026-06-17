/*Pattern - 20: Symmetric-Butterfly Pattern*/
#include<iostream>
using namespace std;
void pattern22(int n){
    int top,left,right,bottom,mindist;
    for(int i=0; i<2*n-1; i++){
        for(int j=0; j<2*n-1; j++){
            top=i;
            left=j;
            bottom=2*n-2-i;
            right=2*n-2-j;
            mindist=min(min(top,bottom),min(left,right));
            cout<<n-mindist<<"  ";
        }
        cout<<endl;
    }
}




int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern22(n);
    return 0;
}