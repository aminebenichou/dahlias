
from django.contrib import admin
from django.urls import path, include
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('logout/', logoutUser),
    path('signup/', signupTemp),
    path('createUserPost/', UserRegisterPost, name='create user'),
    path('login/', login, name='login'),
    path('loginPost/', loginPost),
    path('notes/', include('notes.urls'))

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
