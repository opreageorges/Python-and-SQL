def showtable(nume_tabel, sortby):
    try:
        import cx_Oracle
        connexiune = cx_Oracle.connect('####/####@####/#####')
        c = connexiune.cursor()
        allll = [1]
        i = 0
        allll[0] = 0
        for row in c.execute('SELECT column_name FROM USER_TAB_COLUMNS WHERE table_name = \'' + nume_tabel.upper() +
                             '\''):
            i = i + 1
        for row in c.execute('SELECT column_name FROM USER_TAB_COLUMNS WHERE table_name = \'' + nume_tabel.upper() +
                             '\''):
            allll.append(row[0])
        allll[0] = i

        testsortareboolean = False

        for testsortare in allll[1:allll[0]+1]:
            if sortby.upper() == testsortare.upper():
                testsortareboolean = True

        if testsortareboolean:
            for row in c.execute('select * from ' + nume_tabel + ' order by ' + sortby):
                for elem in row:
                    allll.append(elem)
        else:
            for row in c.execute('select * from ' + nume_tabel):
                for elem in row:
                    allll.append(elem)

        connexiune.close()
        return allll
    except:
        return 'Tabel invalid'
