from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from accounts.views_auth import user_login
from django.conf import settings
from django.conf.urls.static import static
from myschool.views import error_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='user_login'),
    path("accounts/", include("accounts.urls")),
    path("calendar/", include("calendarapp.urls")),
    path("profile/", include("schoolprofile.urls")),
    path("teachers/", include("teachers.urls")),
    path("students/", include("students.urls")),
    path("", RedirectView.as_view(pattern_name="accounts:user_dashboard", permanent=False)),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = lambda request, exception: error_page(request, exception, 400)
handler403 = lambda request, exception: error_page(request, exception, 403)
handler404 = lambda request, exception: error_page(request, exception, 404)
handler500 = lambda request: error_page(request, None, 500)