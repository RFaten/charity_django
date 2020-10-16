from django.shortcuts import render, get_object_or_404
from donations_app.models import Donations
from donations_app.forms import DonationInfoForm
from django.http import HttpResponseRedirect
from django.db.models import Count, Sum
from django.urls import reverse

# Create your views here.
def donations(request):
    donations_list = Donations.objects.values('case_name__case_name', 'case_name').annotate(donation_amount = Sum('donation_amount'))
    # print(donations_list)
    # donations_list = Donations.objects.all().annotate(dcount=Count('donation_amount'))
    # donations_list = Donations.objects.all()
    donations_dict = {'donations': donations_list}
    return render(request, 'donations_app/donations.html', context=donations_dict)

def create_donation(request):
    form = DonationInfoForm()
    if request.method == 'POST':
        form = DonationInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/donations_app/')
    return render(request, 'donations_app/donation_info.html', {'form': form})

def update_donation(request, id):
    donations_list = Donations.objects.filter(case_name=id)
    donations_dict = {'donations': donations_list}
    return render(request, 'donations_app/donation_detail.html', context=donations_dict)

def delete_donation(request, donation_id):
    donation = get_object_or_404(Donations, id = donation_id)
    donation.delete()
    return HttpResponseRedirect(reverse('update_donation', kwargs={'id':donation.case_name.id}))
    # return update_donation(request, donation.case_name)
    # return HttpResponseRedirect('/donations_app/<donation.case_name>/')
