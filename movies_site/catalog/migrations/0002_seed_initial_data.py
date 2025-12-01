from django.db import migrations

def seed_data(apps, schema_editor):
    Language = apps.get_model('catalog', 'Language')
    Location = apps.get_model('catalog', 'Location')
    Movie = apps.get_model('catalog', 'Movie')

    langs = ['English', 'Hindi', 'Kannada', 'Tamil', 'Telugu', 'Malayalam']
    locs = ['Bengaluru', 'Mumbai', 'Chennai', 'Hyderabad', 'Kochi', 'Delhi']

    lang_objs = {name: Language.objects.get_or_create(name=name)[0] for name in langs}
    loc_objs = {name: Location.objects.get_or_create(name=name)[0] for name in locs}

    from datetime import date, timedelta
    today = date.today()

    sample_movies = [
        # Recent (new)
        ('Echoes of Time', 'English', 'Bengaluru', today - timedelta(days=3), 8.2, 'Sci-fi drama.'),
        ('Rajadhani Rumble', 'Kannada', 'Bengaluru', today - timedelta(days=5), 7.6, 'Action-comedy.'),
        ('Mumbai Nights', 'Hindi', 'Mumbai', today - timedelta(days=10), 8.0, 'Romance-drama.'),
        ('Marina Breeze', 'Tamil', 'Chennai', today - timedelta(days=14), 7.9, 'Family drama.'),
        ('Charminar Tales', 'Telugu', 'Hyderabad', today - timedelta(days=18), 7.4, 'Historical fiction.'),
        ('Backwaters', 'Malayalam', 'Kochi', today - timedelta(days=22), 8.5, 'Mystery thriller.'),
        # Older (not new)
        ('Old Shadows', 'English', 'Delhi', today - timedelta(days=65), 6.9, 'Noir mystery.'),
    ]

    for title, lang, loc, rdate, rating, desc in sample_movies:
        Movie.objects.get_or_create(
            title=title,
            language=lang_objs[lang],
            location=loc_objs[loc],
            release_date=rdate,
            defaults={'rating': rating, 'description': desc},
        )

def unseed_data(apps, schema_editor):
    # Optional: leave empty or implement delete logic
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
