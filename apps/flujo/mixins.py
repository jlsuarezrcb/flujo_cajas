from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator


class SecurityMixin(object):

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_anonymous:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(redirect_to=reverse('login'))
        return super().dispatch(request, *args, **kwargs)