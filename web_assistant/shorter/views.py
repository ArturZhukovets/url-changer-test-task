from django.shortcuts import render, redirect
from uuid import uuid4
from .forms import UrlForm
from .models import Url


DOMAIN = 'localhost:8000/'  # insert server address here.


def shorter(request):
    list_of_urls = Url.objects.all()
    url_id = str(uuid4())[:6]
    generated_url = DOMAIN + url_id
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid() and not Url.objects.filter(source_url=form.cleaned_data['source_url']):
            new_url = Url(source_url=form.cleaned_data['source_url'], url_id=url_id)
            new_url.save()
            context = {'form': form, 'url_id': url_id, 'result':generated_url, 'list':list_of_urls, 'domain':DOMAIN}
            return render(request, 'shorter/shorter.html', context)

        else:
            error = 'This url is already exist'
            return render(request, 'shorter/shorter.html', {'form': form, 'error':error, 'list':list_of_urls, 'domain':DOMAIN})
    else:
        form = UrlForm()
    return render(request, 'shorter/shorter.html', context={'form': form, 'list':list_of_urls, 'domain':DOMAIN})


def to_source_url(request, url_id):
    """
     If the user clicks on the shortened URL,
     the function matches it with the source and redirects to the source address
    """
    origin_url = Url.objects.get(url_id=url_id)
    return redirect(origin_url.source_url)


def delete_link(request, url_id):
    url_to_delete = Url.objects.get(url_id=url_id)
    url_to_delete.delete()
    return redirect('/shorter')



