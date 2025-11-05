import csv
with open("Example.csv", mode= 'r') as csv_file:
    csv_Reader= csv.DictReader(csv_file)
    line_count= 0
    for row in csv_Reader:
        if line_count == 0:
           print(f'Column names are {",".join(row)}')
        line_count += 1
        print(f'{row["course_name"]} is taught by {row["instructor"]} and duration of the course is {row["duration_weeks"]} weeks')
        print(f'Done Reading Data {line_count} line.')
       

