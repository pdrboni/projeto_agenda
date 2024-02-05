from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

from contact.models import Contact

# Create your views here.
def index(request):

    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj' : page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,'contact/index.html', context
    )

def contact(request, contact_id):

    single_contact = Contact.objects.filter(pk=contact_id, show=True).first() # não estou utilizando get() pois ele retornaria um erro caso eu busque, na url, um valor que não exista ou um valor duplicado.

    if single_contact is None:
        raise Http404()
    
    # O trecho acima tb funcionaria assim:
    # single_contact = get_object_or_404(
    # Contact.objects.filter(pk=contact_id))
    
    # ou assim:
    # single_contact = get_object_or_404(
    # Contact.objects, pk=contact_id)

    # ou assim:
    # single_contact = get_object_or_404(
    # Contact, pk=contact_id)

    contact_name = f'{single_contact.first_name} - '

    context = {
        'contact' : single_contact,
        'site_title': contact_name,
    }

    return render(
        request,'contact/contact.html', context
    )

def search(request):

    search_value = request.GET.get('q', '').strip() # esse GET vai ser um dicionario, sendo a chave o name do seu form (input em _header.html) e o valor sendo o valor que você procurou em search. o '.get' vai pegar o valor da cahve 'q' do seu dicionario e se não houver valor, ele retorna ''.
    
    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains = search_value) | Q(last_name__icontains = search_value)| Q(phone__icontains = search_value)| Q(email__icontains = search_value)).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'site_title': 'Search - ',
        'search_value': search_value
    }

    return render(
        request,'contact/index.html', context
    )