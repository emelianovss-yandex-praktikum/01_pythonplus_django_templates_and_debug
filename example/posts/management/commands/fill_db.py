from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker
from posts.models import Posts, Profile

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        faker = Faker()
        user = get_user_model().objects.create(
            username='',
            email='',
            first_name='',
            last_name=''
        )
        profile = Profile.objects.create()
        count = options['count']
        for i in range(count):
            pass