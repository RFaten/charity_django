from django.shortcuts import render, get_object_or_404
from cases_app.models import Cases
from cases_app.forms import CaseInfoForm
from django.http import HttpResponseRedirect

# Create your views here.

def cases(request):
    cases_list = Cases.objects.order_by('-case_name')
    cases_dict = {'cases': cases_list}
    return render(request, 'cases_app/cases.html', context=cases_dict)

def create_case(request):
    form = CaseInfoForm()
    if request.method == 'POST':
        form = CaseInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'cases_app/case_info.html', {'form': form})

def update_case(request, id):
    case = get_object_or_404(Cases, id = id)
    form = CaseInfoForm(request.POST or None, instance = case)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
            # return cases(request)
    return render(request, "cases_app/case_info.html", {'form': form})

def delete_case(request, case_id):
    case = get_object_or_404(Cases, id = case_id)
    # if request.method == 'DELETE':
    case.delete()
    return HttpResponseRedirect('/')

# def delete_case(request, id):
#     case = Cases.objects.get(id=id)
#     case.delete()
#     return HttpResponseRedirect('/cases_app')
