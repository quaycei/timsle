from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from circle.models import Tag, Circle, Link, Project, Content, Guideline


class CircleAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')


admin.site.register(Tag)
admin.site.register(Circle, CircleAdmin)
admin.site.register(Link)
admin.site.register(Project)
admin.site.register(Content)
admin.site.register(Guideline)


