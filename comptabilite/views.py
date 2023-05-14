from django.shortcuts import render,redirect
from django.views import generic
from . import forms
from . import models
from django.forms import formset_factory
from medecin import models as umodels
from django.contrib.auth.decorators import user_passes_test,login_required
from django.utils.decorators import method_decorator
from authentication.models import User
import datetime

class Home(generic.View):
    template_name = 'comptabilite/home.html'

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def get(self,request):
        return render(request, self.template_name)

class NombreCheque(generic.View):
    template_name="comptabilite/nombre_cheque.html"

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def get(self,request):
        return render(request,self.template_name)
    
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def post(self,request):
        return redirect('enregistrer_cheque',quantite=request.POST["nombre_cheque"])

class EnregistrerCheque(generic.View):
    template_name = 'comptabilite/formset.html'
    form_class = forms.ChequeForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def get(self,request,**kwargs):
        formset = formset_factory(self.form_class,extra=kwargs["quantite"])
        formset = formset()
        return render(request, self.template_name, context={'formset':formset,'message':'Enregistrer cheque'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def post(self,request,**kwargs):
        formset = formset_factory(self.
        form_class,extra=kwargs["quantite"])
        formset = formset(request.POST)
        if formset.is_valid:
            for form in formset:
                form.save()
            return redirect('home_comptabilite')
        return render(request, self.template_name, context={'formset':formset,'message':'Enregistrer cheque'})    

class EnregistrerPaiement(generic.View):
    template_name = 'comptabilite/form.html'
    form_class = forms.PaiementForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer un paiement'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            paiement = form.save(commit=False)
            if paiement.num_carte_assurance is not None :
                if paiement.num_carte_assurance.date_expiration <= datetime.date.today():
                    return render(request, self.template_name, context={'form':form,'message':'Carte d\'assurance expirée'})            
            paiement.save()
            return redirect('home_comptabilite')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer un paiement'})

class EnregistrerCarteAssurance(generic.View):
    template_name = 'comptabilite/form.html'
    form_class = forms.CarteAssuranceForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une carte d\'assurance'})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            carte_assurance = form.save()
            return redirect('home_comptabilite')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une carte d\'assurance'})

class ListePaiement(generic.ListView):
    model = models.Paiement
    template_name = 'comptabilite/liste_paiement.html'
    paginate_by = 8
    context_object_name = 'liste_paiement'

class ListeCarteAssurance(generic.ListView):
    model = models.CarteAssurance
    template_name = 'comptabilite/liste_carte_assurance.html'
    paginate_by = 8
    context_object_name = 'liste_carte_assurance'


class ListeCheque(generic.ListView):
    model = umodels.Cheque
    template_name = 'comptabilite/liste_cheque.html'
    paginate_by = 8
    context_object_name = 'liste_cheque'

class ModifierCarteAssurance(generic.View):
    template_name = 'comptabilite/form.html'
    form_class = forms.CarteAssuranceModForm
    model = models.CarteAssurance

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def get(self,request,**kwargs):
        carte = self.model.objects.get(num_carte_assurance=kwargs["id"])
        form = self.form_class(instance=carte)
        return render(request,self.template_name,context={"form":form,"message":"Modification carte d'assurance"})

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.COMPTABILITE))
    def post(self,request,**kwargs):
        carte = self.model.objects.get(num_carte_assurance=kwargs["id"])
        form = self.form_class(request.POST,instance=carte)
        if form.is_valid:
            form.save()
            return redirect("liste_carte_assurance")    
        return render(request,self.template_name,context={"form":form,"message":"Modification carte d'assurance"})