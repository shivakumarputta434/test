from django.urls import path
from  .import views
from testapp.views import home2
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('home1',views.home1,name='home1'),
    path('test',views.test,name='test'),
    path('jointable',views.jointable,name='jointable'),
    path('iftest',views.iftest,name="iftest"),

    path('home2',home2.as_view()),
    path('testapi/<int:id>',views.testapi,name='testapi'),
    path('testapiupdate/<int:id>',views.testapiupdate,name='testapiupdate'),
    path('testapical/id=<int:id>&id2=<int:id2>&id3=<int:id3>',views.testapical,name='testapical'),

    path('testapi/',views.testapi),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('post/', views.post, name='post'),
    path('updatepost/<int:id>', views.updatepost, name='updatepost'),
    path('deletepost/<int:id>', views.deletepost, name='deletepost'),


    path('sampleapiall',views.sampleapiall,name='sampleapiall'),
    path('sampleapi/<int:id>',views.sampleapi,name='sampleapi'),
    path('samplepost/name=<str:name>&password=<int:password>&marks=<int:marks>',views.samplepost,name='samplepost'),
    path('samplepostdelete/<int:id>',views.samplepostdelete,name='samplepostdelete'),
    path('samplepostupdate/id=<int:id>&name=<str:name>&password=<int:password>&marks=<int:marks>',views.samplepostupdate,name='samplepostupdate'),


    path('hotelimage',views.hotelimage,name='hotelimage'),
    path('hotelapiall',views.hotelapiall,name='hotelapiall'),





    path('display-movies-api/', views.MovieApi.as_view(), name='displaymoviesapi'),
    path('display-movies-api/<int:pk>/', views.MovieApi.as_view(), name='update'),

    path('display-student/',views.StudentApi.as_view(),name='StudentApi'),
    path('display-student/<int:pk>',views.StudentApi.as_view(),name='update'),


    path('StudentForm/', views.StudentForm, name='StudentForm'),
    path('getcookie/', views.getcookie, name='getcookie'),


    path('CreateUser/', views.CreateUser, name='CreateUser'),

]
