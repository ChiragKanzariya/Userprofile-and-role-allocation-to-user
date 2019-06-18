from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from details.models import ProfileModel


class MyPageModelAdmin(ModelAdmin):
    model = ProfileModel
    menu_label = 'Profile Model'  # ditch this to use verbose_name_plural from model
    menu_icon = 'form'  # change as required
    # will put in 3rd place (000 being 1st, 100 2nd, 200 3rd likewise)
    menu_order = 100
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False
    search_fields = ('name',)


modeladmin_register(MyPageModelAdmin)
