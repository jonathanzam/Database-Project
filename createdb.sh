mysql -u jz034 'jz034'<<EOFMYSQL

CREATE TABLE Team(
TeamID int NOT NULL AUTO_INCREMENT,
TeamName char(50) NOT NULL,
Nickname char(10) NOT NULL,
PRIMARY KEY (TeamID)
);

CREATE TABLE Game(
GameID int PRIMARY KEY,
Location char(50) NOT NULL,
Date char(8) NOT NULL
);

CREATE TABLE Result(
GameID int PRIMARY KEY,
TeamOneID int NOT NULL,
TeamTwoID int NOT NULL,
ScoreOne int,
ScoreTwo int,
FOREIGN KEY (GameID) REFERENCES Game(GameID),
FOREIGN KEY (TeamOneID) REFERENCES Team(TeamID),
FOREIGN KEY (TeamTwoID) REFERENCES Team(TeamID)
);

INSERT INTO Team (TeamName,Nickname) VALUES('Team 1', 'ONE');
INSERT INTO Team (TeamName,Nickname) VALUES('Team 2', 'TWO');

INSERT INTO Game VALUES(1, 'Arena', '01/01/21');
INSERT INTO Game VALUES(2, 'Arena', '01/08/21');

INSERT INTO Result VALUES(1, 1, 2, 15, 3);
INSERT INTO Result VALUES(2, 1, 2, 26, 5);


EOFMYSQL