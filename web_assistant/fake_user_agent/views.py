from django.shortcuts import render
from .models import FakeUserAgent
from django.core.paginator import Paginator
from random import randint


def user_agent(request):
    data = FakeUserAgent.objects.all()
    paginator = Paginator(data, 20)

    page_number = request.GET.get('page', 1)   # get number of the page in url. By default, page_number=1
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    context = {
        'page': page,
        'is_paginated': is_paginated,
        'next': next_url,
        'prev': prev_url
    }
    if request.method == 'POST':
        random_index_ua = randint(1, len(FakeUserAgent.objects.all()))
        random_obj = FakeUserAgent.objects.get(id=random_index_ua)
        context['random_obj'] = random_obj
        return render(request, 'fake_user_agent/user_agent.html', context)

    return render(request, 'fake_user_agent/user_agent.html', context)



