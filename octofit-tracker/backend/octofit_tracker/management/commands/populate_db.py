from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        
        self.stdout.write('Clearing existing data...')
        # Clear all data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write('Creating superhero users...')
        # Create Users - Marvel Team
        ironman = User.objects.create_user(
            username='ironman',
            email='ironman@marvel.com',
            password='password123',
            first_name='Tony',
            last_name='Stark'
        )
        ironman.team = marvel
        ironman.save()

        captain = User.objects.create_user(
            username='captainamerica',
            email='captain@marvel.com',
            password='password123',
            first_name='Steve',
            last_name='Rogers'
        )
        captain.team = marvel
        captain.save()

        thor = User.objects.create_user(
            username='thor',
            email='thor@marvel.com',
            password='password123',
            first_name='Thor',
            last_name='Odinson'
        )
        thor.team = marvel
        thor.save()

        hulk = User.objects.create_user(
            username='hulk',
            email='hulk@marvel.com',
            password='password123',
            first_name='Bruce',
            last_name='Banner'
        )
        hulk.team = marvel
        hulk.save()

        # Create Users - DC Team
        batman = User.objects.create_user(
            username='batman',
            email='batman@dc.com',
            password='password123',
            first_name='Bruce',
            last_name='Wayne'
        )
        batman.team = dc
        batman.save()

        superman = User.objects.create_user(
            username='superman',
            email='superman@dc.com',
            password='password123',
            first_name='Clark',
            last_name='Kent'
        )
        superman.team = dc
        superman.save()

        wonderwoman = User.objects.create_user(
            username='wonderwoman',
            email='wonderwoman@dc.com',
            password='password123',
            first_name='Diana',
            last_name='Prince'
        )
        wonderwoman.team = dc
        wonderwoman.save()

        flash = User.objects.create_user(
            username='flash',
            email='flash@dc.com',
            password='password123',
            first_name='Barry',
            last_name='Allen'
        )
        flash.team = dc
        flash.save()

        self.stdout.write('Creating activities...')
        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        Activity.objects.create(user=ironman, type='weightlifting', duration=45, calories=250)
        Activity.objects.create(user=captain, type='run', duration=60, calories=600)
        Activity.objects.create(user=captain, type='cycle', duration=40, calories=400)
        Activity.objects.create(user=batman, type='cycle', duration=45, calories=450)
        Activity.objects.create(user=batman, type='martial arts', duration=90, calories=700)
        Activity.objects.create(user=superman, type='run', duration=20, calories=800)
        Activity.objects.create(user=thor, type='weightlifting', duration=60, calories=500)
        Activity.objects.create(user=hulk, type='weightlifting', duration=90, calories=900)
        Activity.objects.create(user=wonderwoman, type='martial arts', duration=75, calories=650)
        Activity.objects.create(user=flash, type='run', duration=15, calories=900)

        self.stdout.write('Creating workouts...')
        # Create Workouts
        Workout.objects.create(
            name='Superhero Pushups',
            description='Do 50 pushups with perfect form',
            difficulty='Easy'
        )
        Workout.objects.create(
            name='5K Hero Run',
            description='Run 5 kilometers at a steady pace',
            difficulty='Medium'
        )
        Workout.objects.create(
            name='Power Lifting Session',
            description='Complete a full weightlifting routine',
            difficulty='Hard'
        )
        Workout.objects.create(
            name='Martial Arts Training',
            description='Practice combat techniques for 1 hour',
            difficulty='Hard'
        )
        Workout.objects.create(
            name='Speed Training',
            description='High-intensity interval sprints',
            difficulty='Medium'
        )

        self.stdout.write('Creating leaderboard entries...')
        # Create Leaderboard entries
        Leaderboard.objects.create(user=ironman, score=950)
        Leaderboard.objects.create(user=captain, score=1000)
        Leaderboard.objects.create(user=batman, score=980)
        Leaderboard.objects.create(user=superman, score=820)
        Leaderboard.objects.create(user=thor, score=560)
        Leaderboard.objects.create(user=hulk, score=900)
        Leaderboard.objects.create(user=wonderwoman, score=725)
        Leaderboard.objects.create(user=flash, score=915)

        self.stdout.write(self.style.SUCCESS('✓ Database successfully populated with superhero test data!'))
        self.stdout.write(self.style.SUCCESS(f'  - Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  - Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  - Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  - Workouts: {Workout.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  - Leaderboard entries: {Leaderboard.objects.count()}'))
