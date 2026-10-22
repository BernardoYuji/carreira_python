from wsgiref.simple_server import make_server

def aplicacao(environ, start_response):
    produtos = [
        {'nome': 'Computador', 'valor': 7499.99},
        {'nome': 'Smartphone', 'valor': 4000.00},
        {'nome': 'Videogame', 'valor': 3500.00},
        {'nome': 'Tablet', 'valor': 2999.99},
    ]

    linhas_html = ''
    for produto in produtos:
        linhas_html += f'<li>{produto['nome']} - R${produto['valor']}</li>'

    start_response('200 Ok', [('Content-type', 'text/html;charset=utf-8')])

    with open('./flask/index.html', 'r', encoding='utf-8') as file:
        html = file.read()

    html_final = html.replace('{{PRODUTOS}}', linhas_html)
    return [html_final.encode('utf-8')]

make_server('', 5000, aplicacao).serve_forever()
