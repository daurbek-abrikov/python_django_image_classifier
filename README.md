# python_django_image_classifier
Team: Daurbek Abrikov, Sanzhar Nakyp

Project: Image classifier

In this project, we will classify images using CNN and cifar10 dataset from tensorflow keras datasets. There are total 10 classes as shown below. 
![image](https://user-images.githubusercontent.com/80217865/156740284-59e74b85-0b8a-4dca-a787-4b3bdccdc2f1.png)

Also this project is hosted on Heroku, so you can access it through this link:
https://awimgclassifier.herokuapp.com/


## Installation

There is requirements.txt in the project folder, so it is needed to use this to work with project:
First of all move to project directory and then simply type in terminal:
* ### Requirements.txt
```python $ pip install -r requirements.txt ```

and it will install all needed libraries.

* ### PostgreSQL Database [Download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

* ### To run the server
```python $ cd img_classifier```
```python $ python manage.py runserver```

## Usage
You can access directly to the website by this link:
https://awimgclassifier.herokuapp.com/

Or After installing needed modules, just run the server as it was shown above, it will start server.

By Default it will start on : http://127.0.0.1:8000/

## Examples
Generally we have home page, where we can submit image and see result after pressing "submit" button:
![image](https://user-images.githubusercontent.com/80217865/156741755-9fcc20f4-45a2-436c-bb7c-4403da9bacb1.png)

Also we have "history" page, where we can see previously loaded images and results:
![image](https://user-images.githubusercontent.com/80217865/156741905-86a79da4-f2b7-4ce4-a36f-9da8e504c2e9.png)

