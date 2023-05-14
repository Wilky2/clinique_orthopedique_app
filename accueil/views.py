from django.shortcuts import render, redirect
from django.views import generic
from . import forms
from . import models
from comptabilite import models as cmodels
from django.contrib.auth.decorators import user_passes_test,login_required
from django.utils.decorators import method_decorator
from authentication.models import User
import datetime

class Home(generic.View):
    template_name = 'accueil/home.html'
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def get(self,request):
        return render(request, self.template_name)

class EnregistrerVisite(generic.View):
    template_name = 'accueil/form.html'
    form_class = forms.VisiteForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une visite'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            visite = form.save()
            return redirect('home_accueil')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une visite'})


class EnregistrerPatient(generic.View):
    template_name = 'accueil/form.html'
    form_class = forms.PatientForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer un patient'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            if patient.date_naissance > datetime.date.today():
                return render(request, self.template_name, context={'form':form,'message':'La date de naissance est incorrecte'})
            if not ("existe" in request.POST) :
                liste_patient = models.Patient.objects.filter(nom_patient=patient.nom_patient,prenom_patient=patient.prenom_patient)
                if len(liste_patient) > 0 :
                    return render(request,self.template_name,context={'form':form,'existe':'oui','message':'Un patient avec le meme nom et le meme prenom est deja enregistrer, voulez-vous quand meme enregistrer'})
            patient.save()
            return redirect('enregistrer_responsable',num_patient=patient.num_patient)
        return render(request,self.template_name,context={'form':form,'message':'Enregistrer un patient'})

class EnregistrerResponsable(generic.View):
    template_name = 'accueil/form.html'
    form_class = forms.ResponsableForm
    form_accompagner = forms.AccompagnerForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def get(self,request,**kwargs):
        form = self.form_class()
        form_accompagner = self.form_accompagner()
        return render(request, self.template_name, context={'form':form,'form_accompagner':form_accompagner,'message':'Saisir les informations du responsable du patient'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def post(self, request,**kwargs):
        form_accompagner = self.form_accompagner()
        form = self.form_class()
        if "form_accompagner" in request.POST :
            form_accompagner = self.form_accompagner(request.POST)
            print("a======================================================")
            print(request.POST)
            if form_accompagner.is_valid():
                accompagner = form_accompagner.save(commit=False)
                accompagner.num_patient = models.Patient.objects.get(num_patient=kwargs["num_patient"])
                accompagner.save()
                return redirect('home_accueil')
        else:
            form = self.form_class(request.POST)
            print("b======================================================")
            print(request.POST)
            if form.is_valid():
                responsable = form.save()
                patient = models.Patient.objects.get(num_patient=kwargs["num_patient"])
                accompagner = models.Accompagner(num_patient=patient, num_responsable=responsable)
                accompagner.save()
                return redirect('home_accueil')
        return render(request,self.template_name,context={'form':form,'form_accompagner':form_accompagner,'message':'Saisir les informations du responsable du patient'})

class ListePatient(generic.ListView):
    model = models.Patient
    template_name = 'accueil/liste_patient.html'
    paginate_by = 8
    context_object_name = 'liste_patient'

class ListeResponsable(generic.ListView):
    model = models.Responsable
    template_name = 'accueil/liste_responsable.html'
    paginate_by = 8
    context_object_name = 'liste_responsable'

    def get_queryset(self):
        if 'num_patient' in self.kwargs:
            accompagners = models.Accompagner.objects.filter(num_patient=models.Patient.objects.get(num_patient=self.kwargs["num_patient"]))
            responsable = []
            for accompagner in accompagners:
                responsable.append(accompagner.num_responsable)
            return responsable
        return self.model.objects.none()

class ListeVisite(generic.ListView):
    model = cmodels.Visite
    template_name = 'accueil/liste_visite.html'
    paginate_by = 8
    context_object_name = 'liste_visite'

class ModifierPatient(generic.View):
    template_name = 'accueil/form.html'
    form_class = forms.PatientForm
    model = models.Patient

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def get(self,request,**kwargs):
        patient = self.model.objects.get(num_patient=kwargs["id"])
        form = self.form_class(instance=patient)
        return render(request,self.template_name,context={"form":form,"message":"Modification patient"})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def post(self,request,**kwargs):
        patient = self.model.objects.get(num_patient=kwargs["id"])
        form = self.form_class(request.POST,instance=patient)
        if form.is_valid:
            patient = form.save(commit=False)
            if patient.date_naissance > datetime.date.today():
                return render(request, self.template_name, context={'form':form,'message':'La date de naissance est incorrecte'})
            patient.save()
            return redirect("choix_patient")    
        return render(request,self.template_name,context={"form":form,"message":"Modification patient"})

class ChoixPatient(generic.ListView):
    model = models.Patient
    template_name = 'accueil/liste_patient_mod.html'
    paginate_by = 8
    context_object_name = 'liste_patient'

class ModifierResponsable(generic.View):
    template_name = 'accueil/form.html'
    form_class = forms.ResponsableForm
    model = models.Responsable

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def get(self,request,**kwargs):
        responsable = self.model.objects.get(num_responsable=kwargs["id"])
        form = self.form_class(instance=responsable)
        return render(request,self.template_name,context={"form":form,"message":"Modification responsable"})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.ACCUEIL))
    def post(self,request,**kwargs):
        responsable = self.model.objects.get(num_responsable=kwargs["id"])
        form = self.form_class(request.POST,instance=responsable)
        if form.is_valid:
            form.save()
            return redirect("choix_responsable")    
        return render(request,self.template_name,context={"form":form,"message":"Modification responsable"})

class ChoixResponsable(generic.ListView):
    model = models.Responsable
    template_name = 'accueil/liste_responsable_mod.html'
    paginate_by = 8
    context_object_name = 'liste_responsable'