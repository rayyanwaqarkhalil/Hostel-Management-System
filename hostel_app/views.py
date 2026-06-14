from django.shortcuts import render, redirect
from .models import Student, Room, Fee, Complaint, Warden

# just checking if my changes are uploaded to github correctly
# =========================
# DASHBOARD
# =========================

def home(request):

    context = {
        'students_count': Student.objects.count(),
        'rooms_count': Room.objects.count(),
        'fees_count': Fee.objects.count(),
        'complaints_count': Complaint.objects.count(),
        'wardens_count': Warden.objects.count(),
        'resolved_count': Complaint.objects.filter(
            status='Resolved'
        ).count(),
        'unresolved_count': Complaint.objects.filter(
            status='Unresolved'
        ).count(),
    }

    return render(request, 'home.html', context)


# =========================
# STUDENTS
# =========================

def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def add_student(request):

    rooms = Room.objects.all()

    if request.method == "POST":

        room = Room.objects.get(id=request.POST['room'])

        current_students = Student.objects.filter(room=room).count()

        if current_students >= room.capacity:
            return render(
                request,
                'add_student.html',
                {
                    'rooms': rooms,
                    'error': 'Room is Full'
                }
            )

        Student.objects.create(
            name=request.POST['name'],
            gender=request.POST['gender'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            room=room
        )

        current_students = Student.objects.filter(room=room).count()

        if current_students >= room.capacity:
            room.status = 'Full'
        else:
            room.status = 'Free'

        room.save()

        return redirect('students')

    return render(request, 'add_student.html', {'rooms': rooms})


def edit_student(request, id):

    student = Student.objects.get(id=id)
    rooms = Room.objects.all()

    if request.method == 'POST':

        student.name = request.POST['name']
        student.gender = request.POST['gender']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.address = request.POST['address']

        room = Room.objects.get(id=request.POST['room'])
        student.room = room

        student.save()

        return redirect('students')

    return render(
        request,
        'edit_student.html',
        {
            'student': student,
            'rooms': rooms
        }
    )


def delete_student(request, id):

    student = Student.objects.get(id=id)

    room = student.room

    student.delete()

    current_students = Student.objects.filter(room=room).count()

    if current_students < room.capacity:
        room.status = 'Free'
        room.save()

    return redirect('students')


# =========================
# ROOMS
# =========================

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})


def add_room(request):

    wardens = Warden.objects.all()

    if request.method == "POST":

        Room.objects.create(
            room_number=request.POST['room_number'],
            capacity=request.POST['capacity'],
            status='Free',
            warden_id=request.POST['warden']
        )

        return redirect('rooms')

    return render(request, 'add_room.html', {'wardens': wardens})


# =========================
# WARDENS
# =========================

def wardens(request):
    wardens = Warden.objects.all()
    return render(request, 'wardens.html', {'wardens': wardens})


def add_warden(request):

    if request.method == "POST":

        Warden.objects.create(
            name=request.POST['name'],
            gender=request.POST['gender'],
            phone=request.POST['phone'],
            shift_time=request.POST['shift_time']
        )

        return redirect('wardens')

    return render(request, 'add_warden.html')


# =========================
# COMPLAINTS
# =========================

def complaints(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaints.html', {'complaints': complaints})


def add_complaint(request):


    students = Student.objects.all()

    if request.method == "POST":

        Complaint.objects.create(
            student_id=request.POST['student'],
            complaint_text=request.POST['complaint_text'],
            complaint_date=request.POST['complaint_date'],
            status='Unresolved'
        )

        return redirect('complaints')

    return render(
        request,
        'add_complaint.html',
        {'students': students}

    
    )
def edit_complaint(request, id):

    complaint = Complaint.objects.get(id=id)
    students = Student.objects.all()

    if request.method == "POST":

        complaint.student_id = request.POST['student']
        complaint.complaint_text = request.POST['complaint_text']
        complaint.complaint_date = request.POST['complaint_date']
        complaint.status = request.POST['status']

        complaint.save()

        return redirect('complaints')

    return render(
        request,
        'edit_complaint.html',
        {
            'complaint': complaint,
            'students': students
        }
    )