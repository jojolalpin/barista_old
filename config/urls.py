from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from organizations.backends import invitation_backend

from allauth.account.views import LoginView, LogoutView
from django.contrib.auth.views import login, logout

from barista.chat.views import index
urlpatterns = [

    url(r'^$', index),
    #url(r'^accounts/login/$', login),
    #url(r'^accounts/logout/$', logout),

    url(r'home/^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('barista.users.urls', namespace='users')),

    #url(r'^accounts/login/$', LoginView.as_view(), name='login'),  # Reverse needed
    #url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),  # Reverse needed

    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^accounts/', include('organizations.urls')),
    url(r'^invitations/', include(invitation_backend().get_urls())),

    #url(r'^chat/', index), #include('barista.front.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
