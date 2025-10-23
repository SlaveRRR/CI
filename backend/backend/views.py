import random
from django.http import JsonResponse
from blog.models import Post

def posts(request):
    
    count = random.randint(2, 10)
    
    posts_query = Post.objects.all()
    
    random_posts = posts_query.order_by('?')[:count]
    
    
    
     # Формируем ответ
    posts_data = []
    for post in random_posts:
        posts_data.append({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': {
                    'id': post.author.id,
                    'name': post.author.name,
                    'email': post.author.email
                },
                'category': {
                    'id': post.category.id if post.category else None,
                    'name': post.category.name if post.category else None
                },
                'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'likes_count': post.likes_count,
                'comments_count': post.comments_count,
                'view_count': post.view_count
            })

        
    return JsonResponse({
        'posts': posts_data,
        'total': len(posts_data),
        'generated_at': '2024-01-01 12:00:00'
    })