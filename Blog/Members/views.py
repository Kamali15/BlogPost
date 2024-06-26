from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic  
from django.views.generic import DetailView , CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from BlogApp.models import Profile
from BlogApp.views import *
from .forms import *

# Create your views here.



class CreateProfilePageView(CreateView):
    model = Profile 
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html "
    # fields = '__all__'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
        

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio','profile_pic','website_url','fb_url','instagram_url']
    success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/userprofile.html'

    def get_context_data(self,*args,**kwargs):
       
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        context["page_user"] = page_user
        return context
   
def Password_Success(request):
    return render(request,'registration/password_success.html')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

