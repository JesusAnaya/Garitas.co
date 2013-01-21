import ctypes
import ctypes.util
clib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))


def str_to_int(str):
    return clib.atoi(str)


def str_to_float(str):
    return clib.atof(str)


def num_format(num):
    return num if len(num) == 2 else "0%s" % num


def time_format(time):
    if(time is not None):
        if(time == '0'):
            time = '0 min'
        if(time.find('hrs') == -1):
            time = '0 hrs %s' % time
        if(time.find('min') == -1):
            time = '%s 0 min' % time
        time_list = time.replace(' hrs', '').replace(' min', '').split(' ')
        return (time_list[0], num_format(time_list[1]))
    return ('--', '--')
