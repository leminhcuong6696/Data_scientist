import numpy as np
import pandas as pd

file_name = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
# nhap vao ten file diem hoc sinh
def check(var):
    aray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in var[1:9]:
        if i not in aray:
            return False
    return  True
# Ham kiem tra ma so hoc sinh co dung hay khong

def point(var):
    anser_key = ("B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D").split(',')
    count = 0
    for i in range(1, len(var.split(','))):
        if var.split(',')[i] == anser_key[i-1]:
            count += 4
        if var.split(',')[i] != anser_key[i-1]:
            if var.split(',')[i] == "":
                count += 0
            else:
                count = count - 1
    return count
# Ham tinh diem cho tung bai kiem tra hop le

try:                        #bat dau khoi lenh kiem tra tinh hop le cua file name
    with open(file_name + ".txt", "r") as class_file:
        print ("successfully opened ", file_name, "\n") 
        print ("**** ANALYZING ****", "\n")
        check_list = {}             #khoi tao dictionary de kiem tra tinh hop le cua tung bai kiem tra
        count = 0                   #bien count dung de tinh so bai kiem tra khong hop le
        test_file = class_file.read().split("\n")
        for i in test_file:
            check_list[i] = 0
        for test in test_file:
            if len(test.split(",")) != 26:
                print ("Invalid line of data: does not contain exactly 26 values:", "\n", test, "\n")
                if check_list[test] == 0:
                    check_list[test] = 1
            if (test.split(",")[0][0] != "N") or (len(test.split(",")[0]) !=9) or (check(test.split(",")[0]) == False):
                print ("Invalid line of data: N# is invalid", "\n", test, "\n")
                if check_list[test] == 0:
                    check_list[test] = 1
        for u,v in check_list.items():
            count += v
        result = {}                 #khoi tao dictionary luu tru ma so sinh vien va diem tuong ung
        for u,v in check_list.items():
            if v == 0:
                result[(u.split(",")[0])] = point(u)
        final_point = []            #khoi tao list de luu tru diem cua toan bo class
        for u,v in result.items():
            final_point.append(v)
        if count == 0: 
            print ("No errors found")
            print ("**** REPORT ****", "\n")
            print ("Total valid lines of data: ", len(test_file) - count, '\n')
            print ("Total invalid lines of data: ", count, '\n')
            print ("Mean (average) score: ", round(np.average(final_point), 2), '\n')
            print ("Highest score: ", np.amax(final_point), '\n')
            print ("Lowest score: ", np.amin(final_point), '\n')
            print ("Range of scores: ", np.ptp(final_point), '\n')
            print ("Median score: ", np.median(final_point))
        else:
            print ("**** REPORT ****", "\n")
            print ("Total valid lines of data: ", len(test_file) - count, '\n')
            print ("Total invalid lines of data: ", count, '\n')
            print ("Mean (average) score: ", round(np.average(final_point), 2), '\n')
            print ("Highest score: ", np.amax(final_point), '\n')
            print ("Lowest score: ", np.amin(final_point), '\n')
            print ("Range of scores: ", np.ptp(final_point), '\n')
            print ("Median score: ", np.median(final_point))
    with open(file_name + '_grades.txt', 'w') as save_file:
        for u,v in result.items():
            save_file.write(u + ", " + str(v) + "\n")
except:
    print("file can not be found!") 
 
