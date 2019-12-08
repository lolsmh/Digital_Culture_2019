#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ifstream in("dict"); //входной файл
    ofstream out("dictout"); //выходной файл
    vector<string> dict; //динамический массив строк, в котором будем хранить слова
    string s1; //инициализация строки для считывания
    while (in) { //пока ввод
        in >> s1; //вводится строка
        int n = s1.length(); //переменная для хранения длинны строки
        int k = 0;
        while (k < n) { //метод перевода заглавных букв в строчные
            s1[k] = tolower(s1[k]);
            k++;
        }
        if (s1 != "-") { //если строка не "-"
            for (int i = 0; i < n; i++) {//с шагом в 1 посимвольно идем по строке
                if (s1[i] == '.' || s1[i] == ',' || s1[i] == ';' || s1[i] == ':' || s1[i] == '!' || s1[i] == '?' ||
                    s1[i] == '(' || s1[i] == ')' || s1[i] == '?') { //если находим символ, удаляем его
                    for (int j = i; j < n; j++) { //переписываем часть строки после символа
                        s1[j] = s1[j + 1];
                    }
                }
            }
            dict.push_back(s1); //вставляем в вектор
        }
    }
    dict.erase(dict.begin() + dict.size() - 1, dict.begin() + dict.size()); //редактируем погрешность метода in
    for (const auto &i : dict) { //переписываем слова с исправленными ошибками в файл
        out << i << endl;
    }
    return 0;
}



