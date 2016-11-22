/*
    Copyright (c) 2016 - buyuk.dev@gmail.com
*/

#ifndef __montyhall_stats_hpp_
#define __montyhall_stats_hpp_


#include <iostream>
#include <string>
#include <sstream>

#include "utils.hpp"



std::string stattostr(int stat, int total, std::string msg)
{
    std::ostringstream conv;
    
    conv << msg << ": " << stat
         << " [ " << getPercentValue(stat, total) << "% ]";

    return conv.str();
}


struct Statistics
{
    Statistics(int iters = 0)
    : withSwap(0), withoutSwap(0),
      swaps(0), iters(iters)
    {
    }

    void print(bool header = true)
    {
        if (header)
        {
            std::cout << "--------------------" << std::endl
                      << "     STATISTICS     " << std::endl
                      << "--------------------" << std::endl;
        }

        std::cout << stattostr(withSwap, swaps, "success swap")               << std::endl
                  << stattostr(withoutSwap, iters - swaps, "success no swap") << std::endl
                  << stattostr(swaps, iters, "number of swaps")               << std::endl;
    }

    int withSwap;
    int withoutSwap;
    int swaps;
    int iters;
};


#endif // __montyhall_stats_hpp_

