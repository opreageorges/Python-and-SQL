from flask import Flask, render_template, request

# ####/####@####/#####


app = Flask(__name__)


@app.route('/')
def mainpage():
    return render_template('index.html')


@app.route('/Vizualizare_tabeluri')
def viz_tab():
    table = []
    sortby = " "
    if request.args['ntab']:
        condition = 1
        num_tab = request.args['ntab']
        if request.args['stab']:
            sortby = request.args['stab']
        import showtable
        table = showtable.showtable(num_tab, sortby)
        if table == 'Tabel invalid':
            condition = -1

    else:
        condition = 0

    return render_template('viz_tab.html', condition=condition, table=table, lungimea=len(table))


@app.route('/Stergere')
def deleteentry():
    import functii
    condition = 3
    table_name = request.args['ntab']
    if table_name != '':
        if functii.checktableexist(table_name) and functii.deletefromtable(table_name, request.args['info']):
            condition = 1
        else:
            condition = 0
    return render_template('stergeintrare.html', condition=condition)


@app.route('/Editare')
def editentry():
    import functii
    condition = 3
    table_name = request.args['ntab']
    if table_name != '':
        if functii.checktableexist(table_name) and functii.editfromtable(table_name, request.args['info'], request.args['camp'], request.args['nvalue']) and request.args['camp'] != '':
            condition = 1
        else:
            condition = -1
    return render_template('edittable.html', condition=condition)


@app.route('/Afisdin3tabele')
def afisaredin3tabele():
    import functii
    conditie = 0
    table = ''
    if request.args['ncli'] != '':
        table = functii.threetablecheck( request.args['ncli'], request.args['nprod'])
        if table != '':
            conditie = 1
        else:
            conditie = -1
    return render_template('afis_info.html', condition=conditie, table=table)


@app.route('/<variabila>')
def daily_post(variabila):
    return str(variabila)

# def test():
#     import showtable
#     num_tab = 'Angajati'
#     table = showtable.showtable(num_tab)
#     print(table,'\n', int(len(table)/table[0])-1)
#
# test()\
