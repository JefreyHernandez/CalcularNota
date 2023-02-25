import notesFunctions as nF
def calcUF1M01():
    NRA1PRACTISES = 5
    NRA2PRACTISES = 2
    TOTALPRACTISES = NRA1PRACTISES + NRA2PRACTISES
    PERCENTPPRA1 = 0.1
    PERCENTPPRA2 = 0.25
    MINNOTEPP = 5
    MINNOTETEST = 4

    allpps = nF.insertPP(TOTALPRACTISES)

    lessnotepp = nF.detectLessnote(allpps, MINNOTEPP)

    notesRA1 = [pp * PERCENTPPRA1 for pp in allpps[0:NRA1PRACTISES]]
    notesRA2 = [pp * PERCENTPPRA2 for pp in allpps[NRA1PRACTISES:TOTALPRACTISES]]

    test = float(input('Nota del test UF1? : '))
    if test < MINNOTETEST:
        lessnotetest = True
    else:
        lessnotetest = False

    RA1 = (sum(notesRA1) + (test * 0.5)) * 0.5
    RA2 = (sum(notesRA2) + (test * 0.5)) * 0.5

    total = round(RA1 + RA2, 2)

    lessnote = lessnotepp or lessnotetest

    return total, lessnote
def calcUF2M01():
    NRA1PRACTISES = 5
    NRA2PRACTISES = 2
    NRA3PRACTISES = 3
    TOTALPRACTISES = NRA1PRACTISES + NRA2PRACTISES + NRA3PRACTISES
    NTEST = 2
    PERCENTPPRA1 = 0.1
    PERCENTPPRA2 = 0.25
    PERCENTPPRA3 = 0.17
    MINNOTEPP = 5
    MINNOTETEST = 4

    allpps = nF.insertPP(TOTALPRACTISES)

    lessnotepp = nF.detectLessnote(allpps, MINNOTEPP)

    notesRA1 = [pp * PERCENTPPRA1 for pp in allpps[0:NRA1PRACTISES]]
    notesRA2 = [pp * PERCENTPPRA2 for pp in allpps[NRA1PRACTISES:NRA1PRACTISES + NRA2PRACTISES]]
    notesRA3 = [pp * PERCENTPPRA3 for pp in allpps[NRA1PRACTISES + NRA2PRACTISES:TOTALPRACTISES]]

    alltest = nF.insertTEST(NTEST)
    mediaTests = sum(alltest) / len(alltest)

    lessnotetest = nF.detectLessnote(alltest, MINNOTETEST)

    RA1 = ((sum(notesRA1) * 0.5) + (mediaTests * 0.5)) * 0.4
    RA2 = ((sum(notesRA2) * 0.5) + (mediaTests * 0.5)) * 0.3
    RA3 = ((sum(notesRA3) * 0.5) + (mediaTests * 0.5)) * 0.3

    total = round(RA1 + RA2 + RA3, 2)
    lessnote = lessnotepp or lessnotetest

    return total, lessnote
def calcM01():
    PERCENTUF1 = 0.3
    PERCENTUF2 = 0.4
    PERCENTUF3 = 0.1
    PERCENTUF4 = 0.2
    NUMBERUFS = 4

    option = input('Tienes las notas de las UF? [s/n]: ')
    if option == 's':
        noteList = nF.getUFNotes(NUMBERUFS)
        noteUF1 = noteList[0]
        noteUF2 = noteList[1]
        noteUF3 = noteList[2]
        noteUF4 = noteList[3]
    else:
        noteUF1, lessnoteUF1 = calcUF1M01()
        noteUF2, lessnoteUF2 = calcUF2M01()
        #noteUF3, lessnoteUF3 = calcUF3M01()
        #noteUF4, lessnoteUF4 = calcUF4M01()

    lessnote = lessnoteUF1 or lessnoteUF2 #or lessnoteUF3 or lessnoteUF4

    noteM01 = noteUF1 * PERCENTUF1 + noteUF2 * PERCENTUF2 #+ noteUF3 * PERCENTUF3 + noteUF4 * PERCENTUF4

    return noteM01, lessnote