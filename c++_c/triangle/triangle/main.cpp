//
//  main.cpp
//  triangle
//
//  Created by Vigo Walker on 05-04-22.
//

# include <iostream>
# include <math.h>

using namespace std;

int main(){
    
    int a;
    int b;
    int c;
    
    cout << "Ecrivez un nombre: ";
    cin >> a;
    cout << "Ecrivez un nombre: ";
    cin >> b;
    cout << "Ecrivez un nombre: ";
    cin >> c;
    
    if (a == b or b == c or a == c){
        cout << "Le triangle ABC tel que a = " << a << " b = " << b << " c = " << c << " est icosele ";
    }
    
    return 0;
}
