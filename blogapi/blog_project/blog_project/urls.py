"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path # new
from rest_framework.schemas import get_schema_view # new
from rest_framework_swagger.views import get_swagger_view # new
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# API_TITLE = 'Blog API'
# API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
# schema_view = get_swagger_view(title=API_TITLE) # new
API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version='v1',
        description=API_DESCRIPTION,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@blogapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),  # Your app URLs
    path('api-auth/', include('rest_framework.urls')),  # REST framework login/logout views
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),  # Dj-Rest-Auth endpoints
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration endpoint
    # path('schema/', schema_view), # new
    # path('swagger-docs/', schema_view), # new
    path('swagger-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),

]
