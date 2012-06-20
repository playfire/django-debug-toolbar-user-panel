from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.conf import settings
from django.contrib import auth
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import UserForm
from .decorators import debug_required

@debug_required
def content(request):
    current = []

    if request.user.is_authenticated():
        for field in User._meta.fields:
            if field.name == 'password':
                continue
            current.append(
                (field.attname, getattr(request.user, field.attname))
            )

    return render_to_response('debug_toolbar_user_panel/content.html', {
        'form': UserForm(),
        'next': request.GET.get('next'),
        'users': User.objects.order_by('-last_login')[:10],
        'current': current,
    }, context_instance=RequestContext(request))

@csrf_exempt
@require_POST
@debug_required
def login_form(request):
    form = UserForm(request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest()

    return login(request, **form.get_lookup())

@csrf_exempt
@require_POST
@debug_required
def login(request, **kwargs):
    user = get_object_or_404(User, **kwargs)

    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    auth.login(request, user)

    return HttpResponseRedirect(request.POST.get('next', '/'))
