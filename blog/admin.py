from django.contrib import admin
from .models import Post
# superuser ist: admin / pass1234

admin.site.register(Post)