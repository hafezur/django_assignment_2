from django.contrib import admin

from first_app.models import TodoTaskModel
# Register your models here.
class TodoTaskModelAdmin(admin.ModelAdmin):
    list_display=('id','title','description','status')

admin.site.register(TodoTaskModel,TodoTaskModelAdmin)
