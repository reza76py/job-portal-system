from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import JobView, ApplyJobView

urlpatterns = [
    path('jobs/', JobView.as_view(), name='job-list'),
    path('jobs/apply/<int:job_id>/', ApplyJobView.as_view(), name='apply-job'),

    # ✅ JWT Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
