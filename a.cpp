#include <iostream>
using namespace std;

int main() {
    const int DIAS = 7;
    int temperaturas[DIAS];
    int diasMayoresA35 = 0;
    float suma = 0;

    string dias[DIAS] = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"};
    for (int i = 0; i < DIAS; i++) {
        cout << "Digita la temperatura maxima del dia " << dias[i] << ": ";
        cin >> temperaturas[i];
    }

    for (int i = 0; i < DIAS; i++) {
        if (temperaturas[i] > 35) {
            diasMayoresA35++;
        }
        suma += temperaturas[i];
    }

    float promedio = suma / DIAS;

    cout << "Días con temperatura mayor a 35°C: " << diasMayoresA35 << endl;
    cout << "Promedio de temperaturas: " << promedio << "°C" << endl;

    if (promedio > 30) {
        cout << "Semana calurosa" << endl;
    } else {
        cout << "Semana templada" << endl;
    }

    return 0;
}