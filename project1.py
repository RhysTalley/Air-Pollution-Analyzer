import csv

def file_to_dicts_airquality(file):
    # reads file and converts it to a list of tuples
    data_reader = csv.reader(file)
    l = []
    for line in data_reader:
        l.append((line[0],line[1],line[2],line[3])) # appends in a tuple b/c directions ask for a list of tuples

    # converts list of tuples to 2 dictionaries
    uhf_codes = {}
    dates = {}
    for line in l: # iterates through the list of al the data fields
        if line[0] not in uhf_codes: # if the uhf code is not in the dictionary, make a new entry for that uhf code
            uhf_codes[line[0]] = [line]
        else: # if it is in the dictionary, just append the data to the list value in the dictionary
            uhf_codes[line[0]].append(line)
        if line[2] not in dates: # same thought process for the dates dictionary
            dates[line[2]] = [line]
        else:
            dates[line[2]].append(line)
    return uhf_codes, dates

def file_to_dicts_uhf(file):
    data_reader = csv.reader(file)
    zip_to_uhf = {}
    borough_to_uhf = {}
    for line in data_reader: # very similar process but just iterate straight through data reader (cause tuple isn't necessary)
        if(line[0] not in borough_to_uhf): # creation of borough dict
            borough_to_uhf[line[0]] = [line[2]] # line[0] corresponds to borough, line[2] corresponds to uhf code
        else:
            borough_to_uhf[line[0]].append(line[2])
        for zipcode in line[3:]: # creation of zipcode dict (more than one zipcode in some entries)
            if zipcode not in zip_to_uhf: # so we use list slicing to iterate through all of them
                zip_to_uhf[zipcode] = [line[2]]
            else:
                zip_to_uhf[zipcode].append(line[2])
    return zip_to_uhf, borough_to_uhf


def print_dicts(uhf_codes, dates): # helper method to print out dictionaries
    for c in uhf_codes:
        print(f"{c} --> {uhf_codes[c]}")
        print('\n')
    print('\n')
    print('\n')
    print('\n')
    for c in dates:
        print(f"{c} --> {dates[c]}")
        print('\n')

def print_data(l):
    print(f"{l[2]} UHF {l[0]} {l[1]} {l[3]} mcg/m^3") # helper method to print data in correct format

if __name__=="__main__":
    file = open("air_quality.csv", mode="r", encoding='utf-8-sig')
    file2 = open("uhf.csv", mode="r")
    uhf_codes, dates = file_to_dicts_airquality(file)
    zip_to_uhf, borough_to_uhf = file_to_dicts_uhf(file2) # instantiates the files and creates the dictionaries


    user_choice = input("Would you like to search by Zip Code (z), UHF ID (u), Borough (b), or Date (d)?\n")
    # if, elif, else chain to see what the user inputs
    if user_choice=="z":
        zipcode = input("Enter a zipcode:\n")
        for uhf in zip_to_uhf[zipcode]: # iterate through all uhf codes corresponding to the given zipcode
            for data in uhf_codes[uhf]: # iterates through the data for each uhf code
                print_data(data) # prints it in required format
    elif user_choice=="u":
        uhf = input("Enter a UHF ID:\n")
        for data in uhf_codes[uhf]: # can skip the intermediary step and just search through the ufc dict automatically
            print_data(data)
    elif user_choice=="b":
        borough = input("Enter a borough (capital starting letters, no spaces):\n")
        for uhf in borough_to_uhf[borough]: # same process as zipcode, look through borough_to_uhf dict first
            for data in uhf_codes[uhf]: # then look through the uhf measurement dict
                print_data(data)
    elif user_choice=="d":
        date = input("Enter a date (month/day/year):\n")
        for data in dates[date]: # same process as uhf id b/c we have a dict correlating date to measurement
            print_data(data)
    else:
        print("Invalid input") # just a little bit of error handling in case the user does'nt enter u,z,b, or d