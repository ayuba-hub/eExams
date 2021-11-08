from django.urls import path
from student import views
from .views import UserLogin
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('',UserLogin.as_view(),name='index'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('profile/', views.student_dashboard_view,name='student-dashboard'),

    path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
    path('view-result', views.view_result_view,name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
    path('student-marks', views.student_marks_view,name='student-marks'),
]