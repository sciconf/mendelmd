from django.urls import include, path

from django.contrib import admin

from django.views.generic import TemplateView

admin.autodiscover()

from django.conf import settings as settings2

from django.conf.urls.static import static

from . import views

import files.views
import settings.views

urlpatterns = [
    # Examples:
    # path("", "rockbio.views.home", name="home"),
    # path("blog/", include("blog.urls")),
    path("", views.index, name="index"),

    path("docs/", views.docs, name="docs"),


    path("admin/", admin.site.urls),

    path("upload/", files.views.upload, name="upload"),
    path("subscribe/", settings.views.mysubscription, name="settings-mysubscription"),
    
    

    path("accounts/", include("allauth.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("individuals/", include("individuals.urls")),
    path("diseases/", include("diseases.urls")),
    path("genes/", include("genes.urls")),
    path("variants/", include("variants.urls")),
    path("cases/", include("cases.urls")),
    path("filter_analysis/", include("filter_analysis.urls")),
    path("pathway_analysis/", include("pathway_analysis.urls")),
    path("statistics/", include("stats.urls")),
    path("databases/", include("databases.urls")),
    path("projects/", include("projects.urls")),
    path("select2/", include("django_select2.urls")),
    path("files/", include("files.urls")),
    path("samples/", include("samples.urls")),
    path("settings/", include("settings.urls")),    
    path("tasks/", include("tasks.urls")),
    path("workers/", include("workers.urls")),
    path("analyses/", include("analyses.urls")),
    # path("apps/", include("mapps.urls")),
    path("keys/", include("keys.urls")),
    path("servers/", include("servers.urls")),
    path("apps/", include("apps.urls")),
    #path("subscription/", views.pricing_page, name="pricing_page"),
    


] + static(settings2.STATIC_URL, document_root=settings2.STATIC_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns("",
#         path("__debug__/", include(debug_toolbar.urls)),
#     )
