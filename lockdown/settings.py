from django.conf import settings

URL_EXCEPTIONS = getattr(settings, 'LOCKDOWN_URL_EXCEPTIONS', ())
PASSWORDS = getattr(settings, 'LOCKDOWN_PASSWORDS', ())
FORM = getattr(settings, 'LOCKDOWN_FORM', 'lockdown.forms.LockdownForm')
SESSION_KEY = getattr(settings, 'LOCKDOWN_SESSION_KEY', 'lockdown-allow')
LOGOUT_KEY = getattr(settings, 'LOCKDOWN_LOGOUT_KEY', 'preview-logout')
UNTIL_DATE = getattr(settings, 'LOCKDOWN_UNTIL', None)
AFTER_DATE = getattr(settings, 'LOCKDOWN_AFTER', None)
TEMP_UNLOCK_PASS = getattr(settings, 'LOCKDOWN_TEMP_UNLOCK_PASS', None)
TEMP_UNLOCK_MINUTES = getattr(settings, 'LOCKDOWN_TEMP_UNLOCK_MINUTES', None)

if not isinstance(PASSWORDS, (tuple, list)):
    PASSWORDS = PASSWORDS and (PASSWORDS,) or ()
