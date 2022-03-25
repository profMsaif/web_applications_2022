

from django.shortcuts import render
from .models import Students,AttendanceReport,Courses,Subjects,Attendance,CustomUser


def student_home(request):
  student_obj = Students.objects.get(admin=request.user.id)
  total_attendance =   AttendanceReport.objects.filter(student_id=student_obj).count()
  attendance_present = AttendanceReport.objects.filter(student_id=student_obj,
                                                       status=True).count()
  attendance_absent =  AttendanceReport.objects.filter(student_id=student_obj,
                                                       status=False).count()
  course_obj = Courses.objects.get(id=1)
  total_subjects = Subjects.objects.filter(course_id=course_obj).count()
  subject_name = []
  data_present = []
  data_absent = []
  subject_data = Subjects.objects.filter(course_id=student_obj.course_id)
  for subject in subject_data:
                  attendance = Attendance.objects.filter(subject_id=subject.id)
                  attendance_present_count = AttendanceReport.objects.filter(attendance_id__in=attendance,
                                                                            status=True,
                                                                            student_id=student_obj.id).count()
                  attendance_absent_count = AttendanceReport.objects.filter(attendance_id__in=attendance,
                                                                            status=False,
                                                                            student_id=student_obj.id).count()
                  subject_name.append(subject.subject_name)
                  data_present.append(attendance_present_count)
                  data_absent.append(attendance_absent_count)
     
  context={
        "total_attendance": total_attendance,
        "attendance_present": attendance_present,
        "attendance_absent": attendance_absent,
        "total_subjects": total_subjects,
        "subject_name": subject_name,
        "data_present": data_present,
        "data_absent": data_absent
    }

  return render(request, "student_template/student_home_template.html",context=context)




def student_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)
 
    context={
          "user": user,
          "student": student
      }
    return render(request, 'student_template/student_profile.html', context)


def student_view_attendance(request):
    student = Students.objects.get(admin=request.user.id)
    subjects = Subjects.objects.filter(course_id=student.course_id)
    context = {
        "subjects": subjects
    }
    return render(request, "student_template/student_view_attendance.html", context)    