from django.contrib import admin
from .models import Itinerary, Day, Hotel, Activity, Transfer

# Register your models here.
admin.site.register(Itinerary)
admin.site.register(Day)
admin.site.register(Hotel)
admin.site.register(Activity)
admin.site.register(Transfer)  