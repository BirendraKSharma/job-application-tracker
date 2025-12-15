from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobApplication
from .forms import JobApplicationForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas


@login_required
def job_list(request):
    jobs = JobApplication.objects.filter(user=request.user)

    query = request.GET.get('q')
    status = request.GET.get('status')

    if query:
        jobs = jobs.filter(company_name__icontains=query)

    if status:
        jobs = jobs.filter(status=status)

    context = {
        'jobs': jobs,
        'query': query,
        'status': status,
    }

    return render(request, 'jobs/job_list.html', context)


@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/job_form.html', {'form': form})    


@login_required
def job_update(request, id):
    job = get_object_or_404(JobApplication, id=id, user=request.user)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
        
    else:
        form = JobApplicationForm(instance=job)

    return render(request, 'jobs/job_form.html', {'form': form})

@login_required
def job_delete(request, id):
    job = get_object_or_404(JobApplication, id=id, user=request.user)
    job.delete()
    return redirect('job_list')


@login_required
def job_pdf(request):
    reponse = HttpResponse(content_type='application/pdf')
    reponse['Content-Disposition'] = 'attachment; filename="jobs.pdf"'

    p = canvas.Canvas(reponse)

    jobs = JobApplication.objects.filter(user=request.user)

    y = 800
    p.setFont("Helvetica", 12)
    p.drawString(50, y, "My Job Applications")

    y -= 30
    for job in jobs:
        text = f"{job.company_name} - {job.position} ({job.status}) applied on {job.applied_date}"
        p.drawString(50, y, text)
        y -= 20

        if y < 50:
            p.showPage()
            y = 800

    p.showPage()
    p.save()
    return reponse
