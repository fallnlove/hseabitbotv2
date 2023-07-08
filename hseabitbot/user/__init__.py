import sqlite3

bachelor_programs = [
    'BD_Akter',
    'BD_Ant_Ist',
    'BD_Ant_Fil',
    'BD_Bible',
    'BD_BI',
    'BD_Vostok',
    'BD_GGIGT',
    'BD_ZHur',
    'BD_InYaz',
    'BD_ITSS',
    'BD_IVT',
    'BD_IB',
    'BD_ISTR',
    'BD_Isk',
    'BD_Film',
    'BD_CMB',
    'BD_KogNeir',
    'BD_Compds',
    'BD_Cultural',
    'BD_Marketing',
    'BD_Math',
    'BD_Media',
    'BD_icef',
    'BD_MO',
    'BD_MB',
    'BD_WE',
    'BD_Moda',
    'BD_Political',
    'BD_Pravo',
    'BD_AM',
    'BD_AMI',
    'BD_Data',
    'BD_SE',
    'BD_Psy',
    'BD_AD',
    'BD_CPM',
    'BD_Art',
    'BD_Soc',
    'BD_Producer',
    'BD_bba',
    'BD_Creative',
    'BD_Logistics',
    'BD_Physics',
    'BD_Philology',
    'BD_Phil',
    'BD_Ling',
    'BD_Chem',
    'BD_dlawyer',
    'BD_digital',
    'BD_Stat',
    'BD_EA',
    'BD_Iran',
    'BD_India'
]


def __init__():
    connection = sqlite3.connect('user_id.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE main_table (
     id INTEGER PRIMARY KEY,
     state_id TEXT NOT NULL
    );""")
    cursor.close()
    connection.close()

    connection = sqlite3.connect('sending.db')
    cursor = connection.cursor()
    for program in bachelor_programs:
        cursor.execute(f"""CREATE TABLE {program} (
             id INTEGER PRIMARY KEY
            );""")
    cursor.close()
    connection.close()


__init__()
