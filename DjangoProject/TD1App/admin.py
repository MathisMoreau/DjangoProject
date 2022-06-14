from django.contrib import admin
from .models import Machine
from .models import Infra
from .models import Moi
admin.site.register(Infra)
admin.site.register(Machine)
admin.site.register(Moi)
# Register your models here.
