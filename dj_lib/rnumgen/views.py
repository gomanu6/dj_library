from django.shortcuts import render


rnums = {
    'A123': 'Yes',
    'A124': 'No',
    'A125': 'Maybe'
}

# Create your views here.


def rnum_index(request):
    rnumkeys = list(rnums.keys())
    context = {
        'nums': rnumkeys
    }
    return render(request, 'rnumgen/rnums.html', context)