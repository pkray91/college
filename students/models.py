# from django.db import models
# from common.models import User

# class SessionYearModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     session_start_year = models.DateField()
#     session_end_year = models.DateField()
    
# class Courses(models.Model):
#     id = models.AutoField(primary_key=True)
#     course_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
 
# class Subjects(models.Model):
#     id =models.AutoField(primary_key=True)
#     subject_name = models.CharField(max_length=255)
     
#     # need to give default course
#     course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1)
#     staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Students(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     admin = models.OneToOneField(User, on_delete = models.CASCADE)
#     gender = models.CharField(max_length=50)
#     profile_pic = models.FileField()
#     address = models.TextField()
#     course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, default=1)
#     session_year_id = models.ForeignKey(SessionYearModel, null=True,
#                                         on_delete=models.CASCADE)
    