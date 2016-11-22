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
    int iters;
};


struct Settings
{
    bool verbose;
    int  iters;
};


struct Instance
{
    vector<bool>    gates;
    int             initialChoice;
    int             revealGate;
    bool            shouldSwap;
};


double getPercentValue(int val, int total)
{
    double ratio = double(val) / double(total);
    return ratio * 100.0f;
}


void initRandomGenerator()
{
    time_t tm = time(nullptr);
    unsigned int seed = static_cast<unsigned int>(tm);
    srand(seed);
}


int random(int beg, int end)
{
    int range = (end - beg + 1);
    int base = rand() % range;
    return base + beg;
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
        settings.iters = -1;
        settings.verbose = false;
        return settings;
    }
    
    istringstream parser(argv[1]);
    Settings settings;

    int iters = 0;
    string verbose;    

    parser >> iters;
    verbose = argv[2];

    settings.iters = iters;
    settings.verbose = (verbose == "print");

    return settings;
}


string stattostr(int stat, int total, const string& msg)
{
    ostringstream oss;
    oss << msg << ": " << stat << " [ " << getPercentValue(stat, total) << "% ]";
    return oss.str();
}


void printStats(const Statistics& stats, bool header = true)
{
    if (header)
    {
        cout << "---------------------" << endl
             << "     STATISTICS      " << endl
             << "---------------------" << endl;
    }

    cout << stattostr(stats.withSwap, stats.swaps, "success swap") << endl
         << stattostr(stats.withoutSwap, stats.iters - stats.swaps, "success no swap") << endl
         << stattostr(stats.swaps, stats.iters, "number of swaps") << endl;
}


void run(Settings& settings, Statistics& stats)
{
 
    for (int iter = 0; iter < settings.iters; ++iter)
    {
        Instance inst = randomInstance();
        int result = simulate(inst, stats) ? 1 : 0;

        if (settings.verbose)
        {
            cout << inst << " --> " << result << endl;
        }
    }    
}


int main(int argc, char* argv[])
{
    initRandomGenerator();

    Settings settings = parseArgs(argc, argv);
    Statistics stats = {0, 0, 0, 0};
    stats.iters = settings.iters;

    run(settings, stats);

    printStats(stats);
    return 0;
}


