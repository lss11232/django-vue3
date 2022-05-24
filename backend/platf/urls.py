from rest_framework.routers import SimpleRouter

from .views import PlatformModelViewSet

from django.urls import path,include

router = SimpleRouter()
router.register("api/Platform", PlatformModelViewSet)

urlpatterns = [
    # path("api/Plaxxtform/", PlatformModelViewSet.as_view(
    #     {"get": "get_Platf"}
    # ))

]
urlpatterns += router.urls

# router.register("api/get_Plat", get_Plat)
# urlpatterns += router.urls

