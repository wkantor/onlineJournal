from django.contrib import admin
from .models import Entry
from .models import Question
from .models import Plunge
from .models import Quote
from .models import Quote_item
from .models import Topic
from .models import Topic_item
from .models import Topic_item2
from .models import Shadow
from .models import Shadow_item

admin.site.register(Entry)
admin.site.register(Question)
admin.site.register(Plunge)
admin.site.register(Quote)
admin.site.register(Quote_item)
admin.site.register(Topic)
admin.site.register(Topic_item)
admin.site.register(Topic_item2)
admin.site.register(Shadow)
admin.site.register(Shadow_item)

