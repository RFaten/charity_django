from django.shortcuts import render, get_object_or_404
from donors_app.models import Donors
from donors_app.forms import DonorInfoForm
from django.http import HttpResponseRedirect

# Create your views here.
def donors(request):
    donors_list = Donors.objects.order_by('-donor_name')
    donors_dict = {'donors': donors_list}
    return render(request, 'donors_app/donors.html', context=donors_dict)

def create_donor(request):
    form = DonorInfoForm()
    if request.method == 'POST':
        form = DonorInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/donors_app/')
    return render(request, 'donors_app/donor_info.html', {'form': form})

def update_donor(request, id):
    donor = get_object_or_404(Donors, id = id)
    form = DonorInfoForm(request.POST or None, instance = donor)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/donors_app/')
    return render(request, "donors_app/donor_info.html", {'form': form})

def delete_donor(request, donor_id):
    donor = get_object_or_404(Donors, id = donor_id)
    # if request.method == 'DELETE':
    donor.delete()
    return HttpResponseRedirect('/donors_app/')
