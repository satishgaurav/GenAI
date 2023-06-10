#include <iostream>
#include <string>


// std::string myCppFunction(int input) {
//     // Your existing C++ code here
//     // You can use the input argument and perform your computations
    
//     // Example computation
//     int result = input * 2;
    
//     // Convert the result to a string
//     std::string output = std::to_string(result);
    
//     // Return the output string
//     return output;
// }

// // Interface function to be called from Python
// extern "C" {
//     const char* invokeCppFunction(int input) {
//         std::string result = myCppFunction(input);
//         return result.c_str();
//     }
// }


#include <iostream>

extern "C" {
    int cppMainWrapper(int argc, char** argv) {
        // Execute the original command
        // Modify the command according to your needs
        std::string command = "examples/command/command.cpp";
        for (int i = 1; i < argc; i++) {
            command += " ";
            command += argv[i];
        }
        int result = system(command.c_str());
        return result;
    }
}
