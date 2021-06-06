<br />
<p align="center">
  <a href="#">
    <img src="Assets\hipotesa_logo.jpeg" alt="hipotesaLogo" height="500">
  </a>
  <br>

  <p align="center">
    <img src="https://img.shields.io/badge/ID-B21--CAP0170-00ACEE">
  </p>

  <h1 align="center">Symptoms Based Disease Prediction
  </h1>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#team-members">Team Members</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#android-app">Android App</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

There are a lot of diseases that you need to detect at an early stage to be able to identify
the treatment plan early on and help the patient secure a good way to live. An early detection of
disease and a precise diagnosis allows for quicker action, saving precious time, and to prevent
complications and rapid worsening. Health practitioners have conducted surveys and collected
data on patient information, their disease, and symptoms that allow them to distinguish the
patient's disease with common symptoms. Therefore, the data set can be used to train the
model that predicts the disease based on the symptoms.

In this project we create an Android Native Mobile Application with the resources are supported by 
Google Cloud Platform and will involves user inputs which will be the data containing list of symptoms. 
And then, our system will perform a Machine Learning model that involves the data (list of symptoms). 
The final result is to generate the predicted disease following with its treatments.

### Built With

* [Tensorflow](https://www.tensorflow.org/)
* [Google Cloud Platform](https://cloud.google.com/)
* [Gunicorn](https://gunicorn.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)

## Team Members

|         Member                 | Student ID |                Project Role                |                                                  Contacts                                                    |
| :----------------------------: | :--------: | :----------------------------------------: | :----------------------------------------------------------------------------------------------------------: |
|  Davin Darmalaksana Bhagaspati |  M0111153  | Project Manager, Machine Learning Engineer |  [![davin-linkedin][linkedin-shield]][davin-linkedin-url][![davin-github][github-shield]][davin-github-url]  |
|     Ihsan Nafilah Ramdhani     |  M0111152  |         Machine Learning Engineer          |  [![ihsan-linkedin][linkedin-shield]][ihsan-linkedin-url][![ihsan-github][github-shield]][ihsan-github-url]  |
|  Agus Cahya Ananda Yoga Putra  |  C0121258  |          Cloud Platform Engineer           |    [![agus-linkedin][linkedin-shield]][agus-linkedin-url][![agus-github][github-shield]][agus-github-url]    |
|       Fadia Fatta Dylla        |  C0121262  |          Cloud Platform Engineer           |  [![fadia-linkedin][linkedin-shield]][fadia-linkedin-url][![fadia-github][github-shield]][fadia-github-url]  |
|   Ravedya Aufa Amaranggana W.  |  A0111155  |              Mobile Developer              |  [![raved-linkedin][linkedin-shield]][raved-linkedin-url][![raved-github][github-shield]][raved-github-url]  |



<!-- GETTING STARTED -->
## Getting Started

Setting up the project on your linux machine (for windows user can use Windows Subsystem Linux (WSL))

### Prerequisites

This project require several resources on your development machine: 
* [Python 3.7++](https://www.python.org/downloads/) (we use python 3.9.0)
* [Tensorflow 2.x](https://www.tensorflow.org/) 

### Installation

1. Clone the repository
   ```sh
   $ git clone https://github.com/davindb/Symptoms-Based-Disease-Prediction.git
   #change directory to the repository folder
   $ cd Symptoms-Based-Disease-Prediction
2. Install required packages 
   ```sh
   $ pip install -r requirements.txt
   ```
3. You can run this project on your local machine using jupyter notebook
   ```sh
   $ jupyter-notebook
   ``` 





<!-- USAGE EXAMPLES -->
## Android App

<p align="center">
  <img src="Assets\input_data.PNG" height="500"></img>&nbsp; &nbsp;<img src="Assets\result.PNG" height="500">
</p>




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- LinkedIn Link -->

[linkedin-shield]: https://img.shields.io/badge/LinkedIn--blue?style=social&logo=Linkedin
[davin-linkedin-url]: https://www.linkedin.com/in/davindb/
[ihsan-linkedin-url]: https://www.linkedin.com/in/ihsanramdhani/
[agus-linkedin-url]: https://www.linkedin.com/in/aguscahya/
[fadia-linkedin-url]: https://www.linkedin.com/in/fadia-fatta-dylla-326998113/
[raved-linkedin-url]: https://www.linkedin.com/in/ravedya/

<!-- Github Link -->

[github-shield]: https://img.shields.io/badge/GitHub--blue?style=social&logo=Github
[davin-github-url]: https://github.com/davindb
[ihsan-github-url]: https://github.com/ihsanramdhani
[agus-github-url]: https://github.com/Guscah
[fadia-github-url]: https://github.com/fadiafattadyllaaa
[raved-github-url]: https://github.com/ravedya