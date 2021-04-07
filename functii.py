import cx_Oracle


def checktableexist(nume_tabel):
    connexiune = cx_Oracle.connect('####/####@####/#####')
    c = connexiune.cursor()
    try:
        c.execute('select * from ' + nume_tabel)
        connexiune.close()
        return True
    except:
        connexiune.close()
        return False


def deletefromtable(nume_tabel, idul):
    connexiune = cx_Oracle.connect('####/####@####/#####')
    c = connexiune.cursor()
    try:
        x = ''
        for row in c.execute('SELECT column_name FROM USER_TAB_COLUMNS WHERE table_name = \'' + nume_tabel.upper() +
                             '\''):
            x = row[0]
            break

        c.execute('DELETE FROM ' + nume_tabel + ' WHERE ' + str(x) + ' = ' + str(idul))
        c.execute('commit')
        connexiune.close()
        return True
    except:
        connexiune.close()
        return False

def editfromtable(nume_tabel, idul, campul, noua_valoare):
    connexiune = cx_Oracle.connect('####/####@####/#####')
    try:
        c = connexiune.cursor()
        x = ''
        for row in c.execute('SELECT column_name FROM USER_TAB_COLUMNS WHERE table_name = \'' + nume_tabel.upper() +
                             '\''):
            x = row[0]
            break

        c.execute('UPDATE ' + nume_tabel + ' SET ' + campul + ' = ' '\'' + noua_valoare + '\'' ' WHERE ' + x + '=' + idul)
        c.execute('commit')
        connexiune.close()
        return True
    except:
        connexiune.close()
        return False


def threetablecheck(client, produs):
    connexiune = cx_Oracle.connect('####/####@####/#####')
    try:
        c = connexiune.cursor()
        produse = []
        clientul = []
        for prod in c.execute('select id_prod, nume, id_furn from produse where nume = \'' + str(produs) + '\''):
            produse.append(prod[0])
            produse.append(prod[1])
            produse.append(prod[2])

        for clt in c.execute('select ID_CLIENT, NUME from clienti where nume = \'' + str(client) + '\''):
            clientul.append(clt[0])
            clientul.append(clt[1])
        furn = []
        nrcomanda = [0]
        for nrb in c.execute('select Nr_comanda from nr_bucati where id_prod = \'' + str(produse[0]) + '\' and id_client = \'' + str(clientul[0]) + '\''):
            if str(nrb) == str(nrcomanda[len(nrcomanda)-1]):
                nrcomanda.append(nrb)

        for id_furn_prod in range(2, int(len(produse)/3) + 2,3):
            for frn in c.execute('select NUME_furn from furnizori where id_furn = \'' + str(produse[2]) + '\''):
                furn.append(frn[0])

        if len(nrcomanda) == 1:
            final = " o singura data"
        else:
            final = 'de ' + str(len(nrcomanda)) + ' ori'

        table = ''
        table = table + 'Da, ' + produse[1] + ', vandut de ' + furn[0] + ', a fost comandat de ' + clientul[1] + final
        connexiune.close()
        return table
    except:
        connexiune.close()
        return ''
