from django.shortcuts import render, redirect, HttpResponse
import random
from time import strftime, localtime
def index(request):
    if 'goldcount' in request.session:
        request.session['goldcount'] = request.session['goldcount'] 
    else:
        request.session['goldcount'] = 0
    if 'activities' in request.session:
        pass
    else:
        request.session['activities'] = "Welcome to Ninja Gold.  This is your activity log, where the amount of gold you won or lost will be displayed.  Good luck!"
    if 'turns' in request.session:
        pass
    else:
        request.session['turns'] = 0
    if request.session['goldcount'] >= 500:
        request.session['activities'] = request.session['activities'] + f"\nCongratulations!  You won Ninja Gold!"
    if request.session['turns'] == 25 and request.session['goldcount'] < 500:
        request.session['activities'] = request.session['activities'] + f"\nSorry, you lost...click start over to play again!"
    return render(request, "main_app/index.html")
def process(request):
    destiny = random.randint(1, 2)
    goldamountfarm = random.randint(10, 20)
    goldamountcave = random.randint(5, 10)
    goldamounthouse = random.randint(2, 5)
    goldamountcasino = random.randint(0, 50)
    time = strftime("%b %d, %Y %H:%M %p", localtime())
    if request.session['turns'] <= 24:
        if request.POST['location'] == 'farm':
            request.session['goldcount'] = request.session['goldcount'] + goldamountfarm
            request.session['activities'] = request.session['activities']  + f"\nEarned {goldamountfarm} golds from the farm! ({time})"
            request.session['turns'] = request.session['turns'] + 1
        if request.POST['location'] == 'cave':
            request.session['goldcount'] = request.session['goldcount'] + goldamountcave
            request.session['activities'] = request.session['activities']  + f"\nEarned {goldamountcave} golds from the cave! ({time})"
            request.session['turns'] = request.session['turns'] + 1
        if request.POST['location'] == 'house':
            request.session['goldcount'] = request.session['goldcount'] + goldamounthouse
            request.session['activities'] = request.session['activities']  + f"\nEarned {goldamounthouse} golds from the house! ({time})"
            request.session['turns'] = request.session['turns'] + 1
        if request.POST['location'] == 'casino':
            if destiny == 1:
                request.session['goldcount'] = request.session['goldcount'] - goldamountcasino
                request.session['activities'] = request.session['activities']  + f"\nLost {goldamountcasino} golds from the casino :(... ({time})"
                request.session['turns'] = request.session['turns'] + 1
            elif destiny == 2:
                request.session['goldcount'] = request.session['goldcount'] + goldamountcasino
                request.session['activities'] = request.session['activities']  + f"\nEarned {goldamountcasino} golds from the casino! ({time})"
                request.session['turns'] = request.session['turns'] + 1
            else:
                pass
    return redirect('/')
def reset(request):
    if 'goldcount' and 'activities' and 'turns' in request.session:
        del request.session['goldcount']
        del request.session['activities']
        del request.session['turns']
    else:
        pass
    return redirect('/')

# Create your views here.
