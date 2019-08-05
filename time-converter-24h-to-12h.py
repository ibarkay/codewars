def time_converter(time):
    time_nums = time.split(':')


    time_nums[0] = int(time_nums[0])

    if time_nums[0] == 0 :
        return '12:{} a.m.'.format(time_nums[1])

    if time_nums[0] == 12:
         return '{}:{} p.m.'.format(time_nums[0],time_nums[1])


    if time_nums[0] >=13 :
        time_nums[0] = time_nums[0] -12
        return '{}:{} p.m.'.format(time_nums[0],time_nums[1])

    if time_nums[0] < 12:
        return '{}:{} a.m.'.format(time_nums[0],time_nums[1])











time_converter("12:00")