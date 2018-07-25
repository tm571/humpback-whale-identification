# Humpback Whale Identification Kaggle competition

## Deployment on Heroku

- Download this repository.
- Register on Heroku (https://www.heroku.com).
- Download and install Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
- Open terminal, navigate to where you have downloaded the repository and type the command `git init` to create a git repository.
- Commit the code to the repository by running `git add .`, then `git commit -m "Initial commit"`
- Create heroku app by running `heroku create`.
- We need an api key to allow script to download kaggle data. Go to your kaggle account page and select 'Create API token'. View the downloaded file.
    Copy the value of the key variable then run `heroku config:set KAGGLE_API_KEY=<key>` where <key> is the value you just copied.
- In script.sh, change "username"="tommosley" to your kaggle username.
- Push the code to heroku by running `git push heroku master`.
- The script will deploy the code to a heroku virtual machine, download the kaggle data and run the script load_training_data.py
- To see the output, initiate a virtual machine by running `heroku ps:scale worker=1` and view the logs by `heroku logs --tail`.

The work is done by the code in the Procfile. It first runs `script.sh` to load the kaggle data then when this is done, it runs the
load_training_data.py script on the kaggle data it has just downloaded.

To run your own scripts, add them to the repo, commit your changes (`git add .` then `git commit -m "<your message>"`) then push the changes to heroku
(`git push heroku master`).

When you have finished, run `heroku ps:scale worker=1` to stop the virtual machine from running.
