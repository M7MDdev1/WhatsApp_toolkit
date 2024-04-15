#include <iostream>
#include <fstream>
#include <string>
#include <Windows.h>


using namespace std;

void press_mention(){
    keybd_event(VK_SHIFT, 0, 0, 0); // Press shift key
    keybd_event(0x32, 0, 0, 0); // Press 2 key
    keybd_event(0x32, 0, KEYEVENTF_KEYUP, 0); // Release 2 key
    keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP, 0); // Release shift key
}

void press_Down(){
        // Simulate pressing down arrow key
    keybd_event(VK_DOWN, 0, 0, 0);

    // Simulate releasing the key
    keybd_event(VK_DOWN, 0, KEYEVENTF_KEYUP, 0);

}

void press_Enter(){
        // Simulate pressing down arrow key
    keybd_event(VK_RETURN, 0, 0, 0);

    // Simulate releasing the key
    keybd_event(VK_RETURN, 0, KEYEVENTF_KEYUP, 0);

}

int ReadFromFile(){
        string file_path = "../arg.txt";

    // Open the text file
    ifstream file(file_path);

    // Check if the file is opened successfully
    if (!file.is_open()) {
        cerr << "Failed to open file: " << file_path << endl;
        
    }

    // Read the file line by line and print each line
    string line;
    while (getline(file, line)) {
        cout << line << endl;
    }

    // Close the file
    file.close();
    return stoi(line);
}


int main(){
    int members_no = ReadFromFile();
// cout << "how many members are there? : ";
// cin >> members_no;
    Sleep(3 * 1000);
    
    for(int i = 0; i < members_no - 1; i++){
    cout << i + 1<< endl;
    press_mention();
    for(int j = 0;j < i;j++ ){
        press_Down();
        Sleep(1);
    }
        press_Enter();
    }
}