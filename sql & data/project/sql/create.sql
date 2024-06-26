DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Comments;
DROP TABLE IF EXISTS Photos;
DROP TABLE IF EXISTS Views;
DROP TABLE IF EXISTS PhotoLikes;
DROP TABLE IF EXISTS Tagged;
DROP TABLE IF EXISTS CommentLikes;
DROP TABLE IF EXISTS Follows;

---------------------------------------------------------------------------------------------------------

--Entities Tables:
CREATE TABLE Users
(
	username VARCHAR(64) NOT NULL,
	email VARCHAR(64),
	pass VARCHAR(64) NOT NULL,  
	numFollows BIGINT NOT NULL,
	PRIMARY KEY (username)
);
CREATE TABLE Photos
(
	photo_id VARCHAR(64) NOT NULL,
	publisher VARCHAR(64) NOT NULL,
	dates DATE NOT NULL,
	privacy BIT NOT NULL,
	description VARCHAR(512),
	numLikes BIGINT NOT NULL,
	numViews BIGINT NOT NULL,
	PRIMARY KEY(photo_id),
	FOREIGN KEY(publisher) REFERENCES Users(username) ON DELETE CASCADE
);
CREATE TABLE Comments
(
	comment_id BIGINT NOT NULL,
	comments VARCHAR(1024),
	username VARCHAR(64) NOT NULL,
	photo_id VARCHAR(64) NOT NULL,
	dates DATE NOT NULL,
	numLikes BIGINT NOT NULL,
	PRIMARY KEY(comment_id),
	FOREIGN KEY(username) REFERENCES Users(username) ON DELETE CASCADE,
	FOREIGN KEY(photo_id) REFERENCES Photos(photo_id) ON DELETE CASCADE
);


--------------------------------------------------------------------------------------------------------
--Relation Tables:
CREATE TABLE Views
(
	username VARCHAR(64) NOT NULL,
	photo_id VARCHAR(64) NOT NULL,
	PRIMARY KEY(username,photo_id),
	FOREIGN KEY(username) REFERENCES Users(username) ON DELETE CASCADE,
	FOREIGN KEY(photo_id) REFERENCES Photos(photo_id) ON DELETE CASCADE
);
CREATE TABLE PhotoLikes
(
	username VARCHAR(64) NOT NULL,
	photo_id VARCHAR(64) NOT NULL,
	PRIMARY KEY(username, photo_id),
	FOREIGN KEY(username) REFERENCES Users(username) ON DELETE CASCADE,
	FOREIGN KEY(photo_id) REFERENCES Photos(photo_id) ON DELETE CASCADE
);
--all the people who are tagged in the photo
CREATE TABLE Tagged
(
	username VARCHAR(64) NOT NULL,
	photo_id VARCHAR(64) NOT NULL,
	PRIMARY KEY(username, photo_id),
	FOREIGN KEY(username) REFERENCES Users(username) ON DELETE CASCADE,
	FOREIGN KEY(photo_id) REFERENCES Photos(photo_id) ON DELETE CASCADE
);
 --User Likes a Comment
CREATE TABLE Likes
(
	username VARCHAR(64) NOT NULL,
	comment_id BIGINT NOT NULL,
	PRIMARY KEY(username, comment_id), FOREIGN KEY(username) REFERENCES Users(username) ON DELETE CASCADE,
	FOREIGN KEY(comment_id) REFERENCES Comments(comment_id) ON DELETE CASCADE
);
--1 follows 2
CREATE TABLE Follows
(
	username1 VARCHAR(64) NOT NULL,
	username2 VARCHAR(64) NOT NULL,
	PRIMARY KEY(username1, username2),
	FOREIGN KEY(username1) REFERENCES Users(username) ON DELETE CASCADE,
	FOREIGN KEY(username2) REFERENCES Users(username) ON DELETE CASCADE
);

--===================================================================
----------------------------
-- INSERT DATA STATEMENTS --
----------------------------
--Entity Data
COPY Users (
	username,
	email,
	pass,
	numFollows
)
FROM 'Users.csv'
WITH DELIMITER ',' NULL AS ''
CSV HEADER;

COPY Photos (
	photo_id,
	publisher,
	dates,
	privacy,
	description,
	numLikes,
	numViews
)
FROM 'Photos.csv'
WITH DELIMITER ','
CSV HEADER;

COPY Comments(
	comment_id,
	comments,
	username,
	photo_id,
	dates,
	numLikes
)
FROM 'Comments.csv'
WITH DELIMITER ',' NULL AS ''
CSV HEADER;




--------------------------------------------------------------------------------------------------------
--Relations Data
COPY Views (
	username,
	photo_id
)
FROM 'Views.csv'
WITH DELIMITER ','
CSV HEADER;

COPY PhotoLikes(
	username,
	photo_id
)
FROM 'PhotoLikes.csv'
WITH DELIMITER ','
CSV HEADER;

COPY Tagged(
	username,
	photo_id
)
FROM 'Tagged.csv'
WITH DELIMITER ','
CSV HEADER;

COPY Likes (
	username,
	comment_id
)
FROM 'Likes.csv'
WITH DELIMITER ','
CSV HEADER;

COPY Follows(
	username1,
	username2
)
FROM 'Follows.csv'
WITH DELIMITER ','
CSV HEADER;

