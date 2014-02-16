from django.contrib import admin

from app.models import Item, ItemLike, ItemComment

class ItemLikeInline(admin.TabularInline):
    model = ItemLike

class ItemCommentInline(admin.TabularInline):
    model = ItemComment

class ItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'likes_count', 'comments_count', 'date')
    ordering = ('-id',)
    inlines = [ItemLikeInline, ItemCommentInline]

    def likes_count(self, obj):
        return obj.likes.count()

    def comments_count(self, obj):
        return obj.comments.count()

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemLike)
admin.site.register(ItemComment)
