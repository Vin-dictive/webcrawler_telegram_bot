# webcrawler_telegram_bot
Its heroku deployable app. 
It checks a specified webpage for updates on it and stores them on MONGODB. 
So when it encounters a new page it sends a message to the subscriber on the Telegram bot and updates the DB with the new webpage
available on the page.

Procfile defines which commands are gonna start the app
Requirement.txt defines the dependencies
__init__.py though empty is required for heroku

You can check out the jupyter file to understand the flow of the program
