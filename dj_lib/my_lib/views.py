from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

subjects = {
    'science': 'Science Books',
    'maths': 'Maths Books',
    'English': 'English Books',
    'history': 'histoory Books'
}


# Create your views here.

def index(request):
    # htpr = {
    #     'scheme': request.scheme,
    #     'body': request.body,
    #     'path': request.path,
    #     'path_info': request.path_info
    # }
    # output = f'The HttpResponse header is {request.headers["User-Agent"]}'
    #return HttpResponse(output)

    subjects_keys = list(subjects.keys())

    return render(request, 'my_lib/index.html', {
        'subjects': subjects_keys
    })


def subject(request, subject):
    try:
        book_description = subjects[subject]
        return render(request, 'my_lib/subject.html', {
            'description': book_description,
            'subject': subject.capitalize()
        })
    except:
        raise Http404()
    return HttpResponse(book_description)


def subject_no(request, subject):
    subjects_keys = list(subjects.keys())
    redirect_subject = (subjects_keys[subject -1 ])
    if subject > len(subjects_keys):
        return HttpResponseNotFound("Invalid Subject")
    redirect_url = reverse('subject', args=[redirect_subject])
    return HttpResponseRedirect(redirect_url)
