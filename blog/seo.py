from django.utils import timezone


def post_meta(post):
    title = "<title>{{title}}</title>".replace("{{title}}", post.title[:68])
    description = '<meta name="description" content="{{body}}">'.replace("{{body}}", str(post.body[:155]).replace("'",
                                                                                                                  '	&apos;').replace(
        '"', "&quot;"))
    keywords = '<meta name="keywords" content="{{keywords}}">'.replace("{{keywords}}", post.keywords)
    author = '<meta name="author" content="{{author}}">'.replace("{{author}}", post.author.name)
    date = '<meta name="date" content="{{date}}" scheme="YYYY-MM-DD">'.replace("{{date}}",
                                                                               str(post.date.year) + '-' + str(
                                                                                   post.date.month) + '-' + str(
                                                                                   post.date.day))
    charset = '<meta charset="UTF-8">'

    return {'title': title,
            'description': description,
            'keywords': keywords,
            'author': author,
            'date': date,
            'charset': charset,
            }


def index_meta():
    title = "<title>mowhamadrexa's blog</title>"
    description = '<meta name="description" content="The safest place I can shout out my thoughts without being worry about its consequences...">'
    keywords = '<meta name="keywords" content="mowhamadrexa, blog, محمدرضا کاظمی, canada,کانادا">'
    author = '<meta name="author" content="mowhamadrexa">'
    date = '<meta name="date" content="{{date}}" scheme="YYYY-MM-DD">'.replace("{{date}}",
                                                                               str(timezone.now().year) + '-' + str(
                                                                                   timezone.now().month) + '-' + str(
                                                                                   timezone.now().day))
    charset = '<meta charset="UTF-8">'

    return {'title': title,
            'description': description,
            'keywords': keywords,
            'author': author,
            'date': date,
            'charset': charset,
            }
