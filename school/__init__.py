import csv
from school.models import School, Member

# School Name,School City,Chapter Name,Chapter ID,Division,Region,District,FirstName,MI,LastName,Member ID,MemberType,GPA,GradYear,NumYears,BusEdCourse,EMail,Paid

def import_csv():
    reader = csv.reader(open('MichiganStudentList.csv'))
    #get rid of the headers
    reader.next()
    for row in reader:
        #empty lines shouldn't count.'
        if row:
            try:
                school, created = School.objects.get_or_create(
                    name=row[0], 
                    city=row[1], 
                    division=row[4], 
                    region=row[5] if (row[5] and row[5] is not "X") else None, 
                    district=row[6] if (row[6] and row[6] is not "X") else None)
                if created:
                    #only save if its new? any optimizations help with canada.
                    school.save()
                info = {
                    'first': row[7], 
                    'last': row[9], 
                    'school': school, 
                    'memberid': row[10], 
                    'membertype': row[11], 
                    'gpa': float(row[12]) if row[12] else None,
                    'grad_year': int(row[13]) if row[13] else None,
                    'num_years': int(row[14]) if row[14] else None,
                    'courses': row[15], 
                    'paid': row[17] == "Yes",
                }
                student, created = Member.objects.get_or_create(**info)
            except Exception as e:
                print "Messed Up:", row, e
