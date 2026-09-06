# Reading from files
filename = "rudyard.txt"

with open(filename, "r") as poem_file:
    title = poem_file.readline()
    first_poem_line = poem_file.readline()

print("Title:", title, end="")
print("First line:", first_poem_line, end="")

# Counting Lines
line_count = 0
if_count = 0

with open("rudyard.txt", "r") as poem_file:
    for line in poem_file:
        # Count how many times If appears in this line.
        # Remember: line.count("If") returns a number.

        line_count = line_count + 1
        if_count = line.count("If") + if_count

print("Lines:", line_count)
print("If count:", if_count)

# Writing to a new file
# Task: count the lines in rudyard.txt, then write the answer to stats.txt.
# Use write mode: "w"

line_count = 0

with open("rudyard.txt", "r") as poem_file:
    for line in poem_file:
        line_count = line_count + 1

# Open stats.txt in write mode and write this exact text:
# Lines: 36
# Include the newline character at the end.

with open("stats.txt", "w") as stats_file:
    Data = "Lines: " + str(line_count) + "\n"
    stats_file.write(Data)

with open("stats.txt", "r") as stats_file:
    saved_text = stats_file.read()

print(saved_text)

# Must "w" before "r" as "w" creates the file
# Only allows 1 item to be written so data must be concatenated beforehand.


# Appending to a file
name = input ("Enter reader's name: ")
Reader = "Reader: " + name
with open("reading_log.txt", "a") as log_file:
    log_file.write(Reader)

with open("reading_log.txt", "r") as log_file:
    log_text = log_file.read()

print("Reading log")
print(log_text)

# Searching through a TSV file

# Task: ask for a year, then print every event from that year.
# Each line has: Event, Month, Year, Description

search_year = input("Enter a year: ")
found = False

with open("historical_events.tsv", "r") as event_file:
    header = event_file.readline()
    for line in event_file:
        parts = line.strip().split("\t")
        event = parts[0]
        month = parts[1]
        year = parts[2]
        description = parts[3]
        if search_year == year:
            print(month, year, "-", event)
            found = True

if found == False:
    print("No events found")

# Removes white space and new line characters in the file
# Split the file based on "\t" (can also use split ",")
# Prints on new line each time as it is in a "for loop" so no need for new line character.

# Task: save all events from one chosen month to month_timeline.txt.
# Then read the saved file and print it.

search_month = input("Enter a month: ")

with open("historical_events.tsv", "r") as event_file:
    header = event_file.readline()
    for line in event_file:
        parts = line.strip().split("\t")
        event = parts[0]
        month = parts[1]
        year = parts[2]
        if month == search_month:
            Event = year + " - " + event + "\n"
            with open("month_timeline.txt", "a") as timeline_file:
                timeline_file.write(Event)

with open("month_timeline.txt", "r") as timeline_file:
    print(timeline_file.read())
# Don't forget the new line character for this one as the events are independent of the loop.


# Task: collect a new event and append it to my_events.tsv.
# Then print the file so the new record can be seen.

event = input("Event: ")
month = input("Month: ")
year = input("Year: ")
description = input("Description: ")

# Write the header first using write mode.
with open("my_events.tsv", "w") as events_file:
    events_file.write("Event\tMonth\tYear\tDescription\n")

# Now append the new row using append mode.
# Separate each part with \t and end with \n.

Event = event + "\t" + month + "\t" + year + "\t" + description + "\n"
with open("my_events.tsv", "a") as events_file:
    events_file.write(Event)

with open("my_events.tsv", "r") as events_file:
    print(events_file.read())
# Might be better to refer to the same file using the same identifier to avoid mix-ups.
