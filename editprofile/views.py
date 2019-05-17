from django.shortcuts import render, HttpResponseRedirect
from editprofile.forms.forms import editProfileForm, UpdateProfile
from django.views.generic.edit import UpdateView
from signup.models import Accounts, Users



# Create your views here.
def index(request):
    return render(request, 'editprofile/editprofile.html')


def profile(request):
    args = {}
    current = request.user
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        form.actual_user = request.user
        editprofile = editProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            editprofile.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = UpdateProfile()
        editprofile = editProfileForm()
        args['form'] = form
    return render(request, 'editprofile/editprofile.html', {
        'form': args,
        'forms': editprofile,
        'current': current,
        'users': Users.objects.all(),
        'accounts': Accounts.objects.all()
    })




