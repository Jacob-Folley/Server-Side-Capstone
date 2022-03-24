
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from capstoneapi.views import register_user, login_user
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from capstoneapi.views import ApplicantView, AppliedView, Job_PostingView, ResumeView, SkillsView, CompanyView, AcceptedView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'applicants', ApplicantView, 'applicant')
router.register(r'applied', AppliedView, 'applied')
router.register(r'jobpostings', Job_PostingView, 'jobposting')
router.register(r'resumes', ResumeView, 'resume')
router.register(r'skills', SkillsView, 'skill')
router.register(r'company', CompanyView, 'companies')
router.register(r'accepted', AcceptedView, 'accept')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

