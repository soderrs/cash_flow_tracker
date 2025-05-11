from django.contrib import admin
from django.urls import path

import core.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("get-categories/", core.views.get_categories, name="get_categories"),
    path(
        "get-subcategories/", core.views.get_subcategories, name="get_subcategories"
    ),
]
