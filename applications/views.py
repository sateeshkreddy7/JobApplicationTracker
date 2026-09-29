from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import JobApplicationForm
from .models import JobApplication


@login_required
def add_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            return redirect('add_application')

    else:
        form = JobApplicationForm()

    return render(
        request,
        'applications/add_application.html',
        {'form': form}
    )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add_application')

    else:
        form = UserCreationForm()

    return render(
        request,
        'applications/register.html',
        {'form': form}
    )


@login_required
def dashboard(request):
    applications = JobApplication.objects.filter(
        user=request.user
    ).order_by('-application_date')

    search = request.GET.get('search')
    status = request.GET.get('status')

    if search:
        applications = applications.filter(
            company_name__icontains=search
        ) | applications.filter(
            job_title__icontains=search
        )

    if status:
        applications = applications.filter(status=status)

    total = applications.count()
    applied = applications.filter(status='Applied').count()
    shortlisted = applications.filter(status='Shortlisted').count()
    interview = applications.filter(status='Interview').count()
    selected = applications.filter(status='Selected').count()
    rejected = applications.filter(status='Rejected').count()

    return render(
        request,
        'applications/dashboard.html',
        {
            'applications': applications,
            'search': search,
            'status': status,
            'total': total,
            'applied': applied,
            'shortlisted': shortlisted,
            'interview': interview,
            'selected': selected,
            'rejected': rejected,
        }
    )
@login_required
def edit_application(request, id):
    application = JobApplication.objects.get(
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        form = JobApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = JobApplicationForm(instance=application)

    return render(
        request,
        'applications/edit_application.html',
        {'form': form}
    )
def delete_application(request, id):
    application = JobApplication.objects.get(
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        application.delete()
        return redirect('dashboard')

    return render(
        request,
        'applications/delete_application.html',
        {'application': application}
    )