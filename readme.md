<h1 align="center">Taskify</h1>
<h2 align='center'>Task Manager</h2>
<br>

This project is a simple task management web application which is based on CRUD functionality. To build this app I used HTML, CSS, Python, Bootstrap, Flask and RDBMS. The app is aiming to help a team to manage their tasks and meetings. I wanted to find a solution for a teams to collaborate more effectively and achieve better results.


[View the live project here.]()

<h2 align="center"><img src=""></h2>

## User Experience (UX/UI)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want users to be able to understand main goal of the website. 
        2. As a First Time Visitor, I want users to be able to navigate to the different sections of the website to understand better what the website offers and how it can help them.<br>
    
    <img src="/static/images/screenshots/mp.png"><br>

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want users to Create, Update, Delete their Tasks.
        2. As a Returning Visitor, I want users to Create, Update, Delete their Meetings.
        3. As a Returning Visitor, I want users to be able to locate and see what they created with ease.<br>
   
    <img src="/static/images/screenshots/task_f.png"><br>

    <img src="/static/images/screenshots/meeting_f.png"><br>

    <img src="/static/images/screenshots/meetings_p.png"><br>

    <img src="/static/images/screenshots/task_p.png"><br>


    -   #### Frequent User Goals
        1. As a Frequent User, I want users to rely on the website therefore it must run smoothly without any interferences and glitches.<br>


# Web pages
## Home page(base.html)
The Home page is the landing page which introduces the website to the visitor and introduces the services of the company with links to other pages.
## Tasks/Meetings pages(tasks/meetings.html)
These web pages allows you to see and manipulate your records.
## Add/Edit pages(add_task/add_meeting/edit/edit_tasks.html)
These web pages are the forms which allows you to create and update your records. 


# Wireframes
### Desktop view:<br>
![Desktop Wireframe](/static/images/wireframes/taskify_pc.png)<br><br>

### Tablet view:<br>
![Tablet Wireframe](/static/images/wireframes/taskify_tablet.png)<br><br>

### Mobile View:<br>
![Mobile wireframe](/static/images/wireframes/taskify_phone.png)<br>
<br>

# Technologies and libraries used 
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
-   [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
-   [Git](https://git-scm.com/) - Git was used for version control by utilizing the terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) - GitHub is used to store the projects code after being pushed from Git.
-   [Balsamiq:](https://balsamiq.com/)
-   [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) - I decided to use RDBMS for this project as its:
-   RDBMS is based on rows and columns (table). So it is easier to understand RDBMS work.
-   RDBMS supports more than one user.
-   As it is advanced it can easily handle huge amounts of data.
-   Security is pretty good for RDBMS.


# Testing
## Testing web page links
|Test Case| Test|Expected Outcome|Actual Outcome|Comment|
| ------ | ------ |------ |------ |------ |
|1| Main page links  functional test for all pages |  launch needed page        |All links launched Main page|n/a|
|2| Tasks/Meetings  links functional test for all pages | launch needed pages  |all links launched Quiz page|n/a|
|3| Tasks/Meetings forms links funtional test for all pages  | launch neded pages  |All links launched |n/a|
|4| Update forms links functional tests for all pages | launch HighScores page          |All links launched correctly|n/a|

## Browser support testing
The following web browsers were used to test the display of the website including the functionality of the contact us form:
###### Edge
###### Chrome
###### Opera
###### Safari


## Responsive Test 
-   The App has been made to be responsive on varying sized screens.
-   The App will resize from the screen of a mobile phone all the way to a full desktop display.
-   Its was achieved to make the service more accecible.
-   Even though it has bee created mainly for desktop it can still be used on a mobile by a user if required.

## Language validation
The W3C Markup Validator, W3C CSS Validator and JShint Services were used to validate every page of the project to ensure there were no syntax errors in the project.<br>

 <img src=""><br>

-   [W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Frustam-aliyev889.github.io%2FQuiz%2Findex.html) - Results - No Errors or Warnings


<img src="/static/images/screenshots/css-test.png"><br>

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator) - Results No Errors<br>

-   [Lighthouse reports]:

| Pages  |  Report |
|---|---|
| Home  | <img src="/static/images/screenshots/base.lh.png">  |
| Tasks | <img src="/static/images/screenshots/tasks.lh.png">  |
| Meetings  |  <img src="/static/images/screenshots/meetings.lh.png">  |
| Add Task | <img src="/static/images/screenshots/tasks-f.lh.png">  |
| Add Meeting  | <img src="/static/images/screenshots/meeting-f.lh.png">  |

# Bugs
## To test my code I isolated some parts of it with comments to find out what is might be the problem. I ran into a couple of problems however isolation helped me to figure it out. I also used additional software to see how my functions behave here are some examples:<br>

<br>| Functions  |  Report |
|---|---|
| Tasks  | <img src="/static/images/screenshots/task-funk.png"><br>
 <img src="/static/images/screenshots/task-func1.png"> |
| Meetings | <img src="/static/images/screenshots/metting-func.png.png"><br>
<img src="/static/images/screenshots/meeting-func1.png"> |
| Update Meetings  |  <img src="/static/images/screenshots/update-meeting-func.png">  |
| Get Task | <img src="/static/images/screenshots/get-task-func.png">  |
| Delete Task  | <img src="/static/images/screenshots/delete-task-func.png">  |
| New Task  | <img src="/static/images/screenshots/new-task-func.png">  |

|Bug|Comment|
| ------ | ------ |
|Could not connect to database|This was corrected|
|Could not retrieve data from batabase |Code was included to correct it. Subsequent tests verified it works|
|Update function did not work|This was fixed and tested to ensure it works|
|Delete function did not work|This was fixed and tested to ensure it works|
|I did not understand how to Jinja template works at first so information was not displayed properly|This was fixed and tested to ensure it works|<br>


## Deployment

### Where can it be found on GitHub? 
The GitHub link for the project is - https://github.com/Rustam-Aliyev889/taskify-2nd-att.git
