#include<iostream>
#include<cmath>
#include<cstring>

using namespace std;

int main () {
    int a[5] = {1,2,3,4,5};
    int pos;
    cin >> pos;
    for(int i = 5; i > pos; i--){
        a[i] = a[i-1];
    }
    a[pos] = 6;
    for (int i = 0; i < 6; i++) {
        cout << a[i] << " ";
    }
    return 0;
}