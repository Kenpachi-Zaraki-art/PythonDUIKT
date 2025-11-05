from django.http import HttpResponse


def main_page_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <title>Про мене</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #f0f2f5;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .container {
                width: 90%;
                max-width: 700px;
                background-color: #ffffff;
                padding: 2.5rem;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            }
            h1 {
                color: #1c1e21;
                text-align: center;
                margin-top: 0;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 1.5rem;
            }
            th, td {
                padding: 12px 15px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
            th {
                color: #555;
                font-weight: 600;
                width: 30%;
            }
            tr:last-child th,
            tr:last-child td {
                border-bottom: none;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <h1>Моя персональна сторінка</h1>
            <p>Інформація про мене:</p>

            <table>
                <tr>
                    <th>Параметр</th>
                    <th>Значення</th>
                </tr>
                <tr>
                    <td>ПІБ</td>
                    <td>Руденок Денис Олегович</td>
                </tr>
                <tr>
                    <td>Група</td>
                    <td>ІСД-31</td>
                </tr>
                <tr>
                    <td>Навчальний заклад</td>
                    <td>ДУІКТ</td>
                </tr>
            </table>
        </div>

    </body>
    </html>
    """

    return HttpResponse(html_content)