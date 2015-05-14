from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from django.views import generic
from django.utils.text import slugify

from info.models import UserProfile
from manager.models import Pack
from manager.mixins import PermissionViewMixin, PermissionEditMixin
from gc import get_objects

# Create your views here.
class ProfileDetailView(generic.DetailView):
    model = User
    template_name = "info/profile.html"
    
    
        
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get('username', None))
