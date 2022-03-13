"""
Created on 11/13/2021

@author: alyss
"""
"""
This function returns a sorted list of these strings based on the following 
constraints. The final list should be sorted first by major 
(in alphabetical order), then by GPA (in descending order) and then by class 
(in descending order). If two students have the same major and the same GPA, 
then the student with the higher classification should be recognized first

"""

def sortrankings(students):
    '''
    The list parameter students contains strings in the format "name:major:class:GPA", where:

    name-first name only of a student (assume all student names are unique).

    major-student's major (e.g., "CS" is Computer Science, "ME" is Mechanical Engineering).

    class-an integer from 1-4 (1 is first year, 2 is sophomore, 3 is junior, and 4 is senior).

    GPA-float between 0.0-4.0.

   The function should return a sorted list of students by major (ascending),
   GPA (descending), and class (descending order) in the event there is a tie with GPAs.
    '''
    ret = []
    for student in students:
        name = student.split(":")[0]
        major = student.split(":")[1]
        classification = student.split(":")[2]
        gpa = student.split(":")[3]
        ret.append([name,major,classification,gpa])
    ret = sorted(sorted(sorted(ret,key = lambda x: x[2], reverse = True),
                    key = lambda x: x[3], reverse = True), key = lambda x: x[1])

    return [":".join(i) for i in ret]

if __name__ == '__main__':
    print (sortrankings(["Tim:Math:1:2.75", "Mia:CS:3:3.96", "Kim:AAAS:4:3.96", "Amy:CS:1:3.14", "Jason:ECE:2:3.4"]))
