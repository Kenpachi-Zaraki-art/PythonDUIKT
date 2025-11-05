from django.http import HttpResponse


def main_page_view(request):
    # HTML-код вашої таблиці
    html_content = """
    <html>
    <head>
        <title>Про мене</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { border-collapse: collapse; width: 50%; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Моя персональна сторінка</h1>
        <p>Інформація про мене (згідно з Завданням 3):</p>

        <table>
            <tr>
                <th>Параметр</th>
                <th>Значення</th>
            </tr>
            <tr>
                <td>ПІБ</td>
                <td>(Вкажіть тут ваше Прізвище Ім'я По-батькові)</td>
            </tr>
            <tr>
                <td>Група</td>
                <td>(Вкажіть тут вашу групу)</td>
            </tr>
            <tr>
                <td>Навчальний заклад</td>
                <td>(Наприклад, ДУІКТ)</td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Повертаємо HTTP-відповідь з цим HTML
    return HttpResponse(html_content)