import csv
from school.models import School, Student

# School Name,School City,Chapter Name,Chapter ID,Division,Region,District,FirstName,MI,LastName,Member ID,MemberType,GPA,GradYear,NumYears,BusEdCourse,EMail,Paid

def import_csv():
    reader = csv.reader(open('MichiganStudentList.csv'))
    #get rid of the headers
    reader.next()
    for row in reader:
        #empty lines shouldn't count.'
        if row:
            school, created = School.objects.get_or_create(school=row[0], city=row[1], division=row[4], region=row[5], district=row[6])
            if created:
                #only save if its new? any optimizations help with canada.
                school.save()
            student, created = Student.objects.get_or_create(first=row[7], last=row[9], school=school, member_id=row[10], gpa=row[12], grad_year=row[13], num_years=row[13], courses=row[14], paid=row[16])
            
