import datetime
from django.db import models


class UserStat():
    user = models.CharField()
    last_access_time = models.DateTimeField(blank=False)

