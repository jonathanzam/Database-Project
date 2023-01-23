import sys
import traceback
import logging
import mysql.connector
from tabulate import tabulate

mysql_username = 'jz034'
mysql_password= ''
           
def open_database (hostname,user_name,mysql_pw,database_name):
      global conn
      conn= mysql.connector.connect(host= hostname, 
      user= user_name,  
      password= mysql_pw, 
      database= database_name 
    ) 
      global cursor
      cursor = conn.cursor(buffered = True) 


def printFormat(result):
    header=[]
    for cd in cursor.description:# get headers
        header.append(cd[0])
    print('')
    #print('Query Result:')
    print('')
    print(tabulate(result, headers=header, tablefmt='html', stralign='center', numalign='center'))# print results in table format


def executeSelect (query):
    cursor.execute(query)
    printFormat(cursor.fetchall())


def insert(table,values):
     query ="INSERT into " + table + " values (" + values + ")" +';'
     cursor.execute(query)
     conn.commit()


def checkIfExists(query):
    #print ("\ncheck")
    cursor.execute(f'{query}')
    row_count = cursor.rowcount
    if row_count == 0:
        #print('\nNot a valid entry')
        return False

    return True


def addTeam():
    #print("Testing add team")
    #teamID = input("\nEnter team ID: ")
    try:
        open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
        
        # res = python_db.executeSelect('SELECT * FROM Team;')
        # res = res.split('\n')
        # print("<br/>" + "Table Team before:" + "<br/>" + res[0] + "<br/>" + res[1] + "<br/>")

        teamName = sys.argv[2]
        teamNickname = sys.argv[3]

        #print(teamName + '\n' + teamNickname)

    # values = (f'{teamID}, \'{teamName}\', \'{teamNickname}\'')
        #python_db.insert('Team', values)

        insert('Team (TeamName,Nickname)',f'\'{teamName}\', \'{teamNickname}\'')
        executeSelect(f'SELECT * FROM Team;')
        

        close_db() #close db
    except Exception as e:
        logging.error(traceback.format_exc())  


def addGame():
    try:
        open_database('localhost',mysql_username,mysql_password,mysql_username) # open database

        gameID = sys.argv[2]
        gameLocation = sys.argv[3]
        gameDate = sys.argv[4]

        insert('Game',f'{gameID}, \'{gameLocation}\', \'{gameDate}\'')

        executeSelect(f'SELECT * FROM Game;')
        close_db() #close db
    except Exception as e:
        logging.error(traceback.format_exc()) 



def addResult():
    #print("testing add result...")
    try:
        open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
        

        gameID = sys.argv[2]
        teamOneID = sys.argv[3]
        teamTwoID = sys.argv[4]
        scoreOne = sys.argv[5]
        scoreTwo = sys.argv[6]

        insert('Result',f'{gameID}, {teamOneID}, {teamTwoID}, {scoreOne}, {scoreTwo}')
        
        executeSelect(f'SELECT * FROM Result;')

        close_db() #close db
    except Exception as e:
        logging.error(traceback.format_exc())  


def viewTeams():
    #print("Testing view teams:")
    try:
        open_database('localhost',mysql_username,mysql_password,mysql_username)

        executeSelect('SELECT * FROM Team;')

        close_db() #close db
    except Exception as e:
        logging.error(traceback.format_exc())


def viewResultsTeam():
    #print("testing viewing results by game: ")
    #display the Team name, their nickname, and each result. 
    #Include their opponent, the date of the game, and the score. Indicate whether the won or lost.

    try:
        open_database('localhost',mysql_username,mysql_password,mysql_username)

        teamName = sys.argv[2]

        executeSelect(f"select IF (T1.TeamName = \'{teamName}\', \
        T1.TeamName, T2.TeamName) AS \'Team Name\', IF(T1.TeamName = \
        \'{teamName}\',  T1.Nickname, T2.Nickname) AS \'Team Nickname\', IF \
        (T1.TeamName = \'{teamName}\', T2.TeamName, T1.TeamName) AS \
        Opponent, Game.Date, IF (T1.TeamName = \'{teamName}\', R1.ScoreOne, \
        R1.ScoreTwo) \'Team Score\', IF (T1.TeamName = \'{teamName}\', R1.ScoreTwo, \
        R1.ScoreOne) \'Opponent Score\', IF (R1.ScoreOne > R1.ScoreTwo, T1.TeamName, \
        T2.TeamName) AS \'Winning Team\' FROM Result R1 JOIN Team T1 on T1.TeamId = \
        R1.TeamOneId JOIN Team T2 on  T2.TeamId = R1.TeamTwoId JOIN Game on Game.GameId = \
        R1.GameId WHERE T1.TeamName = \'{teamName}\' OR T2.TeamName = \
        \'{teamName}\';")

        close_db() #close db
    except Exception as e:
        logging.error(traceback.format_exc())



def viewResultsDate():
    #print("Testing results by date: ")

    try:
        open_database('localhost',mysql_username,mysql_password,mysql_username)

        date = sys.argv[2]

        executeSelect(f"select T1.TeamName as \'1st Team\', \
	    T2.TeamName AS \'2nd Team\', Game.Location, R1.ScoreOne AS \'1st Team Score\', \
	    R1.ScoreTwo AS \'2nd Team Score\', IF (R1.ScoreOne > R1.ScoreTwo, T1.TeamName, \
	    T2.TeamName) AS \'Winning Team\' FROM Result R1 JOIN Team T1 on T1.TeamId = \
	    R1.TeamOneId JOIN Team T2 on  T2.TeamId = R1.TeamTwoId JOIN Game on Game.GameId = \
	    R1.GameId WHERE Game.Date = \'{date}\';")


        close_db() #close db
    except Exception as e:
        logging.error(traceback.format_exc())

def close_db ():  # use this function to close db
    cursor.close()
    conn.close()


function = sys.argv[1]
if function == '1':
    addTeam()
elif function == '2':
    addGame()
elif function == '3':
    addResult()
elif function == '4':
    viewTeams()
elif function == '5':
    viewResultsTeam()
elif function == '6':
    viewResultsDate()
