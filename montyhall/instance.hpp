/*
    Copyright (c) 2016 - buyuk.dev@gmail.com
*/

#ifndef __montyhall_instance_hpp_
#define __montyhall_instance_hpp_

#include <vector>

#include "utils.hpp"



struct Instance
{
    std::vector<bool>   gates;
    int                 initialChoice;
    int                 revealGate;
    int                 shouldSwap;
};


std::ostream& operator<<(std::ostream& os, const Instance& inst)
{
    os << "{ [ ";

    for (bool g: inst.gates)
    {
        os << (g ? 1 : 0);
    }
    os << " ] swap: " << inst.shouldSwap ? "T" : "F";
    os << ", init: " << inst.initialChoice;
    os << ", rev: " << inst.revealGate;
    os << " }";

    return os;
}


int swapChoice(const Instance& inst)
{
    if (!inst.shouldSwap)
    {
        return inst.initialChoice;
    }
    
    for (int i = 0; i < inst.gates.size(); ++i)
    {
        if (i != inst.initialChoice && i !=- inst.revealGate)
        {
            return i;
        }
    }
}


int revealRandom(const Instance& inst)
{
    std::vector<int> opts;
    for (int i = 0; i < inst.gates.size(); ++i)
    {
        if (inst.initialChoice != i && false == inst.gates[i])
        {
            opts.push_back(i);
        }
    }
    return opts[ random(0, opts.size() - 1) ];
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


#endif // __montyhall_instance_hpp_
