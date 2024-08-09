#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct SymbolData
{
    string name;
    string type;
    string size;
    string dimension;
    string line_of_code;
    string line_of_usage;
    string address;
};

vector<SymbolData> symbol_table;

void insert(string name, string type, string size, string dimension, string line_of_code, string line_of_usage, string address)
{
    SymbolData data = {name, type, size, dimension, line_of_code, line_of_usage, address};
    symbol_table.push_back(data); //lambda function that serves as the comparison function for sorting.
    sort(symbol_table.begin(), symbol_table.end(), [](const SymbolData& a, const SymbolData& b)
    {
        return a.name < b.name;
    });
}

void search(string name)
{
    cout << "Index\tName\tType\tSize\tDimension\tLine of Code\tLine of Usage\tAddress\n";
    for (size_t i = 0; i < symbol_table.size(); ++i)
    {
        if (symbol_table[i].name == name)
        {
            cout << i << "\t" << symbol_table[i].name << "\t" << symbol_table[i].type << "\t"
                 << symbol_table[i].size << "\t" << symbol_table[i].dimension << "\t\t"
                 << symbol_table[i].line_of_code << "\t\t" << symbol_table[i].line_of_usage << "\t\t"
                 << symbol_table[i].address << "\n";
            cout << "Data found!\n";
            return;
        }
    }
    cout << "Data not found for name: " << name << "\n";
}

void update(string old_name, string new_name, string old_type, string new_type, string old_size, string new_size,
            string old_dimension, string new_dimension, string old_line_of_code, string new_line_of_code,
            string old_line_of_usage, string new_line_of_usage, string old_address, string new_address)
{
    for (auto& data : symbol_table)
    {
        if (data.name == old_name)
        {
            data.name = new_name;
        }
        if (data.type == old_type)
        {
            data.type = new_type;
        }
        //
    }
}

void deleteData(string name)
{
    for (auto it = symbol_table.begin(); it != symbol_table.end(); ++it)
    {
        if (it->name == name)
        {
            symbol_table.erase(it);
            return;
        }
    }
    cout << "Name not found\n";
}

void show()
{
    cout << "Index\tName\tType\tSize\tDimension\tLine of Code\tLine of Usage\tAddress\n";
    for (size_t i = 0; i < symbol_table.size(); ++i)
    {
        cout << i << "\t" << symbol_table[i].name << "\t" << symbol_table[i].type << "\t"
             << symbol_table[i].size << "\t" << symbol_table[i].dimension << "\t \t"
             << symbol_table[i].line_of_code << "\t \t" << symbol_table[i].line_of_usage << "\t\t"
             << symbol_table[i].address << "\n";
    }
}

int getHashKey(const std::string& name, int st_length) {
    int ascii_value = 0;

    for (char x : name) {
        ascii_value += static_cast<int>(x);  // Convert character to ASCII value
    }

    int hash_key = (ascii_value * name.length()) % st_length;
    return hash_key;
}

int main()
{
    while (true)
    {
        cout << "Press 0 to Exit the program\n";
        cout << "Press 1 to Insert data\n";
        cout << "Press 2 to Search any data\n";
        cout << "Press 3 to Update any data\n";
        cout << "Press 4 to Delete any data\n";
        cout << "Press 5 to Show all data\n";
        cout << "Press 6 to Get Hash Key\n\n";

        int choice;
        cout << "Press -> ";
        cin >> choice;
        cout << "\n";

        if (choice == 0)
        {
            cout << "Exiting the program. Thank you!\n";
            break;
        }

        if (choice == 1)
        {
            int n;
            std::cout << "How many inputs? - ";
            std::cin >> n;
            std::cout << "\n";

            for (int i = 0; i < n; ++i)
            {
                string name, type, address;
                string size, dimension, line_of_code, line_of_usage;
                cout << "Enter Name, Type, Size, Dimension, Line of Code, Line of Usage, Address: ";
                cin >> name >> type >> size >> dimension >> line_of_code >> line_of_usage >> address;
                insert(name, type, size, dimension, line_of_code, line_of_usage, address);
            }
            cout << "Data inserted successfully.\n\n";
        }

        if (choice == 2)
        {
            string name;
            cout << "Enter Name: ";
            cin >> name;
            search(name);
            cout << "\n";
        }

        if (choice == 3)
        {
            string old_name, new_name, old_type, new_type, old_address, new_address;
            string old_size, new_size, old_dimension, new_dimension, old_line_of_code, new_line_of_code, old_line_of_usage, new_line_of_usage;

            cout << "Enter old name: ";
            cin >> old_name;
            cout << "Enter new name: ";
            cin >> new_name;

            cout << "Enter old type: ";
            cin >> old_type;
            cout << "Enter new type: ";
            cin >> new_type;
/*
            cout << "Enter old size: ";
            cin >> old_size;
            cout << "Enter new size: ";
            cin >> new_size;

            cout << "Enter old dimension: ";
            cin >> old_dimension;
            cout << "Enter new dimension: ";
            cin >> new_dimension;

            cout << "Enter old line of code: ";
            cin >> old_line_of_code;
            cout << "Enter new line of code: ";
            cin >> new_line_of_code;

            cout << "Enter old line of usage: ";
            cin >> old_line_of_usage;
            cout << "Enter new line of usage: ";
            cin >> new_line_of_usage;

            cout << "Enter old address: ";
            cin >> old_address;
            cout << "Enter new address: ";
            cin >> new_address;
*/
            update(old_name, new_name, old_type, new_type, old_size, new_size, old_dimension, new_dimension,
                   old_line_of_code, new_line_of_code, old_line_of_usage, new_line_of_usage, old_address, new_address);

            cout << "Data updated successfully.\n\n";
        }

        if (choice == 4)
        {
            string name;
            cout << "Enter Name: ";
            cin >> name;
            deleteData(name);
            cout << "Data deleted successfully.\n\n";
        }

        if (choice == 5)
        {
            show();
            cout << "\n";
        }

        if (choice == 6)
        {
            std::string name;
            int st_length;
            cout << "Enter Name: ";
            cin >> name;
            int hash_key = getHashKey(name, st_length);
            //if (hash_Key != -1)
            {
                std::cout << "Hash key: " << hash_key << std::endl;
            }

            cout << "\n";
        }

        if (choice < 0 || choice > 6)
        {
            cout << "Invalid choice. Please try again.\n\n";
        }
    }

    return 0;
}
