from django.shortcuts import render,redirect
from django.views import generic
from . import forms
from . import models
import datetime
from consultation import models as cmodels
from django.contrib.auth.decorators import user_passes_test,login_required
from django.utils.decorators import method_decorator
from authentication.models import User

class Home(generic.View):
    template_name = 'hospitalisation/home.html'

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.HOSPITALISATION))
    def get(self,request):
        return render(request, self.template_name)

class EnregistrerHospitalisation(generic.View):
    template_name = 'hospitalisation/form.html'
    form_class = forms.HospitalisationForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.HOSPITALISATION))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une hospitalisation'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.HOSPITALISATION))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            hospitalisation = form.save(commit=False)
            if hospitalisation.date_fin_hospitalisation :
                if hospitalisation.date_fin_hospitalisation.date() <= datetime.date.today():
                    return render(request, self.template_name, context={'form':form,'message':'La de fin d\'hospitalisation est incorrecte'})
            dossier = cmodels.Dossier.objects.filter(num_patient=hospitalisation.num_patient.num_patient)
            if len(dossier) == 0 :
                return render(request, self.template_name, context={'form':form,'message':'Veuillez d\'abord créer un dossier pour ce patient'})
            else :
                dossier = dossier[0]
                if not dossier.etat_dossier:
                    return render(request, self.template_name, context={'form':form,'message':'Le dossier de ce patient est ferme'})
            hospitalisation.save()
            return redirect('home_hospitalisation')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une consultation'})

class ModifierHospitalisation(generic.View):
    template_name = 'hospitalisation/form.html'
    form_class = forms.HospitalisationModForm
    model = models.Hospitaliser

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.HOSPITALISATION))
    def get(self,request,**kwargs):
        hospitalisation = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(instance=hospitalisation)
        return render(request, self.template_name, context={'form':form,'message':'Veuillez choisir la date de fin  d\'hospitalisation'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.HOSPITALISATION))
    def post(self, request,**kwargs):
        hospitalisation = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(request.POST,instance=hospitalisation)
        if form.is_valid():
            hospitalisation = form.save(commit=False)
            if hospitalisation.date_fin_hospitalisation :
                if hospitalisation.date_fin_hospitalisation.date() <= datetime.date.today():
                    return render(request, self.template_name, context={'form':form,'message':'La de fin d\'hospitalisation est incorrecte'})
            dossier = cmodels.Dossier.objects.filter(num_patient=hospitalisation.num_patient.num_patient)
            if len(dossier) == 0 :
                return render(request, self.template_name, context={'form':form,'message':'Veuillez d\'abord créer un dossier pour ce patient'})
            else :
                dossier = dossier[0]
                if not dossier.etat_dossier:
                    return render(request, self.template_name, context={'form':form,'message':'Le dossier de ce patient est ferme'})
            hospitalisation.save()
            return redirect('liste_hospitalisation')
        return render(request, self.template_name, context={'form':form,'message':'Veuillez choisir la date de fin  d\'hospitalisation'})


class ListerHospitalisation(generic.ListView):
    model = models.Hospitaliser
    template_name = 'hospitalisation/liste_hospitalisation.html'
    paginate_by = 8
    context_object_name = 'liste_hospitalisation'