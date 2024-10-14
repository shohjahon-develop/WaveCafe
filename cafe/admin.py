from django.contrib import admin

from cafe.models import Ice, Hot, Fruit, About,Item,Contact,Comment

# Register your models here.
admin.site.register(Ice)
admin.site.register(Hot)
admin.site.register(Fruit)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Item)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','body','created_time','active']
    list_filter = ['active','created_time']
    search_fields = ['user','body']
    actions = ['disable_comments','activate_comments']

    def disable_comments(self,request,quaryset):
        quaryset.update(active=False)
    def active_comments(self,request,quaryset):
        quaryset.update(active=True)
