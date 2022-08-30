from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Category
from reviews.models import Title
from reviews.models import Review
from reviews.models import Genre_title
from reviews.models import Comments
from reviews.models import Genre
from users.models import User


class Command(BaseCommand):
    help = 'Loads data from csv file'

    def handle(self, *args, **options):
        for row in DictReader(open('./static/data/category.csv')):
            category = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug'])
            category.save()

        for row in DictReader(open('./static/data/genre.csv')):
            genre = Genre(
                id=row['id'],
                name=row['name'],
                slug=row['slug'])
            genre.save()

        for row in DictReader(open('./static/data/titles.csv')):
            titles = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category']
            )
            titles.save()

        for row in DictReader(open('./static/data/users.csv')):
            users = User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )
            users.save()

        for row in DictReader(open('./static/data/review.csv')):
            review = Review(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author'],
                score=row['score'],
                pub_date=row['pub_date']
            )
            review.save()

        for row in DictReader(open('./static/data/comments.csv')):
            comments = Comments(
                id=row['id'],
                review_id_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date']
            )
            comments.save()

        for row in DictReader(open('./static/data/genre_title.csv')):
            genre_title = Genre_title(
                title_id_id=row['title_id'],
                genre_id_id=row['genre_id']
            )
            genre_title.save()
