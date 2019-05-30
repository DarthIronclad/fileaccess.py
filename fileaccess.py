nameinput = input('Enter your name:')
if nameinput == str(nameinput):
        with open("heights.txt", 'a',encoding='utf-8') as f:
                f.write(nameinput)
                f.write('\t')
else:
        print("ERROR")
heightinput = input('Enter your height')
val = float(heightinput)
if val == float(val):
        with open("heights.txt", 'a',encoding='utf-8') as f:
                f.write(heightinput)
                f.write('\n')
else:
        print("ERROR")
class PA1:
        def __init__(code, names, heights, totalStudentHeight, totalStudentCount):
                code.names = names
                code.heights = heights
                code.totalStudentHeight = totalStudentHeight
                code.totalStudentCount = totalStudentCount
class CalUtils(PA1):
        def __init__(code, names, heights, totalStudentHeight, totalStudentCount):
                PA1.__init__(code, names, heights, totalStudentHeight, totalStudentCount)
students = []
total = []
fo = map(str.strip, open('heights.txt').readlines())
for line in fo:
        List = line.split("\t")
        name = List[0]
        height = List[1]
        students.append(name)
        total.append(float(height))
        List = CalUtils(name,height,total,students)
        print('Name:'+ str(List.names))
        print('Height:'+ str(List.heights))
        average = sum(List.totalStudentHeight) / len(List.totalStudentCount)
        print('Average Height of studends is ' + str(round(average,2)) + ' for ' + str(len(List.totalStudentCount)) + ' students')