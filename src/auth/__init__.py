
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import (
    Allow,
    Authenticated,
)

from .security import get_group


class NewRoot:
    def __init__(self, request):
        self.request = request

    def __acl__(self):
        acl = [
            (Allow, Authenticated, 'view'),
        ]
        return acl


def includeme(config):
    config.set_root_factory(NewRoot)

    authn_secret = config.registry.settings['authn.secret']
    authn_policy = AuthTktAuthenticationPolicy(authn_secret, hashalg="sha512")
    config.set_authentication_policy(authn_policy)

    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
