from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apihouse import views
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
swagger_view = get_swagger_view(title='Yusuf\'s ApiStore')

router.register(r'authors', views.AuthorViewSet)
router.register(r'blogs', views.BlogViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'login', views.LoginView)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('apihouse.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api/swagger/', swagger_view),
    path('api/auth/', include('rest_auth.urls')),

]
