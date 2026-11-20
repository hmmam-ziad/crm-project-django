from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.db.models import Q
import logging
from django.contrib import messages

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'web/register.html', context)

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('dashboard')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'web/login.html', context)

@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    return render(request, 'web/dashboard.html', {'records': records})

def my_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record created successfully!")
            return redirect('dashboard')
    else:
        form = CreateRecordForm()

    context = {'form': form}
    return render(request, 'web/create_record.html', context)

@login_required(login_url='login')
def view_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    return render(request, 'web/view_record.html', {'record': record})

@login_required(login_url='login')
def update_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('dashboard')
    else:
        form = UpdateRecordForm(instance=record)

    context = {'form': form, 'record': record}
    return render(request, 'web/update_record.html', context)

@login_required(login_url='login')
def delete_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    record.delete()
    messages.success(request, "Record deleted successfully!")
    return redirect('dashboard')

@login_required(login_url='login')
def search_records(request):
    query = request.GET.get('query', '').strip()
    records = Record.objects.none()

    if query:
        try:
            records = Record.objects.filter(
                Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(phone__icontains=query)
            )
        except Exception as e:
            logger.error("Error occurred while searching records: %s", str(e))

    return render(request, 'web/search_results.html', {'records': records, 'query': query})