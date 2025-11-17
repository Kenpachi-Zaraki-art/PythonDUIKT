from django.http import HttpResponse, HttpResponseRedirect, Http404
from .data import BloggerData

db = BloggerData()

HTML_STYLE = """
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background-color: #f4f7f6;
        color: #333;
        margin: 0;
        padding: 20px;
        line-height: 1.6;
    }
    .container {
        max-width: 900px;
        margin: 20px auto;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #2c3e50;
        margin-bottom: 0.5em;
    }
    h1 {
        font-size: 2.5em;
        border-bottom: 2px solid #ecf0f1;
        padding-bottom: 10px;
    }
    h2 {
        font-size: 2em;
        color: #34495e;
    }
    a {
        color: #3498db;
        text-decoration: none;
        font-weight: 500;
    }
    a:hover {
        color: #2980b9;
        text-decoration: underline;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    th, td {
        padding: 12px 15px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    th {
        background-color: #3498db;
        color: #ffffff;
        text-transform: uppercase;
        font-size: 0.9em;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    tr:hover {
        background-color: #f1f1f1;
    }
    .nav-link {
        font-size: 1.2em;
        margin-right: 15px;
        display: inline-block;
        margin-bottom: 15px;
    }
</style>
"""


def get_base_html(title, content):
    return f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        {HTML_STYLE}
    </head>
    <body>
        <div class="container">
            <h1>{title}</h1>
            {content}
        </div>
    </body>
    </html>
    """


def index(request):
    news_list = db.get_news()

    content = "<a href='/profiles/' class='nav-link'>Переглянути всіх блогерів</a>"

    content += "<h2>Актуальні новини</h2>"
    content += "<table>"
    content += "<tr><th>Дата</th><th>Заголовок</th></tr>"

    for item in news_list:
        content += f"<tr><td>{item['date']}</td><td>{item['title']}</td></tr>"

    content += "</table>"

    # Оновлено:
    # Тепер заголовок H1 буде "Головна сторінка",
    # а H2 залишиться "Актуальні новини".
    return HttpResponse(get_base_html("Головна сторінка", content))


def profiles_list(request):
    all_bloggers = db.get_all_bloggers()

    content = "<a href='/' class='nav-link'>На головну (Новини)</a>"

    content += "<table>"
    content += "<tr><th>Ім'я</th><th>Категорія</th><th>Опис</th></tr>"

    for slug, data in all_bloggers.items():
        content += f"<tr>"
        content += f"<td><a href='/profile/{slug}/'>{data['name']}</a></td>"
        content += f"<td>{data['category']}</td>"
        content += f"<td>{data['description']}</td>"
        content += f"</tr>"

    content += "</table>"

    return HttpResponse(get_base_html("Профілі Блогерів", content))


def profile_detail(request, blogger_slug):
    blogger = db.get_blogger_by_slug(blogger_slug)

    if not blogger:
        raise Http404(f"Блогера зі slug '{blogger_slug}' не знайдено")

    content = "<a href='/profiles/' class='nav-link'>Назад до списку</a>"

    content += "<table>"
    content += f"<tr><td>Ім'я</td><td>{blogger['name']}</td></tr>"
    content += f"<tr><td>Категорія</td><td>{blogger['category']}</td></tr>"
    content += f"<tr><td>Опис</td><td>{blogger['description']}</td></tr>"
    content += f"<tr><td>Останнє відео</td><td>{blogger['last_video']}</td></tr>"

    links = ""
    for network, url in blogger['social_links'].items():
        links += f"<a href='{url}' target='_blank' style='margin-right: 10px;'>{network.capitalize()}</a> "

    content += f"<tr><td>Соц. мережі</td><td>{links}</td></tr>"
    content += "</table>"

    return HttpResponse(get_base_html(f"Профіль: {blogger['name']}", content))


def news_page_redirect(request):
    return HttpResponseRedirect("/")