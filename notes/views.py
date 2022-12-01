from django.shortcuts import redirect, render
from notes.models import Notes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginDjango, logout
from .forms import *

current_user = ''

# Create your views here.
def home(request):
    context = {
        'loggedIn': False
    }
    if request.user.is_authenticated:
            current_user = request.user
            notes = Notes.objects.filter(owner=current_user.id, archived=False)
            context = {
                'notes': notes, 
                'loggedIn': True
            }


    return render(request, 'home.html', context)


def archivedNotes(request):
    notes = Notes.objects.filter(owner=request.user.id, archived=True)
    msg = ''
    # print(notes[0])
    if (not notes):
        msg = 'There are no archived notes'
    print(msg)
    context = {
        'notes': notes,
        'message': msg
    }
    return render(request, 'archived.html', context)


def createNoteTemp(request):
    return render(request, 'createNote.html')


def CreateNote(request):
    note = Notes.objects.all()
    title = request.POST.get('title')
    content = request.POST.get('content')

    note.create(title=title, content=content, owner=request.user)
    return redirect('home')

def updateNoteTemp(request, id):
    #bring specified note
    note = Notes.objects.filter(id=id).first()
    print(request.user)

    context = {
        'title': note.title,
        'content': note.content,
        'id': note.id,
        'name': request.user.username
    }
    print(note.title)

    return render(request, 'updateNote.html', context)


def updateNotePost(request, id):
    note = Notes.objects.filter(id=id)

    #updating note:
    title = request.POST.get('title')
    content = request.POST.get('content')

    note.update(title=title, content=content)

    return redirect('home')

def deleteNote(request, id):
    note = Notes.objects.filter(id=id)

    #delete note:
    # note.delete()
    
    # archive note:
    note.update(archived=True)

    return redirect('home')

def restoreNote(request, id):
    note = Notes.objects.filter(id=id)

    # Restore
    note.update(archived=False)

    return redirect('archived')


def signupTemp(request):
    return render(request, 'Signup.html')


# Create user

def UserRegisterPost(request):
    # retreive data
    email = request.POST.get('email')
    password = request.POST.get('password')
    username = request.POST.get('username')

    # create user
    user = User.objects
    user.create_user(username=username, email=email, password=password)
    

    for i in user.all():
        print(i.password)

    # redirect
    return redirect('home')


# Login user

def login(request):
    login_form = LoginForm()
    print(login_form)
    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)

def loginPost(request):
    password = request.POST.get('password')
    username = request.POST.get('username')

    # login user
    user = authenticate(username=username, password=password)
    if user is not None:
        username = user.get_username()
        loginDjango(request, user)
        context = {
            'username': username
        }
        return redirect('home')
    else:
        return redirect('login')


def logoutUser(request):
    logout(request)
    return redirect('login')