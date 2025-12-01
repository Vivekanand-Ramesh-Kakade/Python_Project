from datetime import date, timedelta
from django.http import JsonResponse
from django.shortcuts import render
from .models import Movie

NEW_DAYS_WINDOW = 30  # define "new" as released within last 30 days

def movies_page(request):
    # Server renders page shell; data loads via AJAX
    context = {
        'new_days_window': NEW_DAYS_WINDOW
    }
    return render(request, 'catalog/movies.html', context)

def new_movies_api(request):
    cutoff = date.today() - timedelta(days=NEW_DAYS_WINDOW)
    qs = (
        Movie.objects
        .select_related('language', 'location')
        .filter(release_date__gte=cutoff)
        .order_by('-release_date', 'title')
    )

    data = [
        {
            'title': m.title,
            'description': m.description,
            'language': m.language.name,
            'location': m.location.name,
            'release_date': m.release_date.strftime('%Y-%m-%d'),
            'rating': float(m.rating) if m.rating is not None else None
        }
        for m in qs
    ]
    return JsonResponse({'results': data, 'count': len(data)})
