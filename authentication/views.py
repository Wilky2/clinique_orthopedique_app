from django.shortcuts import render,redirect
from django.views import generic
from . import forms
from django.contrib.auth import login, authenticate
from . import models
from django.contrib.auth.decorators import user_passes_test,login_required
from django.utils.decorators import method_decorator

class CreateUser(generic.View):
    template_name = 'authentication/form.html'
    form_class = forms.UserForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Veuillez saisir les informations de l\'utilisateur'})
    
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('create_user')        
        return render(request, self.template_name, context={'form':form,'message':'Veuillez saisir les informations de l\'utilisateur'})

class Login(generic.View):
    template_name = 'authentication/form.html'
    form_class = forms.LoginForm

    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Veuillez saisir les informations d\'authentification'})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                if user.service is not None:
                    if user.service == models.User.ACCUEIL:
                        return redirect('home_accueil')
                    elif user.service == models.User.COMPTABILITE:
                        return redirect('home_comptabilite')
                    elif user.service == models.User.CONSULTATION:
                        return redirect('home_consultation')
                    elif user.service == models.User.HOSPITALISATION:
                        return redirect('home_hospitalisation')
                    elif user.service == models.User.IMAGERIE_MEDICALE:
                        return redirect('home_imagerie_medicale')
                    elif user.service == models.User.OPERATION:
                        return redirect('home_operation')
                    else:
                        return render(request, self.template_name, context={'form':form,'message':'Désoler, vous ne travaillez pas dans aucune service'})
                else:
                    return render(request, self.template_name, context={'form':form,'message':'Désoler, vous ne travaillez pas dans aucune service'})                   
            else:
                return render(request, self.template_name, context={'form':form,'message':'les informations d\'authentification ne sont pas valides'})
        return render(request, self.template_name, context={'form':form,'message':'Veuillez saisir les information d\'authentification'})

class DefaultHome(generic.View):
    
    def get(self,request):
        if request.user.is_authenticated:
            user = request.user
            if user.service is not None:
                    if user.service == models.User.ACCUEIL:
                        return redirect('home_accueil')
                    elif user.service == models.User.COMPTABILITE:
                        return redirect('home_comptabilite')
                    elif user.service == models.User.CONSULTATION:
                        return redirect('home_consultation')
                    elif user.service == models.User.HOSPITALISATION:
                        return redirect('home_hospitalisation')
                    elif user.service == models.User.IMAGERIE_MEDICALE:
                        return redirect('home_imagerie_medicale')
                    elif user.service == models.User.OPERATION:
                        return redirect('home_operation')
                    else:
                       return redirect('login')
            else:
                return redirect('login')
        else:
            return redirect('login')