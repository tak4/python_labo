#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include "sample154_generated.h"

using namespace MySample::Sample154;

int main(int argc, char *argv[]) {
    if (argc <= 1) {
        std::cerr << "Error!!!" << std::endl;
        return 1;
    }

    std::string bin_filename = argv[1];
    std::cout << bin_filename << std::endl;

    std::ifstream file(bin_filename, std::ios::binary | std::ios::ate);
    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<uint8_t> buffer(size);
    if (!file.read(reinterpret_cast<char*>(buffer.data()), size)) {
        std::cerr << "Error reading file!" << std::endl;
        return 1;
    }

    std::cout << "Hex Representation: ";
    for (uint8_t byte : buffer) {
        std::cout << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(byte) << ' ';
    }
    std::cout << std::endl;

    auto verifier = flatbuffers::Verifier(buffer.data(), buffer.size());
    if (!verifier.VerifyBuffer<TopTable>()) {
        std::cerr << "Failed to verify buffer" << std::endl;
        return 1;
    }

    auto toptable = GetTopTable(buffer.data());
    auto struct1 = toptable->struct1();
    if (!struct1) {
        std::cerr << "Error deserializing FlatBuffers: Table1 is null" << std::endl;
        return 1;
    }

    // std::cout << struct1 << std::endl;

    try {
        const flatbuffers::Array<Struct2, 3> *s = struct1->struct2();
        std::cout << s[0].sint32() << std::endl;
        
    } catch (const std::exception &e) {
        std::cerr << "Error deserializing FlatBuffers: " << e.what() << std::endl;
        std::cerr << "Buffer size: " << buffer.size() << std::endl;
    }

    return 0;
}
