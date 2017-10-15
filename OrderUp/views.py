from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from django.contrib.auth import logout

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Action for the default route
from django.http import HttpResponse, Http404, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie


# from bubbles.models import Feedback, GameStats, UserStats

# from bubbles.forms import RegistrationForm
# Django transaction system so we can use @transaction.atomic
from django.db import transaction

from datetime import datetime
from django.core import serializers

import json
import sys

def main(request):
    context={}  

    return render(request,'main.html',context)