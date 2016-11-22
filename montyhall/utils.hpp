/*
    Copyright (c) 2016 - buyuk.dev@gmail.com
*/

#ifndef __montyhall_utils_hpp_
#define __montyhall_utils_hpp_

#include <string>
#include <sstream>
#include <cstdlib>


int random(int beg, int end)
{
    int range = (end - beg + 1);
    int base = rand() % range;
    return base + beg;
}


int strtoint(std::string str)
{
    std::istringstream parser(str);

    int val = 0;
    parser >> val;

    return val;
}


bool strtobool(std::string str)
{
    if (str == "true")
    {
        return true;
    }
    else
    {
        return false;
    }
}


void initRandWithTime()
{
    time_t tm = time(nullptr);
    unsigned int seed = static_cast<unsigned int>(tm);
    srand(tm);
}


double getPercentValue(int val, int total)
{
    double ratio = double(val) / double(total);
    return ratio * 100.0f;
}


#endif // __montyhall_utils_hpp_
