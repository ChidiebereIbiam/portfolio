from django.shortcuts import redirect, render
from .models import Profile, Service, Education, Experience, Skills, Contact, Project
from django.core.mail import send_mail

# Create your views here.

def home(request):
    profile = Profile.objects.all()[0]
    service = Service.objects.all()
    education = Education.objects.all().order_by('-id')
    experience = Experience.objects.all().order_by('-id')
    skill1 = Skills.objects.all()[0:3]
    skill2 = Skills.objects.all()[3:6]
    contact = Contact.objects.all()[0]
    project = Project.objects.all().order_by('-id')
    project_count = Project.objects.all().count()


    if request.method == "POST":
        name = request.POST['name']
        email_from = request.POST['email']
        message = request.POST['form-message']
        recipient_list = ['chidiebereorjiibiam7@gmail.com',]

        new_subject = f"Message - from {name}"

        send_mail(new_subject, message, email_from, recipient_list)
        print("Sent")

        redirect("home")
        
    context = {
        'profile': profile,
        'services': service,
        'educations':education,
        'experiences':experience,
        "skill1":skill1,
        "skill2":skill2,
        "contact":contact,
        'projects':project,
        'project_count': project_count,
    }
    return render(request, "core/index.html", context)


    


def project_detail(request, id):
    project = Project.objects.get(id = id)
    return render(request, "core/project-detail.html", {"project":project})