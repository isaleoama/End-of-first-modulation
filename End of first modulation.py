def out_red(text):
    print("\033[36m{}".format(text))
out_red("Средний бал учеников:")
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
student_two = []
unique_keys = len(grades)
students.sort (key=None, reverse=False)
for i in range (unique_keys) :
    average = sum(grades[0]) / len(grades[0])
    student_one = {students[0]:average}
    del_grades = grades.pop([0][0])
    del_students = students.pop([0][0])
    student_two.append(student_one)
print(student_two)
print('////////////////////////////////////////////////////////////////////////////////////////////////////')

#Можем сделать и такой вариант, он заключён на автоматизмне, запрограммировать в приложение и можно запустить с телефона :)
students_list = []
ball_list = []
student_twoo = []
number_students = int(input('Введите кол-во студентов для анализа:'))
for i in range ( number_students ) :
    name = input('Введите имя студента:')
    ball = list(map(int, input('Введите оценки через пробел:').split(" ")))
    students_list.append(name)
    ball_list.append(ball)
    average_b = int(sum(ball_list[0]))/ len(ball_list[0])
    student_one = {students_list[0]:average_b}
    del_balls = ball_list.pop([0][0])
    del_studentss = students_list.pop([0][0])
    student_twoo.append(student_one)
print(student_twoo)





