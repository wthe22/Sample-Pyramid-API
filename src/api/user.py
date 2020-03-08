
from pyramid.view import (
    view_defaults,
    view_config,
)

from src.api.models import (
    Course,
    Score,
)


@view_defaults(renderer='json')
class UserView:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='user.list_scores', permission='view')
    def list_scores(self):
        request = self.request
        user_id = request.authenticated_userid

        scores = list(
            Score.select().join(Course).where(Score.user == user_id)
        )
        score_list = {}
        for score in scores:
            score_list[score.course.name] = score.value

        return score_list
