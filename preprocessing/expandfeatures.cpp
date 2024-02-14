#include <iostream>
#include <fstream>
#include <sstream>
#include <filesystem>
#include <algorithm>
#include <chrono>
#include <string>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

/* returns C(n,k), wrong result if bigger than int32 */
unsigned binom(unsigned n, unsigned k) {
    if (k > n) return 0;
    if (k * 2 > n) k = n-k;
    if (k == 0) return 1;

    int result = n;

    for(int i = 2; i <= k; ++i) {
        result *= (n-i+1);
        result /= i;
    }

    return result;
}


int* combinations(int n, int k) {
    string bitmask(k, 1);
    bitmask.resize(n, 0);
    int size = binom(n, k) * k;
    int* combinations = new int[size];
    int cnt = 0;

    do {
        for (int i=0; i<n; ++i) {
            if (bitmask[i]) {
                combinations[cnt] = i+1;
                cnt++;
            }
        }
    }
    while (prev_permutation(bitmask.begin(), bitmask.end()));

    return combinations;
}


class ExpandFeatures {
    const int CNFS = 5;
    const int COMB = 2;

    public:
    map<string, int> cnfsMap;

    ExpandFeatures(string cnfs, string file, string fileEx) {
        if (cnfs.size() == CNFS) {
            cnfsMap = {
            {"x_or_y" , int(cnfs[0]-'0')},
            {"notx_or_y" , int(cnfs[1]-'0')},
            {"x_or_noty" , int(cnfs[2]-'0')},
            {"notx_or_noty" , int(cnfs[3]-'0')},
            {"x_xor_y" , int(cnfs[4]-'0')},
            };
        }
        else {
            throw runtime_error("Invalid CNFs");
        }

        expandFeatures(file, fileEx);
    }


    int* parseLine(string lineStr, int size) {
        int* line = new int[size];
        string s;
        stringstream ss(lineStr);
        int cnt = 0;

        while (getline(ss, s, ' ')) {
            line[cnt] = stoi(s);
            cnt++;
        }

        return line;
    }


    int countLines(string file) {
        ifstream f(file);
        int numLines = count_if(istreambuf_iterator<char>{f}, {}, [](char c) { return c == '\n'; });
        f.close();

        return numLines;
    }


    int countFeatures(string file) {
        ifstream f(file);
        string lineStr;
        getline(f, lineStr);

        string s;
        stringstream ss(lineStr);
        vector<int> firstLine;

        while (getline(ss, s, ' ')) {
            firstLine.push_back(stoi(s));
        }

        return firstLine.size() - 1;
    }


    void expandFeatures(string file, string fileEx) {
        int numCnfs = count_if(cnfsMap.begin(), cnfsMap.end(), [&](const pair<string, int>& pair) { return pair.second == 1; });
        int numLines = countLines(file);
        int numFeatures = countFeatures(file);
        int* comb = combinations(numFeatures, COMB);
        int size = binom(numFeatures, COMB);
        ifstream dataset(file);
        ofstream datasetEx(fileEx);
        string lineStr;
        int cnt = 0;
        
        while (getline(dataset, lineStr)) {
            int lineSize = 1 + numFeatures + numCnfs * size;
            int* line = parseLine(lineStr, lineSize);

            for (int i=0; i<size; ++i) {
                int f1 = comb[i*COMB];
                int f2 = comb[i*COMB+1];
                int index = 1 + numFeatures + numCnfs * i;
                int k = 0;

                if (cnfsMap["x_or_y"]) {
                    line[index + k] = line[f1] || line[f2];
                    k++;
                }

                if (cnfsMap["notx_or_y"]) {
                    line[index + k] = !line[f1] || line[f2];
                    k++;
                }

                if (cnfsMap["x_or_noty"]) {
                    line[index + k] = line[f1] || !line[f2];
                    k++;
                }

                if (cnfsMap["notx_or_noty"]) {
                    line[index + k] = !line[f1] || !line[f2];
                    k++;
                }

                if (cnfsMap["x_xor_y"]) {
                    line[index + k] = line[f1] ^ line[f2];
                }
            }
            
            for (int i=0; i<lineSize; ++i) {
                datasetEx << line[i] << ' ';
            }
            
            delete[] line;
            datasetEx << "\n";
            int progress = fmod(float(cnt+1)/float(numLines), 100) * 100;
            float file_size = float(filesystem::file_size(fileEx)) / (1024 * 1024);
            cout << "\r" << "Progress: " << progress << "%" << " | " << "File size: " << file_size << " MiB";
            cout.flush();
            cnt++;
        }
        
        delete[] comb;
        dataset.close();
        datasetEx.close();
    }
};


int main(int argc, char* argv[]) {
    string cnfs;
    string file;
    string fileEx;

    if (argc == 4) {
        cnfs = argv[1];
        file = argv[2];
        fileEx = argv[3];

        if (!filesystem::exists(file)) {
            throw runtime_error("File not found");
        }
    }
    else {
        throw runtime_error("Invalid arguments");
    }
    
    auto start = chrono::steady_clock::now();
    ExpandFeatures(cnfs, file, fileEx);
    auto end = chrono::steady_clock::now();
    
    auto execTime = end - start;

    cout << endl << chrono::duration <double, milli> (execTime).count() << " ms" << endl;

    return 0;
}
