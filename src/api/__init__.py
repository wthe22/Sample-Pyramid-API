

def includeme(config):
    config.add_route('api.list_api', '/')

    config.add_route('auth.login', '/login')
    config.add_route('auth.logout', '/logout')

    config.add_route('user.list_scores', '/user/scores')
