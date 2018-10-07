from msds510 import util

records = [
     dict(year='1988',intro='Jun-88'),
     dict(year='1989', intro='May-89'),
     dict(year='2005', intro='5-May'),
     dict(year='2013', intro='13-Nov'),
     dict(year='2014', intro='14-Jan')
]

def printRecord(record):
    recordYear = record['year']
    recordIntro = record['intro']
    print('Input Record - {}'.format(record))
    getDateJoined = util.get_date_joined(recordYear,recordIntro)
    print('Date joined - {}'.format(getDateJoined))
    daysSinceJoined = util.days_since_joined(recordYear,recordIntro)
    print('Days since joined - {}'.format(daysSinceJoined))
    print('\n')

if __name__ == "__main__":
    for record in records:
        printRecord(record)
