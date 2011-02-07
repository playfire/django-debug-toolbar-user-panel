from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import auth
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

def content(request):
    try:
        current = []
        for field in User._meta.fields:
            if field.name == 'password':
                continue

            current.append(
                (field.attname, getattr(request.user, field.attname))
            )

        return render_to_response('debug_toolbar_user_panel/content.html', {
            'next': request.GET.get('next'),
            'users': User.objects.order_by('-last_login')[:20],
            'current': current,
        }, context_instance=RequestContext(request))
    except:
        import traceback
        traceback.print_exc()
        raise

@require_POST
def login(request, pk):
    user = get_object_or_404(User, pk=pk)

    # Hacky
    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    auth.login(request, user)

    return HttpResponseRedirect(request.POST.get('next', '/'))
