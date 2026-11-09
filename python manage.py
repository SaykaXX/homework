# Задание 1
from myapp.models import Article, Category

Article.objects.create(title="First article")
Article.objects.create(title="Second article")
Article.objects.create(title="Django guide")

for article in Article.objects.all():
    print(article.title, article.created_at)

# Задание 2
qs = Article.objects.filter(title__contains="a")
for article in qs:
    print(article.title)

try:
    obj = Article.objects.get(pk=1)
    print(obj.title)
except Article.DoesNotExist:
    print("Объект с pk=1 не найден")

try:
    obj_999 = Article.objects.get(pk=999)
    print(obj_999.title)
except Article.DoesNotExist:
    print("Объект с pk=999 не найден")

# Задание 3
cat_tech = Category.objects.create(name="Technology")
cat_news = Category.objects.create(name="News")

art1 = Article.objects.create(title="Python 3.12 release", category=cat_tech)
art2 = Article.objects.create(title="Global weather update", category=cat_news)

for article in Article.objects.filter(category__isnull=False):
    print(f"Статья: {article.title} -> Категория: {article.category.name}")
