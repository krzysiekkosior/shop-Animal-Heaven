from django.contrib.auth.models import User, Permission
from django.core.management import BaseCommand


def create_admin():
    admin = User.objects.create(username='heavenadmin')
    admin.set_password('admin1')
    perms = list(Permission.objects.filter(content_type_id__in=[7, 8, 9, 10, 11]))
    admin.user_permissions.set(perms)
    admin.save()


class Command(BaseCommand):
    help = "Insert data to database"

    def handle(self, *args, **kwargs):
        pass
        create_admin()
        print("""
        Admin created.
        Login: heavenadmin
        Password: admin1
        """)
