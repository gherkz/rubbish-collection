"""
Custom authentication providers.

"""
from rest_framework.authentication import TokenAuthentication


class BearerTokenAuthentication(TokenAuthentication):
    """
    Custom version of DRF's standard TokenAuthentication which uses the keyword "Bearer" so that
    the required header becomes "Authorization: Bearer [...]". This is more in line with modern
    practice.

    """

    keyword = "Bearer"
