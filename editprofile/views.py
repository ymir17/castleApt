from django.shortcuts import render, HttpResponseRedirect
from editprofile.forms.forms import editProfileForm, UpdateProfile
from django.views.generic.edit import UpdateView



# Create your views here.

def index(request):
    args = {}
    current = request.user
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = UpdateProfile()
    args['form'] = form
    return render(request, 'editprofile/editprofile.html', {
        'form': args,
        'forms': editProfileForm,
        'current': current,
    })




