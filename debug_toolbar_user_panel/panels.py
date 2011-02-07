from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from debug_toolbar.panels import DebugPanel

class UserPanel(DebugPanel):
    """
    Panel that allows you to login as other recently-logged in users.
    """

    name = 'User'
    has_content = True

    def nav_title(self):
        return _('User')

    def url(self):
        return ''

    def title(self):
        return _('User')

    def nav_subtitle(self):
        return self.request.user.username

    def content(self):
        context = self.context.copy()
        context.update({
            'request': self.request,
        })

        return render_to_string('debug_toolbar_user_panel/panel.html', context)

    def process_response(self, request, response):
        self.request = request
