from django.shortcuts import render, redirect
from django.views import generic
from . import forms
from . import models
from django.contrib.auth.decorators import user_passes_test,login_required
from django.utils.decorators import method_decorator
from authentication.models import User

class Home(generic.View):
    template_name = 'consultation/home.html'

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.CONSULTATION))
    def get(self,request):
        return render(request, self.template_name)

class EnregistrerConsultation(generic.View):
    template_name = 'consultation/form.html'
    form_class = forms.ConsultationForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.CONSULTATION))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une consultation'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.CONSULTATION))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            dossier = models.Dossier.objects.filter(num_patient=consultation.num_patient.num_patient)
            if len(dossier) == 0 :
                return render(request, self.template_name, context={'form':form,'message':'Veuillez d\'abord créer un dossier pour ce patient'})
            else :
                dossier = dossier[0]
                if not dossier.etat_dossier:
                    return render(request, self.template_name, context={'form':form,'message':'Le dossier de ce patient est ferme'})
            consultation.save()
            return redirect('home_consultation')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une consultation'})

class EnregistrerDossier(generic.View):
    template_name = 'consultation/form.html'
    form_class = forms.DossierForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.CONSULTATION))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer un dossier'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.CONSULTATION))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            dossier = form.save()
            return redirect('home_consultation')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer un dossier'})

class ListerConsultation(generic.ListView):
    model = models.Consulter
    template_name = 'consultation/liste_consultation.html'
    paginate_by = 8
    context_object_name = 'liste_consultation'

class ListerDossier(generic.ListView):
    model = models.Dossier
    template_name = 'consultation/liste_dossier.html'
    paginate_by = 8
    context_object_name = 'liste_dossier'