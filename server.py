from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.
                <br>
                Человечеству мала одна планета.
                <br>
                Мы сделаем обитаемыми безжизненные пока планеты.
                <br>
                И начнем с Марса!
                <br>
                Присоединяйся!'''


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}">
                    <div>Вот она какая, красная планета</div>
                  </body>
                </html>
                '''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-info" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнём с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <div class="header">на участие в миссии</div>
                            <div>
                                <form class="login_form" method="post">
                                    <input class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <div class="padded">
                                    <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    </div>
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профиссиональное</option>
                                          <option>Бакалавриат</option>
                                          <option>Специалитет</option>
                                        </select>
                                     </div>
                                    <label class="padded" for="professionSelect">Какие у Вас профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" name="profession_1">
                                        <label class="form-check-label" for="profession_1">Инженер-исследователь</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" name="profession_2">
                                        <label class="form-check-label" for="profession_2">Инженер-строитель</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" name="profession_3">
                                        <label class="form-check-label" for="profession_3">Пилот</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" name="profession_4">
                                        <label class="form-check-label" for="profession_4">Метеоролог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" name="profession_5">
                                        <label class="form-check-label" for="profession_5">Инженер по жизнеобеспечению</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" name="profession_6">
                                        <label class="form-check-label" for="profession_6">Инженер по радиационной защите</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" name="profession_7">
                                        <label class="form-check-label" for="profession_7">Врач</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" name="profession_8">
                                        <label class="form-check-label" for="profession_8">Экзобиолог</label>
                                    </div>
                                    <div class="form-group padded">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group padded">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="reason" rows="3" name="reason"></textarea>
                                    </div>
                                    <div class="form-group padded">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check padded">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        professions = ['Инженер-исследователь', 'Инженер-строитель', 'Пилот', 'Метеоролог',
                       'Инженер по жизнеобеспечению', 'Инженер по радиационной защите',
                       'Врач','Экзобиолог']
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print([*filter(lambda x: f'profession_{professions.index(x) + 1}' in request.form.keys(), professions)])
        print(request.form['sex'])
        print(request.form['reason'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    planet_descriptions = {'Марс': ['Эта планета близка к Земле;',
                                    'На ней много необходимых ресурсов;',
                                    'На ней есть вода и атмосфера;',
                                    'На ней есть небольшое магнитное поле;',
                                    'Наконец, она просто красива;'],
                           'Меркурий': ['Не будет проблем с энергией благодаря близкому расположению к Солнцу;',
                                        'Наличие магнитного поля;',
                                        'Имеются ледяные шапки;',
                                        'Суточные перепады температуры минимальны;',
                                        'Планета богата полезными ресурсами;'],
                           'Венера': ['Добираться до Венеры гораздо проще, чем к любой другой планете;',
                                      'Если решить проблему с облаками, то вполне реально получить в итоге условия, подобные земным;',
                                      'Диаметр и масса очень схожи с Землей;',
                                      'Возможно в недрах планеты есть вода;',
                                      'Бомбардировка Венеры кометами и астероидами, которые несут лёд позволит занчительно снизить температуру;',
                                      'Для формирования гидросферы можно добавить водоросли и земные микроорганизмы;'],
                           'Сатурн': ['Планета не утонет, если поместить ее в воду)));',
                                      'Ядро планеты сходно с земным;',
                                      'На планете периодически появляются бури, размер которых может превосходить габариты Земли;',
                                      'Имеет 62 спутника;',
                                      'Находиться на поверхности не представляется возможным, однако жизнь может быть на его спутниках;'],
                           'Уран': ['Безумные ветра (более 800 км/ч). На такой скорости будет сметать всё на своем пути;',
                                    'Нет твердой поверхности;',
                                    'Пахнет тут специфически. Сероводород и аммиак не самые ароматные составы;',
                                    'Грозы колоссальных масштабов;',
                                    'Планету можно будет использовать в качестве колонии по добыче гелия-3;',],
                           'Нептун': ['Синий цвет нептуновым облакам придает метан;',
                                      'У Нептуна 14 спутников;',
                                      'Для колонизации подошел бы крупнейший спутник - Тритон;',
                                      'На нем есть следы тектонической активности и криовулканы, извергающие азот;',
                                      'Низкая температура;',],
                           'Юпитер': ['Носит имя главы римского пантеона;',
                                      'Здесь есть огромные сила тяжести, магнитное поле и радиационные пояса;',
                                      'У Юпитера насчитывается 79 спутников;',
                                      'На Ио, Евпропе, Ганимеде и Каллисто предполагается наличие подледных океанов, и даже, возможно, жизни;',
                                      'При их освоении могут возникнуть технические трудности;']
                           }
    description = planet_descriptions[planet_name]
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <div class="alert" role="alert">
                      {description[0]}
                    </div>
                    <div class="alert alert-success" role="alert">
                      {description[1]}
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      {description[2]}
                    </div>
                    <div class="alert alert-warning" role="alert">
                      {description[3]}
                    </div>
                    <div class="alert alert-danger" role="alert">
                      {description[4]}
                    </div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h3>
                      Претендента на участие в миссии {nickname}:
                    </h3>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert" role="alert">
                      состовляет {rating}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title='Тренировка', prof=prof)


@app.route('/list_prof')
def list_prof():
    return render_template('list_prof.html', title='Список профессий')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
