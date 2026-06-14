from django.db import models


class Warden(models.Model):
    name = models.CharField(max_length=100)
    
    phone = models.CharField(max_length=15)
    shift_time = models.CharField(
    max_length=10,
    choices=[
        ('Morning','Morning'),
        ('Evening','Evening'),
        ('Night','Night')
    ]
    )

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    status = models.CharField(
    max_length=10,
    choices=[
        ('Free','Free'),
        ('Full','Full')
    ],
    default='Free'
    )
    warden = models.ForeignKey(Warden, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_number


class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(
    max_length=10,
    choices=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    status = models.CharField(max_length=20)


class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    complaint_text = models.TextField()
    complaint_date = models.DateField()
    status = models.CharField(
    max_length=15,
    choices=[
        ('Resolved','Resolved'),
        ('Unresolved','Unresolved')
    ],
    default='Unresolved'
    )