"""learning_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from learning_management_app import views, HodViews, TeacherViews, StudentViews
from learning_management_system import settings

urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage, name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home', HodViews.admin_home,name="admin_home"),
    path('add_teacher',HodViews.add_teacher,name="add_teacher"),
    path('add_teacher_save',HodViews.add_teacher_save,name="add_teacher_save"),
    path('add_course',HodViews.add_course,name="add_course"),
    path('add_course_save',HodViews.add_course_save,name="add_course_save"),
    path('add_student',HodViews.add_student,name="add_student"),
    path('add_student_save',HodViews.add_student_save,name="add_student_save"),
    path('add_subject',HodViews.add_subject,name="add_subject"),
    path('add_subject_save',HodViews.add_subject_save,name="add_subject_save"),
    path('manage_teacher',HodViews.manage_teacher,name="manage_teacher"),
    path('manage_student',HodViews.manage_student,name="manage_student"),
    path('manage_course',HodViews.manage_course,name="manage_course"),
    path('manage_subject',HodViews.manage_subject,name="manage_subject"),
    path('edit_teacher/<str:teacher_id>', HodViews.edit_teacher,name="edit_teacher"),
    path('edit_teacher_save', HodViews.edit_teacher_save,name="edit_teacher_save"),
    path('edit_student/<str:student_id>', HodViews.edit_student,name="edit_student"),
    path('edit_student_save', HodViews.edit_student_save,name="edit_student_save"),
    path('edit_subject/<str:subject_id>', HodViews.edit_subject,name="edit_subject"),
    path('edit_subject_save', HodViews.edit_subject_save,name="edit_subject_save"),
    path('edit_course/<str:course_id>', HodViews.edit_course,name="edit_course"),
    path('edit_course_save', HodViews.edit_course_save,name="edit_course_save"),

    #     Staff URL Path
    path('teacher_home', TeacherViews.teacher_home, name="teacher_home"),
    path('student_home', StudentViews.student_home, name="student_home"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
