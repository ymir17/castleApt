from django.shortcuts import render, redirect
from django.core.mail import send_mail
from contactus.forms.forms import MailForm


def index(request):
    if request.method == 'POST':
        form = MailForm(data=request.POST)
        name = form.fields['name']
        email = form.fields['email']
        phoneNo = form.fields['phoneNo']
        message = form.fields['message']
        subject = 'Subject: Contact Us'
        send_mail(subject, message, email, ['contact.castleapt@gmail.com'])
        return redirect('home-index')
    else:
        form = MailForm()
    return render(request, 'Contact_us/contactus.html', {'form': form})

def sendMail(request):
    if request.method == 'POST':
        form = MailForm(data=request.POST)
        print(form.fields['message'])
    else:
        print('Not POST')
