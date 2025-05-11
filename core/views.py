from django.http import JsonResponse

import core.models


def get_categories(request):
    type_id = request.GET.get("type")
    categories = core.models.Category.objects.filter(type=type_id).values("id", "name")

    return JsonResponse({"categories": list(categories)})


def get_subcategories(request):
    category_id = request.GET.get("category")
    subcategories = core.models.Subcategory.objects.filter(category=category_id).values(
        "id", "name"
    )

    return JsonResponse({"subcategories": list(subcategories)})
