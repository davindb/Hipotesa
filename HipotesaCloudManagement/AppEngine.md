# 💻 Deploy to App Engine Flexible

You can apply this application to the Google Cloud Platform App Engine. Following are the steps for running this application in a Flexible App Engine environment.

## 📌Set up Google Cloud Platform

**1. Open a Google Cloud Platform account.**

If you're new to Google Cloud, you can [create an account](https://console.cloud.google.com/freetrial) and new customers also get $300 in free credits to run, test, and deploy workloads.

**2. In the Google Cloud Console, on the project selector page, select or create a Google Cloud projec**

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard) to select a project.

**3. Make sure that billing is enabled for your Cloud project**

[learn how to confirm that billing is enabled for your project](https://cloud.google.com/billing/docs/how-to/modify-project)

**4. [Install and initialize the Cloud SDK](https://cloud.google.com/sdk/docs/install)**

Follow the installation instructions according to your operating system used.


## 📌Downloading and running the app

**1. Cloning the repository to local computer or when you want use console of GCP, you can use cloud shell**

```bash
git clone https://github.com/Guscah/HipotesaRestAPI.git
```

**2. Open directory**

```bash
cd HipotesaRestAPI
```

**3. Open app.yaml**

```bash
nano app.yaml
```
customize your configuration App Engine due your system requirement.

**4. Execute App Engine**

```bash
gcloud app deploy
```

**5. See Log**
Monitor your log to ensure your system working properly.

```bash
gcloud app logs tail -s default
```

