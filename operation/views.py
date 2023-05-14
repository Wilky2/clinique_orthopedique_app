from django.shortcuts import render, redirect
from django.views import generic
from . import models
from . import forms
from consultation import models as cmodels
from django.contrib.auth.decorators import user_passes_test,login_required
from django.utils.decorators import method_decorator
from authentication.models import User

class Home(generic.View):
    template_name = 'operation/home.html'
    
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.OPERATION))
    def get(self,request):
        return render(request, self.template_name)

class EnregistrerOperation(generic.View):
    template_name = 'operation/form.html'
    form_class = forms.OperationForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.OPERATION))
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une operation'})
    
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.service == User.OPERATION))
    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            operation = form.save(commit=False)
            dossier = cmodels.Dossier.objects.filter(num_patient=operation.num_patient.num_patient)
            if len(dossier) == 0 :
                return render(request, self.template_name, context={'form':form,'message':'Veuillez d\'abord créer un dossier pour ce patient'})
            else :
                dossier = dossier[0]
                if not dossier.etat_dossier:
                    return render(request, self.template_name, context={'form':form,'message':'Le dossier de ce patient est ferme'})
            operation.save()
            return redirect('home_operation')
        return render(request, self.template_name, context={'form':form,'message':'Enregistrer une operation'})

class ListerOperation(generic.ListView):
    model = models.Operer
    template_name = 'operation/liste_operation.html'
    paginate_by = 8
    context_object_name = 'liste_operation'