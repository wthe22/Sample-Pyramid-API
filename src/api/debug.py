
from pyramid.view import view_config
from pyramid.response import Response


class DebugView:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='api.list_api')
    def list_api(self):
        request = self.request
        routes = {
            'api.list_api': {},
            'auth.login': {'_query': {'username': 'student', 'password': 'student'}},
            'auth.logout': {},
            'user.list_scores': {},
        }
        for route, params in routes.items():
            routes[route] = request.route_url(route, **params)

        content = ''
        for route, url in routes.items():
            content += '<a href="%s">%s</a><br />\n' % (url, route)
        content = '''
            <h1>API Routes</h1>
            <p style="display: block; font-family: monospace;">%s</p>
        ''' % content

        return Response(content)
