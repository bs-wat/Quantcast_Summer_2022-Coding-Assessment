# Quantcast Summer 2022 Internship - Coding Assessment
# Candidate: Brandon Wat

import sys

def most_active_cookie(csv_file, request_date):
    
    # would consider using defaultdict if additional libraries allowed
    cookie_counts = {}

    # counts the occurences of the cookie using dictionary/hash map
    with open(csv_file, "r") as cookie_log:
        lines = cookie_log.readlines()

        for i in range(1,len(lines)):
            # separate the cookie and timestamp
            entry = lines[i].split(",")
            
            cookie = entry[0]
            time_stamp = entry[1]

            date = time_stamp.split("T")[0]

            # not the request date -> no need to count the cookie -> go to next line
            if date != request_date:
                continue

            if cookie not in cookie_counts:
                cookie_counts[cookie] = 1
            else:
                cookie_counts[cookie] += 1

    # find the highest cookie frequency
    max_freq = max(cookie_counts.values())

    # output most active cookie(s)
    for cookie_key in cookie_counts:
        count = cookie_counts[cookie_key]

        if count == max_freq:
            print(cookie_key)

    # I'm not fully sure about the "-d" parameter if it is already assumed the time zone will be UTC.
    # Currently, I am taking in "-d" at index 2 of sys.argv but I'm not using it and simply using the date at index 3.

    # tested on command line with example format: python most_active_cookie.py cookie_log.csv -d 2018-12-09
if __name__ == "__main__":
    most_active_cookie(sys.argv[1],sys.argv[3])