# Village-Stakeholder
Made for CS491 for B The Cause for their village stakeholder project. The techstack is Vue.js + TailwindCSS, Django, and PostgreSQL. 

# How to run with Docker
Install docker and the devcontainer extension in VSCode. Everything should update correctly and having it running.
So small important details, everything for frontend is running in: [Vue](http://localhost:5173). Django [Django](http://localhost:8000). Add the /admin to see the current backend as a admin. Finally, if you get some weird error about something in the Database not existing make sure to migrate it first. I highly recommend this way of development since it makes everything much easier since you don't have to install PostgreSQL, NPM or Python manually. Contact me if you never used Docker.

# Linux/Mac users
I have no idea if this will work with Mac users but it should work very well with Linux.

# Windows
Use WSL2 Ubuntu with a docker install, make sure you have the Docker WSL2 setting turned on. Then install the devcontainers and run the with rebuild and reopen. 