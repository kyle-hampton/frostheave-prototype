from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from frostheavetest import views

#serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

#Viewset defines view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#routers provide an easy way of automatically determining the Url conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# wire up our api using automatic URl routing .
# Additionally, we include login URLs for the browsable api
urlpatterns = [
    path('frostheavetest/', include('frostheavetest.urls')),
    path('admin/', admin.site.urls),
    path('data/', views.player, name='player'), #player router
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
