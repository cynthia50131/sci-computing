"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )


from app.forms import BootstrapCurveFittingForm
def T1LL_input(request):

    return render(
        request,
        'app/fitting_input.html',
        context_instance = RequestContext(request,
        {
            'title':'Fitting Input',
            'form': BootstrapCurveFittingForm,
               })
    )


def T1LL_result(request):
    import pyFitMR.Fitting_lib as FB

    t_value = request.POST.get('t_value')
    y_value = request.POST.get('y_value')
    fitted_result_dict = FB.T1fitting(t_value, y_value)
    return render(
        request,
        'app/fitting_result.html',
        context_instance = RequestContext(request, fitted_result_dict)
       )


def boston_input(request):

    return render(
        request,
        'app/boston_input.html',
        context_instance = RequestContext(request,
        {
            'title':'Fitting Input',
            'form': BootstrapCurveFittingForm,
               })
    )
def boston_result(request):
    import pyFitMR.boston_lib as FB
    from django.conf import settings
    import os
    import numpy
    from sklearn.externals import joblib

    CRIM = request.POST.get('CRIM')
    ZN = request.POST.get('ZN')
    INDUS = request.POST.get('INDUS')
    CHAS = request.POST.get('CHAS')
    NOX = request.POST.get('NOX')
    RM = request.POST.get('RM')
    AGE = request.POST.get('AGE')
    DIS = request.POST.get('DIS')
    RAD = request.POST.get('RAD')
    TAX = request.POST.get('TAX')
    PTRATIO = request.POST.get('PTRATIO')
    B = request.POST.get('B')
    LSTAT = request.POST.get('LSTAT')

    if not TAX:
        CRIM=1.6566
        ZN=0
        INDUS=19.58
        CHAS=0.
        NOX=0.871
        RM=6.122
        AGE=97.3
        DIS=1.618
        TAX=5.
        RAD=403.
        PTRATIO=14.7
        B=372.8
        LSTAT=14.1
        #X = numpy.array([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, TAX, RAD, PTRATIO, B, LSTAT], dtype = numpy.float64)
        X = [1.6566, 0., 19.58, 0., 0.871 , 6.122, 97.3, 1.618, 5., 403., 14.7, 372.8, 14.1]

    else:
        X = numpy.array([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, TAX, RAD, PTRATIO, B, LSTAT], dtype = numpy.float64)

    lr = joblib.load(os.path.join(settings.PROJECT_ROOT, 'app', 'lrmachine.pkl'))
    MEDV = lr.predict(X)

    result_dict = FB.boston(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, TAX, RAD, PTRATIO, B, LSTAT, MEDV)


    return render(
        request,
        'app/boston_result.html',
        context_instance = RequestContext(request, result_dict)
       )
