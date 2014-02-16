from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponse
from django.utils import simplejson

from rest_framework import viewsets, routers

from app.models import Item, ItemLike, ItemComment, Profile
from api.serializers import UserSerializer, ItemSerializer

def me(request):
    data = {
        'id': request.user.id, 
        'username': request.user.username,
        'profile': {
            'nickname': request.user.profile.nickname,
            'get_mugshot_url': request.user.profile.get_mugshot_url(),
        },
    }
    return HttpResponse(simplejson.dumps(data))


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.exclude(pk=-1)


class ProfileViewSet(viewsets.ModelViewSet):
    model = Profile


class GroupViewSet(viewsets.ModelViewSet):
    model = Group


class PermissionViewSet(viewsets.ModelViewSet):
    model = Permission


class ItemViewSet(viewsets.ModelViewSet):
    model = Item
    serializer_class = ItemSerializer
    filter_fields = ('date', 'user')

    def create(self, request, *args, **kwargs):
        request.DATA['user'] = request.user.id
        return super(viewsets.ModelViewSet, self).create(request, *args, **kwargs)


class ItemLikeViewSet(viewsets.ModelViewSet):
    model = ItemLike

class ItemCommentViewSet(viewsets.ModelViewSet):
    model = ItemComment

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'items', ItemViewSet)
router.register(r'item_likes', ItemLikeViewSet)
router.register(r'item_comments', ItemCommentViewSet)
router.register(r'profiles', ProfileViewSet)
