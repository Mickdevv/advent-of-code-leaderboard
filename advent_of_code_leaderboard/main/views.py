from django.shortcuts import render, redirect
from .forms import UserSubmissionForm
from .models import Submission, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from datetime import datetime

def calculateScores():
    submissionWeekends = [1, 7, 8, 14, 15, 21, 22, 25]
    submissions = Submission.objects.all().order_by('-createdAt')
    approvedSubmissions = Submission.objects.all().filter(approved=True).order_by('createdAt')
    users = User.objects.all()
    profiles = UserProfile.objects.all()
    sCounts = {}
    for p in profiles:
        p.score = 0
        p.save()
        
    for s in approvedSubmissions:
        key = f'{s.day}-{s.part}'
        sUser = s.user
        profile = getattr(sUser, 'profile', None)  
        
        print(s.user.username, profile.score, s.createdAt, s.day, s.part)
        
        if s.day not in submissionWeekends:
            if key not in sCounts:
                print("First for ", key)
                sCounts[key] = 1
                profile.score += 2
            elif sCounts[key] == 1:
                print("Second for ", key)
                sCounts[key] += 1
                profile.score += 1
                
            if s.part == 2:
                keyP1 = f'{s.day}-{1}'
                if keyP1 not in sCounts:
                    print("First for ", keyP1)
                    sCounts[keyP1] = 1
                    profile.score += 2
                elif sCounts[keyP1] == 1:
                    print("Second for ", keyP1)
                    sCounts[keyP1] += 1
                    profile.score += 1
                    
            if s.createdAt.day == s.day:
                profile.score+=1
                
        profile.score += s.part
        if s.part == 2 and len(submissions.filter(user=sUser).filter(day=s.day).filter(part=1)) == 0:
            print(sUser, submissions.filter(user=sUser).filter(day=s.day).filter(part=1))
            profile.score += 1
            if s.createdAt.day == s.day:
                profile.score+=1
            
        
        print(sUser.username, profile.score)
        print()
            
        profile.save()
        
    users = sorted(users, key=lambda user: user.profile.score, reverse=True)
    return users, submissions

@login_required(login_url='/login')
def leaderboard(request):
    users, submissions = calculateScores()
    completedSubmissions = []
    for sub in submissions:
        if sub.approved and sub.user == request.user:
            for allSubs in submissions:
                if allSubs.day == sub.day and allSubs.part == sub.part:
                    completedSubmissions.append(allSubs)
    return render(request, 'leaderboard.html', {'submissions': submissions, 'users': users, 'completedSubmissions': completedSubmissions})

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