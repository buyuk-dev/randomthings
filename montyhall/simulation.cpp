/*
    Copyright (c) 2016 - buyuk.dev@gmail.com
    ----------------------------------------
    Simulation for Monty Hall problem.
    https://en.wikipedia.org/wiki/Monty_Hall_problem
*/


#include "utils.hpp"
#include "stats.hpp"
#include "settings.hpp"
#include "instance.hpp"


using namespace std;



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


void iterate(Statistics& stats, bool verbose)
{
    Instance inst = randomInstance();
    bool result = simulate(inst, stats);

    if (verbose)
    {
        cout << inst << " --> " << (result ? 1 : 0) << endl;
    } 
}


Statistics run(Settings& settings)
{
    Statistics stats(settings.iters); 

    for (int iter = 0; iter < settings.iters; ++iter)
    {
        iterate(stats, settings.verbose);
    }

    return stats;
}


int main(int argc, char* argv[])
{
    Settings settings(argc, argv);
    initRandWithTime();

    Statistics stats = run(settings);
    stats.print();

    return 0;
}


