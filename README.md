# Heart Attack Prediction <img src="https://user-images.githubusercontent.com/66221394/130499684-50155db9-b5d5-419e-a627-bd70f176e7f1.png" width="50" height="50">
## Topics
- [Demo](#Demo)
- [Overview](#Overview)
- [Motivation](#Motivation)
- [Technical Aspect](#Technical-Aspect)
- [Installation](#Installation)
- [Create Flask App](#Create-Flask-App)
- [Deployement on Heroku](#Deployement-on-Heroku)
- [Bug / Feature Request](#Bug-/-Feature-Request)
- [Technologies Used](#Technologies-Used)
- [Team](#Team)
- [License](#License)
- [Credits](#Credits)

## Demo
Link: https://predictheartattacks.herokuapp.com/

[<img src="https://user-images.githubusercontent.com/66221394/130486683-9cfb8b82-79de-44d7-be66-c7a2eb156331.png">](https://predictheartattacks.herokuapp.com/)


## Overview
This is a classification Flask app which predicts whether a person is more prone to heart attack or not based on the individual's heart condition. 
The data is taken from [Kaggle-Heart Attack Prediction](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) which contains
various heart features. Performed EDA and Feature Selection. Best Model is selected after comparing different model's parformance and hypermarater tuning.
The Flask app is developed using python file and then deployed using Heroku.

## Motivation
While looking various datasets on Kaggle, I came across this classification dataset which I think is one of the perfect dataset to learn lots of stuff while 
preparaing a machine learning model as well as is a good step to start deploying your model and implementing end to end.

## Technical Aspect
This project is divided into two part:
1. Training a machine learning model using Sklearn.

2. Building and hosting a Flask web app on Heroku.
- A user can enter input fields related to heart.
- The Input fields are basically the model features.
- After entering the features and pressing 'Predict' button, the predictions are displayed saying if the person has more/ less chances of Heart Attack with 
probability of it in percentage.

## Installation
The Code is written in Python 3.6. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). 
If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 
To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/)
the repository:
`pip install -r requirements.txt`

## Create-Flask-App
- First install Flask on your local system. If you haven't already activated your programming environment, first activate it using
`$ source env/bin/activate`

- To install Flask, run the following command:
`$ pip install flask`
After installing create your base application. You can also refer to this amazing guide on [How To Make a Web Application Using Flask in Python 3](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)

## Deployement on Heroku
Before deployement, make sure you've pushed your code to github repository. Create your account on [Heroku](https://dashboard.heroku.com/apps).
Follow [this](https://dev.to/lordofdexterity/deploying-flask-app-on-heroku-using-github-50nh) step by step guide on how to deploy your Flask app on Heroku.
  


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), 
kindly open an issue [here](https://github.com/daniyal214/End-to-End-ML-Projects/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/daniyal214/End-to-End-ML-Projects/issues/new). 
Please include sample queries and their corresponding results.

## Technologies Used
![python](https://camo.githubusercontent.com/3cdf9577401a2c7dceac655bbd37fb2f3ee273a457bf1f2169c602fb80ca56f8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)
<img src="https://user-images.githubusercontent.com/66221394/130487933-f4616292-15a6-4d0d-8463-c81fcfe44f64.png" width="180" height="100">
<img src="https://user-images.githubusercontent.com/66221394/130488015-d156d9ba-2b74-4c72-956c-ef5da655c98b.png" width="280" height="100">
<img src="https://user-images.githubusercontent.com/66221394/130488547-ef7a0c7c-ecd9-4c07-8485-d3ab5cce7f3d.png" width="200" height="100">
<img src="https://user-images.githubusercontent.com/66221394/130488284-8f8f1f3d-7015-44dd-865a-566095697572.png" width="250" height="100">

## Team
<img src="https://user-images.githubusercontent.com/66221394/130490754-e043534a-9e0e-44c1-aaf5-fc4453a2b1f9.JPG" width="150" height="210">


## License
Copyright [2021] [Muhammad Daniyal]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

## Credits
Main credits goes to [Kaggle](https://www.kaggle.com/) platform for [this](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)
amazing dataset.
It saved my enormous amount of time of collecting the data. 
A huge shout-out to the person who has shared it [Rashik Rahman](https://www.kaggle.com/rashikrahmanpritom).




