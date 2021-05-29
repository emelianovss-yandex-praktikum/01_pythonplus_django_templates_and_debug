from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from posts.models import Post, Profile


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        user = get_user_model().objects.create(
            username=fake.user_name(),
            email=fake.ascii_free_email(),
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        Profile.objects.create(user=user, address=fake.street_address())
        count = options['count']

        for i in range(count):
            Post.objects.create(user=user, title=fake.paragraph(nb_sentences=5))
