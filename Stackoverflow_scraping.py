import requests
from bs4 import BeautifulSoup

r = requests.get('https://pt.stackoverflow.com/')
if r.status_code == 200: # Retorno da request
    #print('Entramos!')
    #print(r.content) Utilizamos o content pois ele é binário, o necessário para fazer o soup, text é unicode
    soup = BeautifulSoup(r.content, 'html.parser') # Transformo para o BeautifulSoup, que facilita o reconhecimento html
    #print(soup.prettify()) Mostra como fica organizado o html
    #print(soup.div) Mostro como fica se pegarmos só a tag, onde se selecionamos algo que possui mais de um, ele mostra o primeiro
    print('===== Home da', soup.title.string, '=====') # Beleza, mostrando o title
    for summary in soup.find_all('div', class_='question-summary'): # Buscando todas as divs com a classe 'question-summary'
        for question in summary.find_all('a', class_='question-hyperlink'): # Pegando valores dentro de divs já filtradas, poderia ter feito direto
            #print(question) Mostra as anchors inteiras
            print('Pergunta:', question.string, '| Link:', question['href']) # Formatado
else:
    print('Algum erro ocorreu...')

interesse = 'javascript'
print('===== Tópicos de {} ====='.format(interesse))
params = {'q':interesse} # Quais parametros posso utilizar, no caso estou fazendo uma busca
r2 = requests.get('https://pt.stackoverflow.com/search', params=params)
if r2.status_code == 200:
    soup = BeautifulSoup(r2.content, 'html.parser')
    for question in soup.find_all('a', class_='question-hyperlink'): # Faço a busca direta pelos Anchors
        print('Pergunta:', question.string, '| Link:', question['href'])
else:
    print('Algum erro ocorreu...')

print('===== Páginas de perguntas =====')
for page in range(1,3): # O último do range não conta
    print('Página {}'.format(page))
    r3 = requests.get('https://pt.stackoverflow.com/questions', params={'page':page})
    if r3.status_code == 200: # Repito o processo do interesse
        soup = BeautifulSoup(r3.content, 'html.parser')
        for question in soup.find_all('a', class_='question-hyperlink'):
            print('Pergunta:', question.string, '| Link:', question['href'])
    else:
        print('Algum erro ocorreu...')

