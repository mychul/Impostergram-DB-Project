# Impostergram-DB-Project
Fall 2020  
Michael Chiang   
Tinh La  
Mingi Lee  

Project Summary:
Purpose: 
This project is a photo-sharing service much like Instagram, where users can upload photos and share them with other users. We are building this project to interact with and learn how to handle a hybrid SQL and NOSQL environment. To accomplish this we have implemented Postgresql and Mongodb into our design to handle their respective sql natures.  
Instagram is a social networking service which enables its users to upload and share their photos  and videos with other users. Instagram users can choose to share information either publicly or privately. Anything shared publicly can be seen by any other user, whereas privately shared content can only be accessed by a specified set of people. Instagram also enables its users to share through many other social networking platforms, such as Facebook, Twitter, Flickr, and Tumblr. 
For the sake of this exercise, we plan to design a simpler version of Instagram, where a user can share photos and can also follow other users. The ‘News Feed’ for each user will consist of top photos of all the people the user follows. 
Functional Requirements:
1. Users should be able to upload/download/view photos. 
2. Users can perform searches for other users based on photo titles, tags, ratings and so on.
3. Users can follow other users. 
4. The system should be able to generate and display a user’s News Feed consisting of top  photos from all the people the user follows. 
5. The system should allow adding tags to photos. 
6. The system should allow searching photos on tags, ratings, dates or publishing users.
7. The system should allow commenting on photos. 
8. The system should allow tagging users to photos. 
9. Our services should be able to record stats of photos, e.g., likes/dislikes, total number of  views, etc. 
10. System should be able to list the most popular photos and users. 
Non-functional Requirements:
1. Our service needs to be highly available. 
2. Consistency can take a hit (in the interest of availability), if a user doesn’t see a photo for a while; it should be fine. 
3. The system should be highly reliable; any uploaded photo or video should never be lost.


## ER Diagram
![CS 179G ER Diagram](https://github.com/mychiang13/Impostergram-DB-Project/blob/main/images/CS%20179G%20ER%20Diagram.png)