/*
    Copyright (c) 2016 - buyuk.dev@gmail.com
*/

#ifndef __montyhall_settings_hpp_
#define __montyhall_settings_hpp_


#include "utils.hpp"




struct Settings
{
    Settings(int argc, char* argv[])
    {
        if (argc < 2)
        {
            iters = 0;
        }

        if (argc < 3)
        {
            verbose = false;
        }

        if (argc == 3)
        {
            verbose = strtobool(argv[2]);
        }

        if (argc > 1)
        {
            iters = strtoint(argv[1]);
        }
    }  

    bool verbose;
    int  iters;
};


#endif // __montyhall_settings_hpp_
