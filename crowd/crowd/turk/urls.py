# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # # URL pattern for the Welcome Page
    url(
        # regex=r'^(?P<key>[\w.@+-]+)&(?P<user_type>[\w.@+-]+)/$',
        regex=r'^$',
        view=views.welcome,
        name='welcome'
    ),

    # # URL pattern for the UserRedirectView
    # url(
    #     regex=r'^~redirect/$',
    #     view=views.UserRedirectView.as_view(),
    #     name='redirect'
    # ),

    # # URL pattern for the UserDetailView
    # url(
    #     regex=r'^(?P<username>[\w.@+-]+)/$',
    #     view=views.UserDetailView.as_view(),
    #     name='detail'
    # ),

    # # URL pattern for the UserUpdateView
    # url(
    #     regex=r'^~update/$',
    #     view=views.UserUpdateView.as_view(),
    #     name='update'
    # ),
]