import pandas as pd
from pathlib import Path
file=Path("Data/Students_classes_6_to_10_Marks.xlsx")
Students=pd.read_excel(file)
life='yes'
while life=='yes':
    print("1.Display the All the Students in Record")
    print("2.Display the Top Five students")
    print("3.Display the Least Five Students")
    print("4.Display the Topper of the Each class")
    print("5.Display the Topper of the School")
    print("6.Display the looser of the Each class")
    print("7.Display of the losser of the school")
    print("8.Display the Students Each class")
    print("9.Display Data info")
    print("10.Display the How many Students are pass")
    print('11.Display the How many columns')
    print('12.Display the Shape')
    print('13.Display the Total number of students')
    print('14.Convert the integer to Float value Attendance Percentage')
    print('15.Display the Above 500 Marks')
    print('16.Display the Below 300 marks')
    choice=int(input("Enter Your Choice:"))
    if(choice>10 and choice <0):
        print("Please Enter the valid Choice")
    elif choice==1:
        print(Students)
    elif choice==2:
        SortStudents=Students.sort_values(by='Total_Marks',ascending=False)
        print(SortStudents.head())
    elif choice==3:
        SortStudents=Students.sort_values(by='Total_Marks',ascending=True)
        print(SortStudents.head())
    elif choice==4:
        Toppers=Students.loc[Students.groupby('Class')['Total_Marks'].idxmax()]
        print(Toppers)
    elif choice==5:
        print(Students.loc[Students['Total_Marks'].idxmax()])
    elif choice==6:
            Toppers=Students.loc[Students.groupby('Class')['Total_Marks'].idxmin()]
            print(Toppers)
    elif choice==7:
        print(Students.loc[Students['Total_Marks'].idxmin()])
    elif choice==8:
        Count=Students['Class'].value_counts()
        print(Count)
    elif choice==9:
        print(Students.info())
    elif choice==10:
        print(Students['Result'].value_counts())
    elif choice==11:
        print(Students.columns)
    elif choice==12:
        print(Students.shape)
    elif choice==13:
        print(Students.shape[0])
    elif choice==14:
        Students1=Students.loc[Students['Average_Marks'].astype(int)]
        print(Students1.head())
    elif choice==15:
        print(Students[Students['Total_Marks']>500])
    elif choice==16:
        print(Students[Students['Total_Marks']<300])
    life=input('If you want to continue enter the yes or else enter the no:')
