from django.contrib import admin
from .models import Ratings

# Register your models here.

class RatingsAdmin(admin.ModelAdmin):
      fieldsets = [
        ("Personal Details", {'fields': ["name", "username","country","city","organization"]}),
        ("Codeforces Info", {"fields": ["rank_codeforces","rating_codeforces"]})
    ]

admin.site.register(Ratings,RatingsAdmin)
