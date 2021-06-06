gcloud app deploy -> to deploy
gcloud app logs tail -s default -> to monitoring app engine

to start service:

1. go to app engine.
2. select version.
3. checklist top version after that click start.
4. wait a minutes...
5. enjoy the Service :)

to Deploy service to App Engine:

1. open cloud shell.
2. git clone apps (app.yaml, main.py, assets.py, requirements.txt) please take all file in one folder.
3. go to directory of apps (cd ....).
4. in apps folder run this function "gcloud app deploy".
5. wait a minutes...
6. service deploy at app engine :)
