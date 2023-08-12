from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import openai
from django.db.models import Q
from builder.models import Users, Contact
from django import forms
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Applicant, Document, Product
from django.shortcuts import render
from django.contrib import messages

 

# Create your views here.
def home(request):
    return render(request, 'builder/home.html')

def base(request):
    return render(request, 'base.html')

def ai(request):
    return render(request, 'builder/ai.html')
    
def signup(request):
    return render(request, 'builder/signup.html')

def login(request):
    return render(request, 'builder/login.html')

def builder(request):
    products = Product.objects.all()
    return render(request, 'builder/builder.html', {'products': products})
 
    
def process(request):
    return render(request, 'builder/process_docx.html')

def about(request):
    return render(request, 'builder/aboutus.html')

def template1(request):
    return render(request, 'builder/resumeXtemplates/template1.html')

def contact(request):
    return render(request, 'builder/contact.html')

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'builder/editResume.html', {'product': product})

# ChatGPT integratoin

# Configure your OpenAI API key
openai.api_key = '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'

@csrf_exempt
def generate_chat_response(request):
    if request.method == 'POST':
        # Get user input from the POST request
        user_input = request.POST.get('user_input')

        # Call the Chat GPT API to generate a response
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the generated response from the API response
        generated_response = response.choices[0].text.strip()

        # Prepare the response data
        data = {
            'response': generated_response,
        }

        # Return the response as JSON
        return JsonResponse(data)

    return render(request, 'builder/ai.html')


# signup

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        # Perform validation and create a new signup record
        # You can add your own validation logic here

        signup = Users(name=name, email=email, contact=contact, password=password)
        a = Users.objects.filter(email=email)
        if len(a) == 0:
            signup.save()
            return redirect('login')
        else:
            message = "User already exists. Please use a different email."
            return render(request, 'builder/signup.html', {'message': message})
    return render(request, 'builder/signup.html')



# login
def login_view(request):
    if request.method == "POST":
        identifier = request.POST.get('identifier')  # Get the identifier (name, email, or contact)
        password = request.POST['password']

        # Check if the identifier matches name, email, or contact
        data = Users.objects.filter(Q(name=identifier) | Q(email=identifier)).first()

        if data and data.password == password:
            request.session['email'] = data.email
            request.session['name'] = data.name
            request.session['is_logged_in'] = True  # Set the session flag
            return redirect('home')
        else:
            message = "* Invalid username or password. Please try again"
           
            return render(request, 'builder/login.html', {'message': message})

    return render(request, 'builder/login.html')



def logout (request):
    if 'email' in request.session:
        del request.session['email']
    
    if 'is_logged_in' in request.session:
        del request.session['is_logged_in']
    
    return redirect('home')






def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'builder/process_docx.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'builder/home.html', {'documents': documents})

# Add the following code at the end of views.py


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file')
        
        
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        print("name:", name)
        print("email:", email)
        print("phone:", phone)
        print("content:", content)

        contact_instance = Contact.objects.create(
            name=name, email=email, phone=phone, content=content)
        contact_instance.save()
        message='Message Sent Succesfully'
        return render(request, 'builder/contact.html', {'message': 'Message Sent Successfully'})
    else:
        return render(request, 'builder/contact.html')

 

def applicant_form(request):
    class ApplicantForm(forms.ModelForm):
        class Meta:
            model = Applicant
            fields = '__all__'
    
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
            return render(request, 'builder/builder.html', {'form': form})
    else:
        form = ApplicantForm()
    
    return render(request, 'builder/builder.html', {'form': form})

 
