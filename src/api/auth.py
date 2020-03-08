
from pyramid.view import (
    view_defaults,
    view_config,
)
from pyramid.httpexceptions import (
    HTTPBadRequest,
    HTTPUnauthorized,
)
from pyramid.security import (
    remember,
    forget,
)

from src.auth.security import check_credentials


@view_defaults(renderer='json')
class AuthViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='auth.login')
    def login(self):
        request = self.request
        args = request.params
        try:
            username = args['username']
            password = args['password']
        except KeyError:
            return HTTPBadRequest()

        user_id = check_credentials(username, password)
        if not user_id:
            return HTTPUnauthorized()

        request.response.headers = remember(request, user_id)
        return {'status': 'OK'}

    @view_config(route_name='auth.logout')
    def logout(self):
        request = self.request
        request.response.headers = forget(request)
        return {'status': 'OK'}
