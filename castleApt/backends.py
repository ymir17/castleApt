from django.contrib.auth.models import User


class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            print('From backends: email')
            kwargs = {'email': username}
        else:
            print('From backends: username')
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
