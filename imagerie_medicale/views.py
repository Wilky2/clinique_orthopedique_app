from django.shortcuts import render, redirect
from django.views import generic
from . import forms
from . import models
from consultation import models as cmodels
from django.contrib.auth.decorators import user_passes_test,login_required
from django.utils.decorators import method_decorator
from authentication.models import User
import datetime

class Home(generic.View):
    template_name = 'imagerie_medicale/home.html'

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.IMAGERIE_MEDICALE))
    def get(self,request):
        return render(request, self.template_name)

class EnregistrerExamen(generic.View):
    template_name = 'imagerie_medicale/form.html'
    form_class = forms.ExamenForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.IMAGERIE_MEDICALE))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer un examen'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.IMAGERIE_MEDICALE))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            examen = form.save(commit=False)
            dossier = cmodels.Dossier.objects.filter(num_patient=examen.num_patient.num_patient)
            if len(dossier) == 0 :
                return render(request, self.template_name, context={'form':form,'message':'Veuillez d\'abord créer un dossier pour ce patient'})
            else :
                dossier = dossier[0]
                if not dossier.etat_dossier:
                    return render(request, self.template_name, context={'form':form,'message':'Le dossier de ce patient est ferme'})
            examen.save()
            return redirect('home_imagerie_medicale')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer un examen'})

class EnregistrerPrescription(generic.View):
    template_name = 'imagerie_medicale/form.html'
    form_class = forms.PrescriptionForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.IMAGERIE_MEDICALE))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une prescription'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.IMAGERIE_MEDICALE))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            prescription = form.save()
            return redirect('home_imagerie_medicale')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une prescription'})


class EnregistrerRendezVous(generic.View):
    template_name = 'imagerie_medicale/form.html'
    form_class = forms.RendezVousForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.IMAGERIE_MEDICALE))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer un rendez vous'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.IMAGERIE_MEDICALE))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            rendez_vous = form.save(commit=False)
            if rendez_vous.date_rendez_vous.date() <= datetime.date.today():
                return render(request, self.template_name, context={'form':form,'message':'date rendez vous incorrect'})
            rendez_vous.save()
            return redirect('home_imagerie_medicale')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer un rendez vous'})


class ListerExamen(generic.ListView):
    model = models.Examiner
    template_name = 'imagerie_medicale/liste_examen.html'
    paginate_by = 8
    context_object_name = 'liste_examen'

class ListerPrescription(generic.ListView):
    model = models.Prescription
    template_name = 'imagerie_medicale/liste_prescription.html'
    paginate_by = 8
    context_object_name = 'liste_prescription'

class ListerRendezVous(generic.ListView):
    model = models.RendezVous
    template_name = 'imagerie_medicale/liste_rendez_vous.html'
    paginate_by = 8
    context_object_name = 'liste_rendez_vous'