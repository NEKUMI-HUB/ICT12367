from django.contrib import admin
from myapp.models import Person

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'date')
    search_fields = ('name',)
    list_filter = ('date',)
