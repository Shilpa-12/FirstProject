import csv
def write_into_csv(infolist):
    with open('student_info.csv','a',newline='') as csv_file :
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age", "Contact Number", "Email"])
        writer.writerow(infolist)
if __name__ == '__main__':
    condition = True
    student_num = 1
    while(condition):
        student_info = input("Enter some student information for student #{} in format(Name Age Contact Email):".format(student_num))
        student_info_list=student_info.split(' ')
        print("\nEntered information is:\nName: {}\nAge: {}\nContact Number: {}\nEmail: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Is entered information is correct (yes/no):")
        if choice_check == "yes":
            write_into_csv(student_info_list)
            condition_check = input("Want to continue? Enter (yes/no) ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("\nRe-enter the values")
