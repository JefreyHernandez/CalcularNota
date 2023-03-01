import notesFunctions as nF
import sys
def insertCustomNotes(ppslist, percentages):
    notes = []
    for pp, percent in zip(ppslist, percentages):
        try:
            ppnote = float(input(f'Nota {pp} : '))
            if 0 <= ppnote <= 10:
                notes.append(ppnote * percent)
            else:
                nF.printPermitedNotes()
                sys.exit(1)
        except ValueError as ppnotetype2:
            try:
                ppnote = str(ppnotetype2).split("'")
                ppnote = ppnote[1].split('/')
                divisor = int(ppnote[0])
                divident = int(ppnote[1])
                ppnote = divisor / divident * 10
                if 0 <= ppnote <= 10:
                    notes.append(ppnote * percent)
                else:
                    nF.printPermitedNotes()
                    sys.exit(1)
            except:
                sys.exit(1)
    return notes

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
def calcUF2M01(): # TODO arreglar formula alltest
    NRA1PRACTISES = 5
    NRA2PRACTISES = 2
    NRA3PRACTISES = 3
    TOTALPRACTISES = NRA1PRACTISES + NRA2PRACTISES + NRA3PRACTISES
    NTEST = 3
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

    test1 = alltest[0]
    test2 = alltest[1]
    test3 = alltest[2]

    lessnotetest = nF.detectLessnote(alltest, MINNOTETEST)

    RA1 = ((sum(notesRA1) * 0.5) + (test1 * 0.5)) * 0.4
    RA2 = ((sum(notesRA2) * 0.5) + (test2 * 0.5)) * 0.3
    RA3 = ((sum(notesRA3) * 0.5) + (test3 * 0.5)) * 0.3

    total = round(RA1 + RA2 + RA3, 2)
    print(f"Nota amb RA1 i RA2 : {round(RA1 + RA2, 2)}")
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

    return noteM01, lessnote #
def calcUF1M03(): # TODO lessnotes
    PERCENTPR1 = 0.05
    PERCENTPR2 = 0.1
    PERCENTPE1 = 0.4
    PERCENTPP1 = 0.45
    PERCENTPR3 = 0.1
    PERCENTPR4 = 0.1
    PERCENTPP2 = 0.3
    PERCENTPR5 = 0.1
    PERCENTPP3 = 0.4
    NRA1PRACTISES = 4
    NRA2PRACTISES = 5
    TOTALPRACTISES = NRA1PRACTISES + NRA2PRACTISES

    PPLIST = ('PR1', 'PR2', 'PE1', 'PP1', 'PR3', 'PR4', 'PP2', 'PR5', 'PP3')
    PERCENTLIST = (PERCENTPR1, PERCENTPR2, PERCENTPE1, PERCENTPP1, PERCENTPR3, PERCENTPR4, PERCENTPP2, PERCENTPR5, PERCENTPP3)

    notes = insertCustomNotes(PPLIST, PERCENTLIST)

    RA1 = sum(notes[0:NRA1PRACTISES]) * 0.1
    RA2 = sum(notes[NRA1PRACTISES:TOTALPRACTISES]) * 0.9
    noteUF1 = round(RA1 + RA2, 2)
    return noteUF1
def calcUF2M03():
    PERCENTPT11 = 0.15
    PERCENTPT12 = 0.15
    PERCENTPP1 = 0.7

    PPLIST = ('PT1.1', 'PT1.2', 'PP1')
    PERCENTAGES = (PERCENTPT11, PERCENTPT12, PERCENTPP1)

    notes = insertCustomNotes(PPLIST, PERCENTAGES)

    RA1 = sum(notes)
    noteUF2 = round(RA1, 2)

    return noteUF2

def calcUF1M07():
    PERCENTX101 = 0.0294
    PERCENTX110 = 0.0294
    PERCENTX111 = 0.0294
    PERCENTX112 = 0.0294
    PERCENTX121 = 0.0588
    PERCENTX122 = 0.0588
    PERCENTX129T = 0.0882
    PERCENTX129O = 0.0882
    PERCENTX131 = 0.0294
    PERCENTX132 = 0.1618
    PERCENTX141 = 0.0588
    PERCENTX151 = 0.0294
    PERCENTX152 = 0.0588
    PERCENTX153 = 0.0294
    PERCENTX156 = 0.0588
    PERCENTX160 = 0.1618

    PPLIST = ('X101', 'X110', 'X111', 'X112', 'X121', 'X122', 'X129-TCP/IP', 'X129-OSI','X131', 'X132', 'X141', 'X151', 'X152', 'X153','X156', 'X160')
    PERCENTAGES = (PERCENTX101, PERCENTX110, PERCENTX111, PERCENTX112, PERCENTX121, PERCENTX122, PERCENTX129T,
                   PERCENTX129O, PERCENTX131, PERCENTX132, PERCENTX141, PERCENTX151, PERCENTX152, PERCENTX153,PERCENTX156, PERCENTX160)

    notes = insertCustomNotes(PPLIST, PERCENTAGES)

    total = round(sum(notes), 2)
    return total

def calcUF2M07():
    PERCENTX202 = 0.1905
    PERCENTX203 = 0.0476
    PERCENTX204 = 0.1905
    PERCENTX205 = 0.2381
    PERCENTX205C = 0.0476
    PERCENTX206 = 0.2381
    PERCENTX206C = 0.0476

    PPLIST = ('X202', 'X203', 'X204', 'X205', 'X205-C', 'X206', 'X206-C')
    PERCENTAGES = (PERCENTX202, PERCENTX203, PERCENTX204, PERCENTX205, PERCENTX205C, PERCENTX206, PERCENTX206C)

    notes = insertCustomNotes(PPLIST, PERCENTAGES)

    total = round(sum(notes), 2)
    return total