#include <iostream>

using namespace std;

long long factorial (unsigned long long n){
    if(n == 0) return 1;
    else return n * factorial(n-1);
}

int main()
{
    unsigned long long n;
    
    while(1){
        cin >> n;
        cout<<factorial(n)<<endl;
    }

    return 0;
}
