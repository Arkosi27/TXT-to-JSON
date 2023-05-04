text = """
Genesis: Gen, Ge, Gn
Exodus: Exod, Ex, Exo
Leviticus: Lev, Lv, Le
Numbers: Num, Nu, Nm
Deuteronomy: Deut, Dt, Deu
Joshua: Josh, Jos, Jsh
Judges: Judg, Jdg, Jg
Ruth: Ruth, Ru, Rt
1 Samuel: 1 Sam, 1 Sa, 1 Sm
2 Samuel: 2 Sam, 2 Sa, 2 Sm
1 Kings: 1 Kgs, 1 Ki, 1 Kin
2 Kings: 2 Kgs, 2 Ki, 2 Kin
1 Chronicles: 1 Chron, 1 Chr, 1 Ch
2 Chronicles: 2 Chron, 2 Chr, 2 Ch
Ezra: Ezra, Ezr, Ez
Nehemiah: Neh, Ne, Nee
Esther: Esth, Est, Es
Job: Job, Jb, J
Psalms: Psalms, Ps, Pss
Proverbs: Prov, Prv, Pro
Ecclesiastes: Eccles, Eccl, Ecc
Song of Solomon: Song of Sol, Song, So
Isaiah: Isa, Is
Jeremiah: Jer, Je, Jr
Lamentations: Lam, La,
Lm Ezekiel: Ezek,Ezk,Eze Daniel:
Dan,Da,Dl Hosea:
Hos,Ho Joel:
Joel,Joe,Jl Amos:
Amos,Amm Amo Obadiah:
Obad Ob Oba Jonah:
Jonah Jon Jnh Micah:
Micah Mic Mc Nahum:
Nah Na Nhm Habakkuk:
Hab Hb Hk Zephaniah:
Zeph Zep Zp Haggai:
Hag Hg Hgg Zechariah:
Zech Zec Zc Malachi:
Mal Ml Mlc Matthew:
Matt Mt Mat Mark:
Mk Mrk Mar Luke:
Lk Luk John:
Jn Joh Jhn Acts:
Acts Ac Act Romans:
Rom Ro Rm Corinthians:
Cor Co Corin Galatians:
Gal Ga Gl Ephesians:
Eph Ep Ephp Philippians:
Phil Php Philp Colossians:
Col Co Coss Thessalonians:
Thess Thes Th Timothy:
Tim Ti Tm Titus:
Titus Tit Ti Philemon:
Philem Phile Phlm Hebrews:
Heb Hb Hebr James:
Jas Jms Ja Peter:
Pet Pe Pt John:
Jn Joh Jhn Jude:
Jude Jud Jd Revelation:
Rev Re Rv
Ezekiel: Ezek, Ezk, Eze
    Daniel: Dan, Da, Dl
    Hosea: Hos, Ho
    Joel: Joel, Joe, Jl
    Amos: Amos, Am, Amo
    Obadiah: Obad, Ob, Oba
    Jonah: Jonah, Jon, Jnh
    Micah: Micah, Mic, Mc
    Nahum: Nah, Na, Nhm
    Habakkuk: Hab, Hb, Hk
    Zephaniah: Zeph, Zep, Zp
    Haggai: Hag, Hg, Hgg
    Zechariah: Zech, Zec, Zc
    Malachi: Mal, Ml, Mlc 
New Testament:
    Matthew: Matt, Mt, Mat
    Mark: Mk, Mrk, Mar
    Luke: Lk, Luk
    John: Jn, Joh, Jhn
    Acts: Acts, Ac, Act
    Romans: Rom, Ro, Rm
    1 Corinthians: 1 Cor, 1 Co, 1 Corin
    2 Corinthians: 2 Cor, 2 Co, 2 Corin
    Galatians: Gal, Ga, Gl
    Ephesians: Eph, Ep, Ephp
    Philippians: Phil, Php, Philp
    Colossians: Col, Co, Coss
    1 Thessalonians: 1 Thess, 1 Thes, 1 Th
    2 Thessalonians: 2 Thess, 2 Thes, 2 Th
    1 Timothy: 1 Tim, 1 Ti, 1 Tm
    2 Timothy: 2 Tim, 2 Ti, 2 Tm
    Titus: Titus, Tit, Ti
    Philemon: Philem, Phile, Phlm
    Hebrews: Heb, Hb, Hebr
    James: Jas, Jms, Ja
    1 Peter: 1 Pet, 1 Pe, 1 Pt
    2 Peter: 2 Pet, 2 Pe, 2 Pt
    1 John: 1 Jn, 1 Joh, 1 Jhn
    2 John: 2 Jn, 2 Joh, 2 Jhn
    3 John: 3 Jn, 3 Joh, 3 Jhn
    Jude: Jude, Jud, Jd
    Revelation: Rev, Re, Rv"""

lines = text.split('\n')
abbreviations = []
for line in lines:
    if ':' in line and ',' in line and len(line.split(':')) == 2 and len(line.split(':')[-1].split(',')) > 0 :
        abbrs = line.split(':')[-1].split(',')
        for abbr in abbrs:
            abbreviations.append(abbr.strip())

print(abbreviations)