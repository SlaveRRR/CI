from django.core.management.base import BaseCommand
from blog.models import Author, Category, Post, Comment
from django.utils import timezone
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Генерирует тестовые данные для блога'

    def handle(self, *args, **options):
        # Очищаем существующие данные
        Comment.objects.all().delete()
        Post.objects.all().delete()
        Category.objects.all().delete()
        Author.objects.all().delete()

        # Создаем авторов
        authors_data = [
            {'name': 'Алексей Петров', 'email': 'alex@example.com', 'bio': 'Senior Python разработчик'},
            {'name': 'Мария Иванова', 'email': 'maria@example.com', 'bio': 'Frontend разработчик'},
            {'name': 'Иван Сидоров', 'email': 'ivan@example.com', 'bio': 'Fullstack разработчик'},
            {'name': 'Екатерина Волкова', 'email': 'ekaterina@example.com', 'bio': 'UI/UX дизайнер'},
            {'name': 'Дмитрий Козлов', 'email': 'dmitry@example.com', 'bio': 'DevOps инженер'},
        ]

        authors = []
        for author_data in authors_data:
            author = Author.objects.create(**author_data)
            authors.append(author)

        # Создаем категории
        categories_data = [
            {'name': 'Django', 'description': 'Статьи о Django фреймворке'},
            {'name': 'React', 'description': 'Статьи о React и фронтенд разработке'},
            {'name': 'Python', 'description': 'Статьи о языке Python'},
            {'name': 'JavaScript', 'description': 'Статьи о JavaScript'},
            {'name': 'Базы данных', 'description': 'Статьи о базах данных и SQL'},
            {'name': 'DevOps', 'description': 'Статьи о DevOps и deployment'},
        ]

        categories = []
        for category_data in categories_data:
            category = Category.objects.create(**category_data)
            categories.append(category)

        # Заголовки и контент для постов
        titles = [
            "Изучение Django: от основ к продвинутым темам",
            "React компоненты - лучшие практики",
            "Python советы и трюки для ежедневного использования",
            "Оптимизация запросов к базе данных",
            "Создание REST API с Django REST Framework",
            "Введение в hooks в React",
            "Асинхронное программирование в Python",
            "MySQL vs PostgreSQL: что выбрать?",
            "Docker для Django разработчиков",
            "Тестирование React приложений с Jest",
        ]

        contents = [
            "В этой статье мы рассмотрим основные концепции Django и как эффективно использовать этот мощный фреймворк для создания веб-приложений.",
            "React предоставляет множество возможностей для создания переиспользуемых компонентов. Узнайте о лучших практиках и паттернах.",
            "Python - невероятно гибкий язык. Вот коллекция советов, которые помогут вам писать более чистый и эффективный код.",
            "Производительность базы данных критически важна для веб-приложений. Узнайте, как оптимизировать ваши запросы и улучшить скорость работы.",
            "REST API стали стандартом для веб-разработки. Узнайте, как создавать надежные API с помощью Django REST Framework.",
            "Hooks изменили способ написания React компонентов. Изучите, как использовать их для упрощения вашего кода.",
            "Асинхронность - ключевая особенность современного Python. Разберитесь с async/await и асинхронными библиотеками.",
            "Выбор базы данных - важное решение. Сравним две популярные реляционные базы данных и их особенности.",
            "Docker упрощает deployment и разработку. Узнайте, как контейнеризировать ваше Django приложение.",
            "Качественное тестирование - залог надежного приложения. Изучите инструменты и подходы для тестирования React.",
        ]

        # Создаем посты
        posts = []
        for i in range(50):  # Создаем 50 постов
            post = Post.objects.create(
                title=f"{random.choice(titles)} #{i+1}",
                content=random.choice(contents),
                author=random.choice(authors),
                category=random.choice(categories),
                created_at=timezone.now() - timedelta(days=random.randint(0, 365)),
                likes_count=random.randint(0, 150),
                comments_count=random.randint(0, 25),
                view_count=random.randint(50, 1000),
                is_published=random.choice([True, True, True, False])  # 75% опубликованы
            )
            posts.append(post)

        # Создаем комментарии
        comment_authors = ['Олег', 'Светлана', 'Андрей', 'Наталья', 'Михаил', 'Анна', 'Павел', 'Юлия']
        comment_texts = [
            "Отличная статья! Очень полезная информация.",
            "Спасибо за подробное объяснение, многое стало понятнее.",
            "Есть вопрос по поводу производительности, можно ли оптимизировать дальше?",
            "Интересный подход, обязательно попробую в своем проекте.",
            "Хотелось бы увидеть больше примеров кода.",
            "Статья помогла решить проблему, над которой бился несколько дней!",
            "Есть небольшое замечание по терминологии, но в целом очень хорошо.",
            "Жду продолжения темы, особенно про advanced техники.",
        ]

        for post in posts:
            # Создаем 0-5 комментариев для каждого поста
            for _ in range(random.randint(0, 5)):
                Comment.objects.create(
                    post=post,
                    author_name=random.choice(comment_authors),
                    content=random.choice(comment_texts),
                    created_at=post.created_at + timedelta(days=random.randint(1, 30)),
                    is_approved=random.choice([True, True, True, False])  # 75% одобрены
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'Успешно создано: {Author.objects.count()} авторов, '
                f'{Category.objects.count()} категорий, '
                f'{Post.objects.count()} постов, '
                f'{Comment.objects.count()} комментариев'
            )
        )