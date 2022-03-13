"""
Created on 11/11/2021

@author: alyssa
"""
def countHonors(students):
    '''
    students - list of strings of student info in the format
    ["lastname,class,GPA"]
	NOTE: THERE IS NO SPACE AFTER ANY COMMA IN EACH STRING
	'''

    dict = {}
    for student in students:
        gpa = float(student.split(",")[-1])
        if gpa >= 3.5 and student.split(",")[1] not in dict:
            dict[student.split(",")[1]] = 1
        elif gpa >= 3.5:
            dict[student.split(",")[1]] += 1
    ret = []
    for i in sorted(dict.items()):
        ret.append(i[0] + ":" + str(i[1]))
    return ret

    # students=["Lewis,First Year,3.56", "Harris,Sophomore,3.5", "Thomas,Senior,3.18", "Williams,First Year,3.7"]
#
# Returns ["First Year:2", "Sophomore:1"]

if __name__ == '__main__':
    print (countHonors(["Lewis,First Year,3.56", "Harris,Sophomore,3.5", "Thomas,Senior,3.18", "Williams,First Year,3.7"]))
