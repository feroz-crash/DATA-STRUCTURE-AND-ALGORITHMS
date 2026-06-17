//Number Crown Pattern
#include<iostream>
using namespace std;
void pattern12(int n){
    for (int i =n;i>=1;i--){
        
        for(int j=1;j<=n-i+1;j++){
            cout<<j;
        }
        for(int k=2*i-2;k>=1;k--){
            cout<<" ";
        }
        for(int l=n;l>=i;l--){

            cout<<l-i+1;
        }
        cout<<endl;
    
    }
    //or
        // Initial number of spaces in the first row
    int spaces = 2 * (n - 1);
    
    // Outer loop for the number of rows
    for (int i = 1; i <= n; i++) {
        
        // Inner loop to print numbers in increasing order
        for (int j = 1; j <= i; j++) {
            cout << j;
        }
        
        // Inner loop to print spaces in the middle
        for (int j = 1; j <= spaces; j++) {
            cout << " ";
        }
        
        // Inner loop to print numbers in decreasing order
        for (int j = i; j >= 1; j--) {
            cout << j;
        }
        
        // Move to the next line after printing the row
        cout << endl;
        
        // Decrease spaces by 2 after each row
        spaces -= 2;
    }
    
}
int main(){
    int n;
    cout<<"Enter the number of rows: ";
    cin>>n;
    pattern12(n);
    return 0;
}