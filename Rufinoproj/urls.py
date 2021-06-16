from django.contrib import admin
from django.conf.urls import include, url
from TitikPoetryApp import views as list_views
from TitikPoetryApp import urls as list_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url('admin/', admin.site.urls),
	url(r'^TitikPoetryApp/', include(list_urls)),
	url(r'^$', list_views.Page, name='page'),
	url(r'^MainPage/$', list_views.MainPage, name='MainPage'),
	url(r'^TitikVideo/$', list_views.TitikVideo, name='TitikVideo'),
	url(r'^TitikPoetry/$', list_views.TitikPoetry, name='TitikPoetry'),
	url(r'^TitikSigya/$', list_views.TitikSigya, name='TitikSigya'),
	url(r'^TitikEnterprise/$', list_views.TitikEnterprise, name='TitikEnterprise'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

