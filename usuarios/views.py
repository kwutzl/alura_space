from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

# Create your views here.
def login(request):
    form = LoginForms()
    context = {
        'form': form
    }
    return render(request, 'usuarios/login.html', context)


def cadastro(request):
    form = CadastroForms()
    context = {
        'form': form
    }
    return render(request, 'usuarios/cadastro.html', context)