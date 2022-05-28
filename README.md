Orange_Cube
# Project Title

Orange_Cube which is a web development project that is designed and developed by Shashank Singh for Microsoft Engage through which movie is recommended on basis of search history and it also recommended 6 related movie for search movie and two or more people can create room together and enjoy movie and much more.


#To start the app
- Run data.py file(python3)
- npm install
- node index


## Table of Contents:

- Features
- Technology Stack
- Workflow $ Database
- Future Plans
- Limitations
- Troubleshooting
- Images
- Credits

# Features:
1. **Search Movie** : There is option to Search movie in this website which return 6 related movie including searched one
2. **Search Based Recommendation** : It recommend related moive to the login user according to his/her search history
4. **Populatiy based Action Movie Recommendation** : For any user to website can check popular Action moive
4. **Populatiy based Thriller Movie Recommendation** : For any user to website can check popular Thriller moive
4. **Populatiy based Adventure Movie Recommendation** : For any user to website can check popular Adventure moive
5. **Create Meets** : User can create room under which two or more Member come together and watch movie, discuss about something
5. **Video Conversation** : 2+ people can have a video conversation in this website about moive or something
6. **Turn off / on Camera** : Users can choose to show or hide themselves from others during a call and only show initials of their name
6. **Mute / Unmute Audio** : Users can choose to speak or not speak and avoid causing chaos in a call
7. **Mute All Member** : Users can mute everyone in the call, excluding themselves while talking so to avoid interruptions
8. **Name on Hovering** : While hovering on a video box one can see the Member name
20. **Chat** : Users can chat in the call to communicate when not able to speak
11. **Sign Up / Log In** : If user watch moives regularly and hosts regular room and want to store the chats, list of created room and quickly remind people of the room then they can log in
52. **Reminders** : Server automatically remind users about their room at the time of their room
22. **Contact Us** : User can contact us and give feedback that will help me to better my project
23. **Help Page** : A help page is provided where every question regarding the use of the website is provided
25. **Create Groups / Join Groups** : User can create many groups, each with a key to keep the group private and secure from unwanted people
24. **Group Details in Group Dashboard** : In the dashboard, one can see the details such as key and members so that if one forgets the key, they can find it there and also know who all are a part of the group
20. **Sound Alerts** : This is provided so that the people in the call become aware of the entering of a new person


# Technology Stack:
1. **Node.js** - Back End
2. **Python** - Recommendation system
2. **MongoDB (Mongoose)** - Database
3. **Bcrypt** - Hash Passwords
4. **Express-session** - To manage sessions
5. **EJS** - Templating
6. **CSS** - Designing (also used Bootstrap's framework and AOS' library to design)
5. **JavaScript** - For interactivity (also used jQuery)
5. **Socket.io** - For real time communication
8. **Peer.js** - Simplifies WebRTC's use
8. **Nodemailer** - Sending Reminder Mails
8. **Node-cron** - Scheduling Reminders
9. **Pickle** - For creating Model file




# Problem Faced
- **cold-start problelm** : Recommendation for new user and new movies is Problem for me. So for new user i recommend most popular movie and new movie are recommend to user according to genres and keyword
- **integration of python and Nodejs** : using "require("child_process").spawn" i get rid of this



# **Future**
**Recommend similar choice user** :- Recommendation of user those who watch moive of similar genres and keyword.
- i plan to add genres and keyword of all the searched movie one one user and do similarly for others.
- convert whole thing in vector using countVectorizer
- store distance of one user with all other user in matrix using cosine_similarity
- Then recommend most similar user


## Troubleshooting:
- If you are not able to see the other user then try checking your connection and try using mobile data
- If you are not able to connect with the other user - go to inspect -> settings -> untick "Enable Java Script Source Maps"


## Credits:
- Mentors - Mr. Pramit mallic
- Developer - [Shashank singh](https://github.com/singhshashank25)


![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
