<!--
*** WELCOME TO HIPOTESA REST API AND CLOUD MANAGEMENT README
*** Thanks for checking out the Hipotesa REST API and Cloud Management Readme. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- COLOR CODE: 082c4e -->

<p align="center">
    <img src="https://img.shields.io/badge/ID-B21--CAP0170-082c4e">
</p>

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="http://www.hipotesa.tech/">
    <img src="images/hipotesa.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Hipotesa REST API and Cloud Management</h3>

  <p align="center">
    An AI based healthcare system aims to help patients to detect their disease at an early stage to be able to identify the treatment plan early on and help them secure a good way to live.
    <br />
    <a href="https://github.com/davindb/Hipotesa#readme"><strong>Go to the project »</strong></a>
    <br />
    <br />
    <a href="https://github.com/davindb/Hipotesa/">View Demo</a>
    ·
    <a href="http://www.hipotesa.tech/">Our Website</a>
    ·
    <a href="https://github.com/Guscah/HipotesaRestAPI/#contributing">Contribute</a>
    ·
    <a href="https://github.com/Guscah/HipotesaRestAPI/issues">Report Bug</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#resources">Resources</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#deployment">Deployment</a></li>
          <li><a href="#open-apis">Open APIs</a></li>
         <li><a href="#other-repositories">Other Repositories</a></li>
      </ul>
    </li>
    <li><a href="#our-cloud-computing-engineer-team">Our Cloud Computing Engineer Team</a></li>
    <li><a href="#contributing">Contributing</a></li>
      <li><a href="#license">License</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#copyright">Copyright</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

There are a lot of diseases that you need to detect at an early stage to be able to identify the treatment plan early on and help the patient secure a good way to live. An early detection of disease and a precise diagnosis allows for quicker action, saving precious time, and to prevent complications and rapid worsening. Health practitioners have conducted surveys and collected data on patient information, their disease, and symptoms that allow them to distinguish the patient's disease with common symptoms. Therefore, the data set can be used to train the model that can predict the disease based on the symptoms.

In this project we create an **Android Native Mobile Application** with the resources are supported by **Google Cloud Platform**. We imlemented a **Machine Learning Model** that requires data containing a list of symptoms. Our system then will find out what disease the patients have and what treatments they should take.

<!-- RESOURCES -->

### Resources

- [Android Studio](https://developer.android.com/studio)
- [Tensorflow](https://www.tensorflow.org/)
- [Google Cloud Platform](https://cloud.google.com/)
- [Google App Engine](https://cloud.google.com/appengine)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Gunicorn](https://gunicorn.org/)

<!-- GETTING STARTED -->

## Getting Started

This is an overview of Hipotesa Cloud Architecture, what the prequisites are, how to download and use the app, open APIs guidance for developers, and more.

<p align="center">
    <img src="images/Cloud%20Configuration.png">
</p>

### Prerequisites

- Laptop / PC
- Internet Connection
- Python 3.9

### Installation

To deploy an application on Google Cloud Platform, you don't need to install any software, just provide app.yaml, main.py and requirements.txt files.

### Deployment

For the REST API deployment on the Google Cloud Platform to be able to be accessed by android apps, we choose App Engine Service as a platform to deploy our REST API.

We use App Engine [Flexible Environment](https://github.com/Guscah/HipotesaRestAPI/AppEngine.md) as our deployment service (Main Option).

<b>Note:</b> You can't do the deployment using the App Engine Standard if the number of files are more than 10K and it will need more time for like more than 10 minutes to deploy.

### Open APIs

Please refer to the _Hipotesa Open APIs Documentation_ below for more information and guidance.

- [Open APIs Documentation](https://github.com/davindb/HipotesaDeveloper/#readme)

### Other Repositories

Check our other repositories to know more about Hipotesa.

- [Hipotesa Project](https://github.com/davindb/Hipotesa/#readme)
- [Hipotesa Application]()
- [Hipotesa Algorithm](https://github.com/davindb/HipotesaAlgorithm)

<!-- TEAM MEMBERS -->

## Our Cloud Computing Engineer Team

|            Member            | Student ID |       Project Role       |                                                  Contacts                                                  |
| :--------------------------: | :--------: | :----------------------: | :--------------------------------------------------------------------------------------------------------: |
| Agus Cahya Ananda Yoga Putra |  C0121258  | Cloud Computing Engineer |   [![agus-linkedin][linkedin-shield]][agus-linkedin-url][![agus-github][github-shield]][agus-github-url]   |
|      Fadia Fatta Dylla       |  C0121262  | Cloud Computing Engineer | [![fadia-linkedin][linkedin-shield]][fadia-linkedin-url][![fadia-github][github-shield]][fadia-github-url] |

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

We are very grateful to all of those with whom we have had the pleasure to work during this and other related projects especially [Bangkit Academy](https://grow.google/intl/id_id/bangkit/) who supported for doing this project. Each of the team members of this project has provided the team extensive personal and professional guidance about both scientific research and life in general especially in healthcare related fields.

<p align="center" style="padding-top: 5px">
  <a href="https://grow.google/intl/id_id/bangkit/">
    <img src="images/Bangkit.PNG" alt="Logo" width="50%" height="100%">
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="http://www.hipotesa.tech/">
    <img src="images/hipotesa.png" alt="Logo" width="22%" height="22%" >
  </a>
</p>

<!-- COPYRIGHT -->

## Copyright

Kreasi Anak Bangsa group © Copyright 2021 | All Rights Reserved.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- LINKED IN -->

[linkedin-shield]: https://img.shields.io/badge/LinkedIn--blue?style=social&logo=Linkedin
[davin-linkedin-url]: https://www.linkedin.com/in/davindb/
[ihsan-linkedin-url]: https://www.linkedin.com/in/ihsanramdhani/
[agus-linkedin-url]: https://www.linkedin.com/in/aguscahya/
[fadia-linkedin-url]: https://www.linkedin.com/in/fadia-fatta-dylla-326998113/
[raved-linkedin-url]: https://www.linkedin.com/in/ravedya/

<!-- GITHUB -->

[github-shield]: https://img.shields.io/badge/GitHub--blue?style=social&logo=Github
[davin-github-url]: https://github.com/davindb
[ihsan-github-url]: https://github.com/ihsanramdhani
[agus-github-url]: https://github.com/Guscah
[fadia-github-url]: https://github.com/fadiafattadyllaaa
[raved-github-url]: https://github.com/ravedya

<!-- OTHERS -->

[contributors-shield]: https://img.shields.io/github/contributors/davindb/HipotesaProject.svg?style=for-the-badge
[contributors-url]: https://github.com/davindb/HipotesaProject/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/davindb/HipotesaProject.svg?style=for-the-badge
[forks-url]: https://github.com/davindb/HipotesaProject/network/members
[stars-shield]: https://img.shields.io/github/stars/davindb/HipotesaProject.svg?style=for-the-badge
[stars-url]: https://github.com/davindb/HipotesaProject/stargazers
[issues-shield]: https://img.shields.io/github/issues/davindb/HipotesaProject.svg?style=for-the-badge
[issues-url]: https://github.com/davindb/HipotesaProject/issues
