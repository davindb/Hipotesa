<!--
*** WELCOME TO HIPOTESA REST API DOCUMENTATIONS
*** Thanks for checking out the Hipotesa REST API Documentations Readme. If you have a suggestion
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

  <h3 align="center">Hipotesa Open APIs Documentation</h3>

  <p align="center">
    An AI based healthcare system aims to help patients to detect their disease at an early stage to be able to identify the treatment plan early on and help them secure a good way to live.
    <br />
    <a href="https://github.com/davindb/Hipotesa#readme"><strong>Go to the project »</strong></a>
    <br />
    <br />
    <a href="https://github.com/davindb/Hipotesa">View Demo</a>
    ·
    <a href="http://www.hipotesa.tech">Our Website</a>
    ·
    <a href="https://github.com/davindb/Hipotesa/tree/main/Hipotesa%20APIs%20Documentation#contributing">Contribute</a> 
    ·
    <a href="https://github.com/davindb/Hipotesa/issues">Report Bug</a>
    
  </p>
</p>

This is the complete guidance on how our APIs can be implemented to your machine. Feel free to ask a help to us and if you want to contribute to this project just click the contribute button. Let us know what you have created !!!

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#open-endpoints">Open Endpoints</a>
    </li>
    <li>
      <a href="#disease-prediction">Disease Prediction</a>
    </li>
    <li><a href="#diseases-list">Diseases List</a></li>
    <li><a href="#symptoms-list">Symptoms List</a></li>
    <li><a href="#preform-queries-on-request">Perform Queries on Request</a></li>
    <li><a href="#project-repositories">Project Repositories</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#copyright">Copyright</a></li>

  </ol>
</details>

## Open Endpoints

Our APIs are open endpoints and require **no authentication**

Preadict a disease:

- [Predict](#disease-prediction) : `POST /api/predict/`

Read data:

- [Diseases](#diseases-list) : `GET /api/diseases/`
- [Symptoms](#symptoms-list) : `GET /api/symptoms/`

Read data with specific queries:

- [Diseases](#diseases-list-with-queries) : `POST /api/diseases/`
- [Symptoms](#symptoms-list-with-queries) : `POST /api/symptoms/`

## Disease Prediction

Used to predict a disease based on the symptoms from user inputs.

**URL** : `/api/predict/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
  "symptom_1": "[valid symptom <str>]",
  "symptom_2": "[valid symptom <str>]",
  "symptom_3": "[valid symptom <str>]"
}
```

**Data example**

```json
{
  "symptom_1": "itching",
  "symptom_2": "nodal_skin_eruptions",
  "symptom_3": "skin_rash"
}
```

We recommend you to put at least three key value pairs for getting the most accurate results.

Valid symptom means the symptom that is existed in our database. You can see what symptoms are existed in our database by following the instruction on calling a [Symptoms List](#symptoms-list) request.

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "Description": "In humans, fungal infections occur when an invading fungus takes over an area of the body and is too much for the immune system to handle. Fungi can live in the air, soil, water, and plants. There are also some fungi that live naturally in the human body. Like many microbes, there are helpful fungi and harmful fungi.",
  "Disease": "Fungal infection",
  "Precaution": [
    "bath twice",
    "use detol or neem in bathing water",
    "keep infected area dry",
    "use clean cloths"
  ],
  "Probability": 96.66658639907837
}
```

### Error Response

**Condition** : If type of the value is not a string.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
  "ErrorMessage": "TypeError: <value> is expected to be string but got <class 'int'>."
}
```

## Diseases List

Used to get the list of diseases.

**URL** : `/api/diseases/`

**Method** : `GET`

**Auth required** : NO

### Success Response

**Code** : `200 OK`

**Content example**

```json
[
    {
        "Description": "In humans, fungal infections occur when an invading fungus takes over an area of the body and is too much for the immune system to handle. Fungi can live in the air, soil, water, and plants. There are also some fungi that live naturally in the human body. Like many microbes, there are helpful fungi and harmful fungi.",
        "Disease": "Fungal infection",
        "Id": 0,
        "Precautions": [
            "bath twice",
            "use detol or neem in bathing water",
            "keep infected area dry",
            "use clean cloths"
        ]
    },
    ...
]
```

## Symptoms List

Used to get the list of symptoms.

**URL** : `/api/symptoms/`

**Method** : `GET`

**Auth required** : NO

### Success Response

**Code** : `200 OK`

**Content example**

```json
[
    {
        "Id": 0,
        "Symptom": "abdominal_pain"
    },
    {
        "Id": 1,
        "Symptom": "abnormal_menstruation"
    },
    ...
]
```

## Perform Queries on Request

These are the available properties to perform queries.

| Property     | Type            | Description                                                   |
| :----------- | :-------------- | :------------------------------------------------------------ |
| `where`      | key-value pairs | Specify which field you want to retrieve from the collection. |
| `order`      | string          | Sort order for your data based on the field you specified.    |
| `limit`      | integer         | Limit the number of object you want to retrieve.              |
| `descending` | boolean         | Sort the retrieved data in descending order.                  |

### Valid field for Diseases Collection

- Id <value: int>
- Disease <value: str>
- Description <value: str>
- Precautions <value: array>

### Valid field for Symptoms Collection

- Id <value: int>
- Symptom <value: str>

## Diseases List with Specific Queries

Used to get the list of diseases.

**URL** : `/api/diseases/`

**Method** : `POST`

**Auth required** : NO

### Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "Description": "Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus. The virus is one of several types of hepatitis viruses that cause inflammation and affect your liver's ability to function.",
    "Disease": "hepatitis A",
    "Id": 19,
    "Precautions": [
      "Consult nearest hospital",
      "wash hands through",
      "avoid fatty spicy food",
      "medication"
    ]
  }
]
```

## Symptoms List

Used to get the list of symptoms.

**URL** : `/api/symptoms/`

**Method** : `POST`

**Auth required** : NO

### Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "Id": 25,
    "Symptom": "continuous_sneezing"
  }
]
```

One of our open API features is that you are able to perform queries to get a specific data that you want.

To specify which field you want to retrieve, you can perform a query parameter using `where`.

**Data constraints**

```json
{
  "where": {
    "[valid field]": "[valid value <str> or <int>]"
  }
}
```

**Data example**

```json
{
  "where": {
    "Id": 3
  }
}
```

Based on the example, I will retrieve the data which the **'Id'** is **3**.

You can also perform an `OR` condition using array as a type of the value.

**Data example**

```json
{
  "where": {
    "Disease": ["Fungal infection", "Allergy", "AIDS"]
  }
}
```

Then, you will retrieve any data that satisfied the values.

To sort your data based on the field you specified, you can use `order`.

**Data constraints**

```json
{
  "order": "[valid field <str>]"
}
```

**Data example**

```json
{
  "order": "Disease"
}
```

Based on the example, I will retrieve the data which will be sorted based on the **'Disease'** in an ascending way.

If you want to sorted in a descending format, you can add `descending` field and set it to true (default is false).

**Data example**

```json
{
  "order": "Disease",
  "descending": true
}
```

`limit` is like its name which is to limit the number of object you want to retrieve.

**Data constraints**

```json
{
  "limit": "[valid number <int>]"
}
```

**Data example**

```json
{
  "limit": 3
}
```

You can also combine all the parameter like the given example below.

```json
{
  "where": {
    "Disease": ["Fungal infection", "Allergy", "AIDS"]
  },
  "order": "Id",
  "descending": true,
  "limit": 2
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "Description": "Acquired immunodeficiency syndrome (AIDS) is a chronic, potentially life-threatening condition caused by the human immunodeficiency virus (HIV). By damaging your immune system, HIV interferes with your body's ability to fight infection and disease.",
    "Disease": "AIDS",
    "Id": 6,
    "Precautions": [
      "avoid open cuts",
      "wear ppe if possible",
      "consult doctor",
      "follow up"
    ]
  },
  {
    "Description": "An allergy is an immune system response to a foreign substance that's not typically harmful to your body.They can include certain foods, pollen, or pet dander. Your immune system's job is to keep you healthy by fighting harmful pathogens.",
    "Disease": "Allergy",
    "Id": 1,
    "Precautions": [
      "apply calamine",
      "cover area with bandage",
      "use ice to compress itching"
    ]
  }
]
```

#### Error Response

**Condition** : If type of the key (field) is not valid.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
  "ErrorMessage": "ValueError: <key> is not a valid key."
}
```

### Error Response

**Condition** : If type of the value is not valid.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
  "ErrorMessage": "TypeError: <value> expected to be a string."
}
```

## Project Repositories

Check our project repositories to know more about Hipotesa.

- [Hipotesa Project](https://github.com/davindb/Hipotesa)
- [Hipotesa Application]()
- [Hipotesa Algorithm](https://github.com/davindb/Hipotesa/tree/main/HipotesaAlgorithm#readme)
- [Hipotesa Rest API & Cloud Management](https://github.com/davindb/Hipotesa/tree/main/HipotesaCloudManagement/#readme)

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

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
