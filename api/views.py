from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, authentication, permissions
from .serializers import UserSerializer

User = get_user_model()


class DefaultMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class UserViewSet(DefaultMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users."""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD,)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD,)
