from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Parties, Voters

@login_required
def index(request):
    if request.user.is_voters:
        return render(request, 'home.html')
    return render(request, 'logout.html')


@login_required
def login(request):
    if request.user.is_voters:
        return render(request, 'home.html')
    return render(request, 'login.html')


@login_required()
def select(request):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    ass = assc.assign
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
        'assc': assc,
    }
    return render(request, 'info/t_attendance.html', context)