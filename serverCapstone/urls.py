
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from capstoneapi.views import register_user, login_user
from rest_framework import routers
from capstoneapi.views import ApplicantView, AppliedView, EmployerView, Job_PostingView, ResumeView, SkillsView, CompanyView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'applicants', ApplicantView, 'applicant')
router.register(r'applied', AppliedView, 'applied')
router.register(r'employers', EmployerView, 'employer')
router.register(r'jobpostings', Job_PostingView, 'jobposting')
router.register(r'resumes', ResumeView, 'resume')
router.register(r'skills', SkillsView, 'skill')
router.register(r'company', CompanyView, 'companies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls))
]
