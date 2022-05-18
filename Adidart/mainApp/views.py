
from multiprocessing import context
from django.shortcuts import render


def ChoixJoueur(request):
    jeu = request.GET.get('jeu')
    context={
        'jeu':jeu
    }

    return render(request, 'mainApp/ChoixNbJoueur.html',context)


def Game(request):
    if request.GET.get('nbPlayer') is not None:
        nbPlayer = request.GET.get('nbPlayer')
    if request.GET.get('jeu') is not None:
        jeu = request.GET.get('jeu')

    if jeu == "cricket":
        context={
            'nbPlayer':nbPlayer,
        }
        return render(request, 'mainApp/cricket.html',context)
    else :
        context={
            'nbPlayer':nbPlayer,
            'jeu':jeu,
        }
        return render(request, 'mainApp/ClassicGame.html',context)




def index(request):
    return render(request, 'mainApp/ChoixJeu.html')

    




    


