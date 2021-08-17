from django.urls import path
from . import views 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', views.hi),
    path('candidates/',views.candidate_info),
]
