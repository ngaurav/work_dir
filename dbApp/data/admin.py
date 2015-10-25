from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Client, RegularUser, Page, ProUser, Disease, Event, Record, Review

# Define an inline admin descriptor for Employee model
class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ClientInline, )

class CityAdmin(admin.ModelAdmin):
    pass

class RegularUserAdmin(admin.ModelAdmin):
    pass
#    search_fields = ('category', )
#    list_display = ('category', 'domain',)
#    list_filter = ('domain',)

class PageAdmin(admin.ModelAdmin):
    pass

class ProUserAdmin(admin.ModelAdmin):
    pass

class DiseaseAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    pass

class RecordAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

# Re-register UserAdmin
admin.site.register(City, CityAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(RegularUser, RegularUserAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(ProUser, ProUserAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Review, ReviewAdmin)
