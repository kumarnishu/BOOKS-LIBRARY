from django.urls import path
from app.views import *


app_name="app"
urlpatterns=[
    path("",index,name="index"),
    path("login_page/",login_page,name="login_page"),
    path("login_view/",login_view,name="login_view"),
    path("signup_page/",signup_page,name="signup_page"),
    path('signup_view/',signup_view,name="signup_view"),
    path("logout_view/",logout_view,name="logout_view"),
    path("reset_page/",reset_page,name="reset_page"),
    path("reset_password_view/",reset_password_view,name="reset_password_view"),
    path("book_display/",book_display,name="book_display"),
    path("new_book_page/",new_book_page,name="new_book_page"),
    path("update_page/<slug:slug>",update_page,name="update_page"),
    path("del_page/<slug:slug>/",del_page,name="del_page"),
    path("new_book/",new_book,name="new_book"),
    path("update/<slug:slug>/",update,name="update"),
    path("delete/<slug:slug>/",delete,name="delete"),
    path("issue_page/<slug:slug>/",issue_page,name="issue_page"),
    path("issue/<slug:slug>/",issue,name="issue"),
    path("del_issue/<slug:slug>/",del_issue,name="del_issue"),
    path("del_issue_page/<slug:slug>/",del_issue_page,name="del_issue_page"),
    path("create_data/<num>/",create_data,name="create_data"),
    path("create_data_page/",create_data_page,name="create_data_page"),
    path("update_profile_page/",update_profile_page,name="update_profile_page"),
    path("update_profile/<slug:slug>/",update_profile,name="update_profile"),
    path("staff_page/",staff_page,name="staff_page"),
    path("new_staff_page/",new_staff_page,name="new_staff_page"),
    path("update_staff_page/<slug:slug>/",update_staff_page,name="update_staff_page"),
    path("delete_staff_page/<slug:slug>/",delete_staff_page,name="delete_staff_page"),
    path("new_staff/",new_staff,name="new_staff"),
    path("update_staff/<slug:slug>/",update_staff,name="update_staff"),
    path("delete_staff/<slug:slug>/",delete_staff,name="delete_staff"),


]


