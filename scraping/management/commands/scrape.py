from django.core.management.base import BaseCommand

from scraping.models import Job
class Command(BaseCommand):
    # define logic of command
    def handle(self, *args, **options):
        try:
            # save in db
            Job.objects.create(
            url="test"            #insert comma if several columns
            )
        except:
            print('error')

        self.stdout.write( 'job complete' )
