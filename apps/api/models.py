from __future__ import absolute_import

import logging, base64, M2Crypto, uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

def generate_key():
    return base64.b64encode(M2Crypto.m2.rand_bytes(20) + uuid.uuid1().bytes)

class ApiKey(models.Model):
    """
    API keys are proxies for the userid/password used for API calls.  The advantage
    over regular passwords is that 1) they can be individually disabled, 2) they
    don't need to be memorable.

    I considered storing these encrypted, but couldn't think of a realistic situation 
    where this would improve security, since these keys aren't useful elsewhere.
    """
    user = models.ForeignKey(User, verbose_name=_(u'user'), editable=False, db_index=True)
    name = models.CharField(max_length=80, verbose_name=_(u'name'))
    key  = models.CharField(
        max_length=48, 
        verbose_name=_(u'access key'), 
        editable=False, 
        default=generate_key, 
        db_index=True
    )

    def __unicode__(self):
        return self.name





