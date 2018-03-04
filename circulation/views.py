from urllib.parse import urlencode
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from circulation.models import (RentalClient, ClientHasBoardGame)
from circulation.forms import (RentalClientForm, ClientHasBoardGameForm)
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)
from django.conf import settings


############################################
# Client Views
############################################
class RentalClientListView(ListView):
    model = RentalClient
    paginate_by = settings.CLIENTS_PAGINATION
    paginate_orphans = settings.CLIENTS_PAGINATION_ORPHANS

    def get_queryset(self):
        if self.request.method == 'GET':
            self.filter_criteria = self.request.GET.get("filter")
            if self.filter_criteria and len(self.filter_criteria) >= 2:
                search_type = self.request.GET.get("search")
                if search_type == "identificationCode":
                    return RentalClient.objects.filter(identificationCode__startswith=self.filter_criteria).order_by(
                        "identificationCode")
                elif search_type == "initials":
                    return RentalClient.objects.filter(initials__icontains=self.filter_criteria).order_by("initials")

        return RentalClient.objects.none()


class RentalClientDetailsView(DetailView):
    model = RentalClient


class RentalClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'circulation.add_rentalclient'
    form_class = RentalClientForm
    model = RentalClient


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'circulation.change_rentalclient'
    raise_exception = True

    form_class = RentalClientForm
    model = RentalClient


@login_required
@permission_required('circulation.add_rentalclient', raise_exception=True)
def return_home(request):
    if request.method == 'POST':
        form = RentalClientForm(request.POST)
        if form.is_valid():
            boardgame = form.save(commit=False)
            boardgame.save()
    return redirect('welcome')


def redirect_query(url, params=None):
    response = redirect(url)
    if params:
        query_string = urlencode(params)
        response['Location'] += '?' + query_string
    return response


@login_required
@permission_required('circulation.add_rentalclient', raise_exception=True)
def rentalClientList_return(request):
    if request.method == 'POST':
        form = RentalClientForm(request.POST)
        if form.is_valid():
            rentalClient = form.save(commit=False)
            rentalClient.save()
            return redirect_query('circulation_entries',
                                  {'filter': rentalClient.identificationCode, 'search': 'identificationCode'})
        else:
            return render(request, 'circulation/rentalclient_form.html', {'form': form})
    return redirect('circulation_entries')


class ClientHasBoardGameList(ListView):
    model = ClientHasBoardGame


class ClientHasBoardGameCreateView(CreateView):
    model = ClientHasBoardGame
    form_class = ClientHasBoardGameForm
