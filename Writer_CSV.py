import csv
with open("Example.csv", mode= 'w') as csv_file:
    fieldnames= ['course_name', 'instructor', 'duration_weeks']
    writer= csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'course_name': 'Python Basics', 'instructor': 'Ali Khan', 'duration_weeks': '6'})
    writer.writerow({'course_name': 'Data Science Essentials', 'instructor': 'Sara Ahmed', 'duration_weeks': '8'})
    writer.writerow({'course_name': 'Web Development', 'instructor': 'Usman Tariq', 'duration_weeks': '10'})
    writer.writerow({'course_name': 'Machine Learning', 'instructor': 'Amna Iqbal', 'duration_weeks': '12'})
    print("Writing csv done and saved to example.csv")