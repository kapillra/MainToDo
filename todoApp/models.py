from django.db import models

class Role(models.Model):
    Role = models.CharField(max_length=20)

    class Meta:
        db_table = 'role'

    def __str__(self) -> str:
        return self.Role

class Department(models.Model):
    DeptName = models.CharField(max_length=25)

    class Meta:
        db_table = 'department'

    def __str__(self) -> str:
        return self.DeptName

class Master(models.Model):
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=25)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
)
class UserProfile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    

    ProfileImage = models.FileField(upload_to='users/avatars', default='avatar.png')

    FullName = models.CharField(max_length=25, blank=True, null=True)
    Gender = models.CharField(max_length=2, choices=gender_choices)
    BirthDate = models.DateField(auto_created=True, blank=True, null=True)
    Mobile = models.CharField(max_length=10, blank=True, null=True)
    Country = models.CharField(max_length=25, blank=True, null=True)
    State = models.CharField(max_length=25, blank=True, null=True)
    City = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'userprofile'

    def __str__(self) -> str:
        return self.FullName if self.FullName else 'NoName'

status_choices = (
    ('c', 'completed'),
    ('p', 'pending'),
    ('nt', 'not started')
)
class ToDoList(models.Model):
    Title = models.CharField(max_length=25)
    Tags = models.CharField(max_length=255)
    Deadline = models.DateTimeField(auto_created=True)
    DateCreated = models.DateTimeField(auto_now_add=True)

    Description = models.TextField(max_length=255)
    Status = models.CharField(max_length=15, choices=status_choices)
    DateCompleted = models.DateTimeField(auto_created=True)

    class Meta:
        db_table = 'todolist'

    def __str__(self) -> str:
        return self.Title

class TaskAssociation(models.Model):
    Member = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ToDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TaskAssociation'

    def __str__(self) -> str:
        return self.Member.FullName