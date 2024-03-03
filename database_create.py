import sqlite3
from datetime import datetime
import csv

conn = sqlite3.connect('gym.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

# to drop the table if it exists
conn.execute('DROP TABLE IF EXISTS powerlift')

conn.execute('DROP TABLE IF EXISTS meets_data')

conn.execute('''
    CREATE TABLE powerlift (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SN INTEGER,
        MeetID INTEGER,
        Name TEXT,
        Sex TEXT,
        Equipment TEXT,
        Age INTEGER,
        Division TEXT,
        BodyweightKg REAL,
        WeightClassKg INTEGER,
        Squat4Kg REAL,
        BestSquatKg REAL,
        Bench4Kg REAL,
        BestBenchKg REAL,
        Deadlift4Kg REAL,
        BestDeadliftKg REAL,
        TotalKg REAL,
        Place INTEGER,
        Wilks REAL
    )
''')
# Create the table for meets data
conn.execute('CREATE TABLE meets_data (id INTEGER PRIMARY KEY AUTOINCREMENT, MeetID INTEGER, MeetPath TEXT, Date DATETIME, MeetCountry TEXT, MeetState TEXT, MeetTown TEXT, MeetName TEXT)')

# Process powerlift.csv
with open('powerlift.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        meet_id = int(row['MeetID'])
        existing_record = cur.execute('SELECT MeetID FROM powerlift WHERE MeetID = ?', (meet_id,)).fetchone()

        if existing_record:
            print(f"MeetID {meet_id} already exists in powerlift. Skipping insertion. Row: {row}")
        else:
            try:
                cur.execute("INSERT INTO powerlift (SN, MeetID, Name, Sex, Equipment, Age, Division, BodyweightKg, WeightClassKg, Squat4Kg, BestSquatKg, Bench4Kg, BestBenchKg, Deadlift4Kg, BestDeadliftKg, TotalKg, Place, Wilks) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                    int(row['SN']) if 'SN' in row else None,
                    meet_id,
                    row.get('Name', None),
                    row.get('Sex', None),
                    row.get('Equipment', None),
                    int(row['Age']) if 'Age' in row and row['Age'].isdigit() else None,
                    row.get('Division', None),
                    float(row['BodyweightKg']) if 'BodyweightKg' in row and row['BodyweightKg'].replace('.', '', 1).isdigit() else None,
                    int(row['WeightClassKg']) if 'WeightClassKg' in row and row['WeightClassKg'].isdigit() else None,
                    float(row['Squat4Kg']) if 'Squat4Kg' in row and row['Squat4Kg'].replace('.', '', 1).isdigit() else None,
                    float(row['BestSquatKg']) if 'BestSquatKg' in row and row['BestSquatKg'].replace('.', '', 1).isdigit() else None,
                    float(row['Bench4Kg']) if 'Bench4Kg' in row and row['Bench4Kg'].replace('.', '', 1).isdigit() else None,
                    float(row['BestBenchKg']) if 'BestBenchKg' in row and row['BestBenchKg'].replace('.', '', 1).isdigit() else None,
                    float(row['Deadlift4Kg']) if 'Deadlift4Kg' in row and row['Deadlift4Kg'].replace('.', '', 1).isdigit() else None,
                    float(row['BestDeadliftKg']) if 'BestDeadliftKg' in row and row['BestDeadliftKg'].replace('.', '', 1).isdigit() else None,
                    float(row['TotalKg']) if 'TotalKg' in row and row['TotalKg'].replace('.', '', 1).isdigit() else None,
                    int(row['Place']) if 'Place' in row and row['Place'].isdigit() else None,
                    float(row['Wilks']) if 'Wilks' in row and row['Wilks'].replace('.', '', 1).isdigit() else None
                ))
                conn.commit()
            except Exception as e:
                print(f"Error inserting row into powerlift: {row}, Error: {e}")

# Process meets.csv
with open('meets.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        meet_id = int(row['MeetID'])
        existing_record = cur.execute('SELECT MeetID FROM meets_data WHERE MeetID = ?', (meet_id,)).fetchone()

        if existing_record:
            print(f"MeetID {meet_id} already exists in meets_data. Skipping insertion. Row: {row}")
        else:
            try:
                cur.execute('INSERT INTO meets_data VALUES(NULL,?,?,?,?,?,?,?)', (
                    meet_id, row['MeetPath'],
                    datetime.strptime(row['Date'], '%d/%m/%Y'),
                    row['MeetCountry'], row['MeetState'],
                    row['MeetTown'], row['MeetName']
                ))
                conn.commit()
            except Exception as e:
                print(f"Error inserting row into meets_data: {row}, Error: {e}")

# Close the connection
conn.close()
