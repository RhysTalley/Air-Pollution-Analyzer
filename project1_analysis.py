from project1 import file_to_dicts_uhf, file_to_dicts_airquality

if __name__ == "__main__":
    file = open("air_quality.csv", mode="r", encoding='utf-8-sig')
    file2 = open("uhf.csv", mode="r")
    uhf_codes, dates = file_to_dicts_airquality(file) # same instantiation and creation of dicts from last time
    zip_to_uhf, borough_to_uhf = file_to_dicts_uhf(file2)

    # a) Lowest and Highest Air Pollution in Zip Code 10027

    highest = 0.0 # set the highest to arbitrarily low point so it will be overridden
    lowest = 100000.0 # set lowest to arbitrarily high point to it will be overwritten
    for uhf in zip_to_uhf['10027']: # search through all uhf codes associated with "10027"
        for data in uhf_codes[uhf]: # search through all data associated with all uhf codes
            if float(data[3])>highest: # check to see if it's value is higher than the highest
                highest = float(data[3]) # if it is, change highest to this new value
            if float(data[3])<lowest: # same process for lowest
                lowest = float(data[3])
    print(f"Highest: {highest}\nLowest: {lowest}") # print out highest and lowest

    # b) Which UHF ID had the Worst Air Pollution in 2019?

    worst = 0.0 # again, arbitrarily low value for worst so it is overwritten
    uhf = 0 # uhf variable set to any value (value doesn't matter here because there is no comparison against the uhf variable)
    for key in dates: # iterate through all dates
        if key[len(key)-2:]=='19': # use string slicing to check the last two digits in the date are equal to '19', 2019
                                   # (start from the back of the string.subtract two, and slice off everything before that)
            for tups in dates[key]: # if the date is in 2019, iterate through the data within that entry
                if float(tups[3])>worst: # change worst if the measurement is worse
                    worst = float(tups[3])
                    uhf = tups[0] # then, create a uhf variable
    print(f"UHF {uhf} had the worst air pollution in 2019 with the maximum air pollution being {worst} mgc/m^3")

    # c) What was the average air pollution in Manhattan in 2008 and in 2019.

    # the idea is that we will sum all the measurements from 2008 and 2019 and divide it by the total number of data
    # entries in each year

    sum_eight = 0 # sum of the pollutions in 2008
    sum_nineteen = 0 # sum of the pollutions in 2019
    count_eight = 0 # the amount of data entries in 2008
    count_nineteen = 0 # the amount of data entries in 2019
    for uhf in borough_to_uhf["Manhattan"]: # iterate through the uhf codes in Manhattan
        for tups in uhf_codes[uhf]: # iterate through the tups in all the uhf codes in manhattan
            if tups[2][len(tups[2])-2:]=='19': # checks to see if the date is 2019
                sum_nineteen += float(tups[3]) # adds the measurement to the total sum
                count_nineteen+=1 # increments the count
            if tups[2][len(tups[2])-2:]=='08': # checks to see if the date is 2008
                sum_eight += float(tups[3]) # same process as 2019
                count_eight += 1
    sum_eight /= count_eight # once the loop is over, divide the sum by the total count
    sum_nineteen /= count_nineteen #
    print(f"Average in 2008: {sum_eight}\nAverage in 2019: {sum_nineteen}") # then print out the newly calculated averages

    # d) What is the Borough With the Highest Average Pollution Over From 2008-2020?

    highest_avg = 0 # highest avg set arbitrarily low
    for key in borough_to_uhf: # iterate through every borough
        count = 0.0 # create a count
        pollution_sum = 0.0 # and a sum so you can divide count by sum at the end
        for uhf in borough_to_uhf[key]:
            for measurements in uhf_codes[uhf]:
                pollution_sum += float(measurements[3]) # sum up all the measurements
                count += 1 # and increment the count
        pollution_sum /= count # then divide to find the average
        if pollution_sum>highest_avg: # if the avg pollution is higher than the highest_avg
            highest_avg = pollution_sum # then we update highest_avg
            borough_name = key # and instantiate a variable called borough_name with the new borough name
    print(f"The borough with the highest average air pollution is {borough_name} with an average pollution of {highest_avg}")

    # e) Average Pollution in June vs December from 2008-2020?

    avg_june = 0.0 # variable for june avg (and also the sum of all measurements in june)
    count_june = 0 # counts all the measurements taken in june
    avg_dec = 0.0 # same for dec
    count_dec = 0 # same for dec
    for date in dates:
        l_str = date.split("/") # split the dates into a string based on where the '/' is, so we can separate day from month from year
        if l_str[0]=="6" or l_str[0]=="12": # check to see if the first field in this list, corresponding to month, is june or december
            for tups in dates[date]: # if it is, then  sum up the data
                if l_str[0]=="6": # if it's june
                    avg_june += float(tups[3])
                    count_june += 1
                else: # if it's not june, it must be december
                    avg_dec += float(tups[3])
                    count_dec += 1
    avg_june /= count_june # then divide to find true averages
    avg_dec /= count_dec
    print(f"Average in June: {avg_june}\nAverage in December: {avg_dec}") # and print