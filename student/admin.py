from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post)
from .models import User
admin.site.register(User)
from .models import Event
admin.site.register(Event)
from .models import EvenClub
admin.site.register(EvenClub)
from .models import EvenSocial
admin.site.register(EvenSocial)
from .models import Reaction
admin.site.register(Reaction)
from .models import Stage
admin.site.register(Stage)
from .models import Recommandation
admin.site.register(Recommandation)
from .models import Logement
admin.site.register(Logement)
from .models import Transport
admin.site.register(Transport)


