/*
    Copyright (c) 2016 - buyuk.dev@gmail.com
    ----------------------------------------
    Simulation for Monty Hall problem.
    https://en.wikipedia.org/wiki/Monty_Hall_problem
*/


#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <ctime>


using namespace std;



struct Statistics
{
    int withSwap;
    int withoutSwap;
    int swaps;
};


struct Settings
{
    bool verbose;
    int  itersnum;
};


struct Instance
{
    vector<bool>    gates;
    int             initialChoice;
    int             revealGate;
    bool            shouldSwap;
};


void initializeRandom()
{
    srand(static_cast<unsigned int>(time(0)));
}


int random(int beg, int end)
{
    return rand() % (end-beg+1) + beg;
}


int revealRandom(const Instance& inst)
{
    vector<int> opts;
    for (int i = 0; i < inst.gates.size(); ++i)
    {
        if (inst.initialChoice != i && false == inst.gates[i])
        {
            opts.push_back(i);
        }
    }
    return opts[ random(0, opts.size()-1) ];
}


int swapChoice(const Instance& inst)
{
    if (!inst.shouldSwap)
    {
        return inst.initialChoice;
    }

    for (int i = 0; i < inst.gates.size(); ++i)
    {
        if (i != inst.initialChoice && i != inst.revealGate)
        {
            return i;
        }
    }
}


Instance randomInstance()
{
    Instance inst;

    inst.gates.resize(3, false);
    inst.gates[ random(0, 2) ] = true;

    inst.initialChoice = random(0, 2);
    inst.revealGate = revealRandom(inst);
    inst.shouldSwap = static_cast<bool>(random(0, 1));

    return inst;
}


ostream& operator<<(ostream& os, const Instance& inst)
{
    os << "{ [ ";
    for (bool v: inst.gates)
    {
        os << (v ? 1 : 0);
    }
    os << " ] swap: " << inst.shouldSwap ? "T" : "F";
    os << ", init: " << inst.initialChoice;
    os << ", rev: " << inst.revealGate ? "T" : "F";
    os << " }";

    return os;
}


bool simulate(const Instance& inst, Statistics& stats)
{
    int choice = swapChoice(inst);
    int& counter = inst.shouldSwap ? stats.withSwap : stats.withoutSwap;
    
    if (inst.shouldSwap)
    {
        stats.swaps ++;
    }

    if (inst.gates[choice])
    {
        counter ++;
        return true;
    }

    return false;
}


Settings parseArgs(int argc, char* argv[])
{
    if (argc < 3)
    {
        Settings settings;
        settings.itersnum = -1;
        settings.verbose = false;
        return settings;
    }
    
    istringstream parser(argv[1]);
    Settings settings;

    int itersnum = 0;
    string verbose;    

    parser >> itersnum;
    verbose = argv[2];

    settings.itersnum = itersnum;
    settings.verbose = (verbose == "print");

    return settings;
}


int main(int argc, char* argv[])
{
    initializeRandom();

    Settings settings = parseArgs(argc, argv);
    cout << "---------------------" << endl;
    cout << "       SETTINGS      " << endl;
    cout << "---------------------" << endl;
    cout << "verbose: " << (settings.verbose ? "true" : "false") << endl;
    cout << "number of iterations: " << settings.itersnum << endl;

    Statistics stats = {0, 0};

    for (int iter = 0; iter < settings.itersnum; ++iter)
    {
        auto inst = randomInstance();
        int result = simulate(inst, stats) ? 1 : 0;
        if (settings.verbose)
        {
            cout << inst << " --> " << result << endl;
        }
    } 

    cout << "---------------------" << endl;
    cout << "       SUMMARY       " << endl;
    cout << "---------------------" << endl;
    cout << "success with swap: " << stats.withSwap << endl;
    cout << "success without swap: " << stats.withoutSwap << endl;
    cout << "number of swaps: " << stats.swaps << endl;
    cout << "---------------------" << endl;
    cout << "percent with swap: " << (double(stats.withSwap) / double(stats.swaps) * 100.0f) << endl;
    cout << "percent without swap: " << (double(stats.withoutSwap) / double(settings.itersnum - stats.swaps) * 100.0f) << endl;
    cout << "percent of swaps: " << (double(stats.swaps) / double(settings.itersnum) * 100.0f) << endl;
    

    return 0;
}


