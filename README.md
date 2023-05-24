# Saving The Night Below

# Intro

I was contacted by the client to assist with transferring the contents of a website they had created. The site they had been hosting content on was being deprecated and the client was given a JSON file with the various articles he had written on the site. The client only needed the contents to continue a game he was playing with his friends and was not intending for the content to be consumed by outside viewers. Client also did not want to spend too much time on the project, he planned to deprecate the website eventually so anything more than a few hours the client viewed as not worth the time. Client also mentioned that he planned to host more content later so I aimed to provide a template that he could use in the future

# Scope of project

A review of the data made me confident that the data could easily be set up in a flask app and I was able to find a few options for free hosting. Flask met the clients requirements for being able to host for free and had the flexibility to navigate the site in a way that the client liked. Due to the short timeframe desired, the website was designed to be functional without much attention to aesthetics.

# Overview

Initially, the plan was to use the JSON file to populate a database and then keep the database available to intake new content. Unfortunately, the JSON file had several issues with escape characters due to the formatting used on the previously hosted website and efforts to load the database into the hosted application caused errors. The plan shifted to creating separate html pages for each article entry and then creating routes in flask to render the template of each.

## ETL

As mentioned above, the first step was to extract the articles from the JSON file into a pandas dataframe keeping only the relevant content and replacing links so that they pointed to the new website. The resulting data frame was saved to an SQLITE database. Next, the data frame was used to create a Python file with the flask app routing, looping through each entry to open the file, load the data for that entry in the app route and then save the file. Then, each row was iterated through to create the html file and appended content for each article. The file name matched the output for the Python file so that template rendered correctly in flask. CSS and JS were used to create navbars and sidenav bars for navigation and a base.html file was called in so that page could be updated easily in the future.

## Hosting

The file was uploaded with the Python app.py file, html files in a template folder and CSS, JS and image files in a static files folder following Flasks format. It was uploaded into github and then pulled into pythonanywhere. Using github made it much easier to upload due to the high number of articles and the lack of a bulk uploader in pythonanywhere. 

# Outcome

Client was pleased with the end result and that it did not take much time to complete. Client continues to work through his next project and is interested in seeing more about Flask to solve some other challenges he expects to have.
