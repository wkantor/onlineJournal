from django.contrib import admin
from .models import Entry
from .models import Question
from .models import Quote
from .models import Rumi
from .models import Mooji
from .models import Topic
from .models import Topic_item

admin.site.register(Entry)
admin.site.register(Question)
admin.site.register(Quote)
admin.site.register(Rumi)
admin.site.register(Mooji)
admin.site.register(Topic)
admin.site.register(Topic_item)

