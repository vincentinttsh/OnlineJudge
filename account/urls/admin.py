from django.conf.urls import url

from ..views.admin import UserAdminAPI, GenerateUserAPI, SessionManagementAPI

urlpatterns = [
    url(r"^user/?$", UserAdminAPI.as_view(), name="user_admin_api"),
    url(r"^generate_user/?$", GenerateUserAPI.as_view(), name="generate_user_api"),
    url(r"^sessions/?$", SessionManagementAPI.as_view(), name="admin_session_management_api")
]
