from django.shortcuts import render, redirect
from .forms import UserSubmissionForm
from .models import Submission, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from datetime import datetime

def calculateScores():
    submissionWeekends = ['Day 1', 'Day 7', 'Day 8', 'Day 14', 'Day 15', 'Day 21', 'Day 22', 'Day 25']
    submissions = Submission.objects.all().filter(approved=True).order_by('createdAt')
    users = User.objects.all().filter(is_staff=False)
    profiles = UserProfile.objects.all()
    sCounts = {}
    for p in profiles:
        p.score = 0
        p.save()
        
    for s in submissions:
        key = f'{s.day}-{s.part}'
        key = f'{s.day}-{s.part}'
        sUser = s.user
        profile = getattr(sUser, 'profile', None)   
        profile.score = 0         
        if key not in sCounts:
            if s.day not in submissionWeekends:
                if s.part == 1:
                    sUser.score += 3
                elif s.part == 2:
                    sUser.score += 4
            else:
                if s.part == 1:
                    sUser.score += 1
                elif s.part == 2:
                    sUser.score += 2
                
            sCounts[key] = 1
        else:
            if sCounts[key] == 1 and s.day not in submissionWeekends:
                sUser.score += 1

            if s.part == 1:
                sUser.score += 2
            elif s.part == 2:
                sUser.score += 1
            
        profile.save()
    print(sCounts)    
        
    return users, submissions

@login_required(login_url='/login')
def leaderboard(request):
    users, submissions = calculateScores()
    return render(request, 'leaderboard.html', {'submissions': submissions, 'users': users})

@login_required(login_url='/login')
def submission(request):
    return render(request, 'submission.html')

@login_required(login_url='/login')
def submission(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.approved = False
            submission.save() 
            return redirect('home')
    else:
        form = UserSubmissionForm()
    return render(request, 'submission.html', {'form': form})

    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='/login')
def upload_image(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            user_image = form.save(commit=False)
            user_image.user = request.user
            user_image.save()
            return redirect('submissions')
    else:
        form = UserSubmissionForm()
    return render(request, 'upload_image.html', {'form': form})

@login_required(login_url='/login')
def image_list(request):
    images = UserSubmissionForm.objects.filter(user=request.user)
    return render(request, 'image_list.html', {'images': images})


@login_required(login_url='/login')
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        data = request.POST
        if form.is_valid():
            password = data["new_password1"]
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = PasswordChangeForm(user)
        
    return render(request, 'registration/password-change-form.html', {"form": form})