from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

# handler404 = "BeerProject.views.View404()"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("PunkApiDB.urls")),
    path('beerproject/', include("BeerProject.urls")),
    path('calculator/', include("Calculator.urls")),
    path('accounts/', include("User.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)