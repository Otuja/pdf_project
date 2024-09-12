from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from .models import Pdf

from .forms import SignupForm, NewItemForm, EditItemForm, SubscriberForm

from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    pdfs = Pdf.objects.all()
    query = request.GET.get('query', '')

    # Start by filtering the queryset based on the search query
    if query:
        pdfs = Pdf.objects.filter(
            Q(coursename__icontains=query) | 
            Q(coursecode__icontains=query) | 
            Q(description__icontains=query) | 
            Q(institution__icontains=query)
        )
    else:
        pdfs = Pdf.objects.all()  # No search query, return all

    # getting all object for index page

    # for pagination
    paginator = Paginator(pdfs, 4)
    page_number = request.GET.get('page')

    try:
        # Get the items for the current page
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {
        'pdfs': pdfs,
        'query': query,
        'page_obj': page_obj
    })

def detail(request, id):
    pdf = get_object_or_404(Pdf, pk=id)

    return render(request, 'detail.html', {
        'pdf': pdf
    })

@login_required
def pdf_list(request):
    pdfs = Pdf.objects.filter(owner=request.user.id)#1:30
    context = {
        'pdfs' : pdfs
    }
    return render(request, 'pdf_list.html', context)


# authentication

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:

        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })

# login do not need view

# add
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            pdf = form.save(commit=False)
            pdf.owner = request.user
            form.save()

            return redirect('/files/', id=pdf.id)

    else:
        form = NewItemForm()

    return render(request, 'form.html', {
        'form': form,
        'title': 'New Item',
    })


@login_required
def delete(request, id):
    pdf = get_object_or_404(Pdf, pk=id, owner=request.user)
    pdf.delete()

    return redirect('/files/')


@login_required
def edit(request, id):
    pdf = get_object_or_404(Pdf, pk=id, owner=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=pdf)

        if form.is_valid():
            pdf.save()

            return redirect('detail', id=pdf.id)
    else:
        form = EditItemForm(instance=pdf)

    return render(request, 'form.html', {
        'form': form
    })


def custom_logout(request):
    logout(request)

    return redirect('index')


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
        else:
            messages.error(request, 'There was an issue with your subscription.')
    return redirect(request.META.get('HTTP_REFERER', 'index'))