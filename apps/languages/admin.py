from django.contrib import admin
from apps.languages.models import Language, LanguageSkill, Level

admin.site.register(Language)
admin.site.register(LanguageSkill)
admin.site.register(Level)
