from django.contrib import admin
from .models import JobModel,UserModel,JobPost,FeedModel,CommentModel
# Register your models here.
admin.site.register(JobModel)
admin.site.register(UserModel)
admin.site.register(JobPost)
admin.site.register(FeedModel)
admin.site.register(CommentModel)