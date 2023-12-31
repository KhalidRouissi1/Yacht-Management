
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("yachtStore.urls")),
    path('members/', include("django.contrib.auth.urls")),
    path('members/', include("members.urls")),
    path('members/', include("members.urls")),
    path('api/', include("api.urls")),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns +=staticfiles_urlpatterns()
