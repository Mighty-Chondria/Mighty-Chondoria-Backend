from django.urls import path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views



# app_name="accounts"



urlpatterns=[
    path('admin/', admin.site.urls),
    path('register/',views.register_request,name='register'),
    path('courses/',views.courses,name='courses'),
    path('immunology/',views.immunology,name='immunology'),
    path('hematology/',views.hematology,name='hematology'),
    path('contact/',views.contactus,name='contactus'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('',views.home_page,name='homepage'),


    # path('admin_panel/add_price/',views.add_price,name='addprice'),

    #path('change-language/<str:language_code>/',views.change_language,name='changelanguage'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        

