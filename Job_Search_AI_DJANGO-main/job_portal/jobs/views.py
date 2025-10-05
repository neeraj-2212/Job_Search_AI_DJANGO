from django.shortcuts import render, redirect
from django.urls import reverse
from .models import JobModel,JobPost,FeedModel,CommentModel
from .forms import UserForm, JobPostForm,FeedForm,CommentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from PyPDF2 import PdfReader
import os
from django.conf import settings
from urllib.parse import unquote
from datetime import datetime


def home(request):
    comp_name = JobPost.objects.values('company_name').distinct()
    titles = JobPost.objects.values('job_title').distinct()
    data = JobModel.objects.all().distinct()
    all_data = JobPost.objects.all()
    if(request.method=="POST"):
        selected_company = ""
        selected_company = request.POST["selected_company"]
        selected_region = request.POST["selected_job_region"]
        selected_type = request.POST["selected_type"]
        
        if(selected_company == "Anywhere"):
            all_data = JobPost.objects.all()
            return render(request, "home.html", {'all_datas':all_data,'titless':titles,'comp_names':comp_name,'datas': data})
        else:
            all_datas2 = JobPost.objects.get(company_name=selected_company)
        
        filtered_data = {'s_company_name':selected_company}
        return render(request, "home.html", {'titless':titles,'comp_names':comp_name,'datas': data,'f_data':filtered_data,'filtered_datas':all_datas2})
    return render(request, "home.html", {'all_datas':all_data,'titless':titles,'comp_names':comp_name,'datas': data})
    
def upload_resume(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        resume_file = request.FILES['resume']
        fs = FileSystemStorage()
        filename = fs.save(resume_file.name, resume_file)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        # Open and read the PDF
        # uploaded_file_url looks like '/media/filename.pdf'
        relative_path = uploaded_file_url.replace('/media/', '')  # remove the media URL prefix
        # Decode URL-encoded characters like '%20' → ' '
        decoded_path = unquote(relative_path)
        # Build full path using MEDIA_ROOT
        full_path = os.path.join(settings.MEDIA_ROOT, decoded_path)
    with open(full_path, 'rb') as pdf_file:
        
        reader = PdfReader(pdf_file)
        page = reader.pages[0]
        text = page.extract_text()

        # Keywords you want to search for
        keywords = ['python', 'java']  # lowercase for case-insensitive match

        # Convert text to lowercase and check if any keyword exists
        if any(keyword in text.lower() for keyword in keywords):
            data = JobPost.objects.filter(job_title="Python Developer")
            print("You are a Python Developer")
        else:
            data = JobPost.objects.all()
            print("You are not a Python Developer")

# Don't forget to close the file
        pdf_file.close()
        # You can do more here, like saving to a model
    return render(request, 'home.html', {'uploaded_file_url': uploaded_file_url,'file_data':data})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Existing user - login
            login(request, user)
            return redirect("home")
        else:
            # New user - create and login
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect("home")
            else:
                # Username exists but wrong password
                return render(request, "login.html", {"error": "Invalid credentials or user already exists."})
    return render(request, "login.html")


def custom_logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('home')
    return render(request, 'confirm_logout.html')


def about_view(request):
    return render(request, 'about.html')


def job_single(request):
    return render(request, 'job_single.html')

def pjob_single(request,id):
   
    data = JobPost.objects.get(id=id)
    
    return render(request,'job_single.html',{'datass':data})


def job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to any success page
    else:
        form = JobPostForm()

    # Passing fixed job regions
    datas = JobModel.objects.all()

    return render(request, 'job_post.html', {'form': form, 'datas': datas})
    

def services(request):
    return render(request, 'services.html')

def services_single(request):
    return render(request, 'services_single.html')

def blog_single(request):
    total_comments = CommentModel.objects.count()
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')

        CommentModel.objects.create(
            name=name,
            email=email,
            website=website,
            message=message,
            Image='comment_images/default.jpg',  # fixed image
            date=datetime.now()
        )

        comments = CommentModel.objects.all().order_by('-date')
        return render(request, 'blog_single.html', {'comments': comments ,'total_comments': total_comments})  # or show success message

    return render(request, 'blog_single.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_single(request):
    return render(request, 'portfolio_single.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def faq(request):
    return render(request, 'faq.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if(request.method == 'POST'):
        form = FeedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to any success page
    else:
        form = FeedForm()
    return render(request, 'contact.html', {'form': form})
