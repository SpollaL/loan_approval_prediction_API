Loan Model API
================

Welcome to the Loan Model API repository! 🚀

This repository contains the implementation of a loan approval prediction model using machine learning and Django as the web framework.

**Overview**
-----------

The Loan Model API is a web-based application that predicts the approval of a loan application based on various factors such as first name, last name, gender, marital status, education, income, loan amount, and credit history.

**Key Features**
---------------

* **Loan Approval Prediction**: The API uses a machine learning model to predict the approval of a loan application based on user input.
* **User-Friendly Interface**: The API provides a user-friendly interface for users to input their details and receive a prediction.
* **RESTful API**: The API is built using Django Rest Framework, providing a RESTful API for clients to interact with.

**Technical Details**
--------------------

### Models

* **Approval Model**: The `models.py` file defines the `Approval` model, which has various fields to store information about an approval application.

### Serializers

* **ApprovalsSerializer**: The `serializers.py` file defines a serializer for the `Approval` model, which converts the model data into a format suitable for API responses.

### Views

* **predict_view**: The `views.py` file defines a view function that handles the `/predict/` URL, which is used for making predictions. It uses a machine learning model loaded from a pickle file to make predictions based on user input.

### Forms

* **PredictionForm**: The `forms.py` file defines a form for the `Approval` model, which can be used for creating and editing `Approval` instances.

### Tests

* **TestCase**: The `tests.py` file defines a test case class for unit testing the application.

**Getting Started**
-------------------

To get started with the Loan Model API, follow these steps:

1. Clone the repository using `git clone <repository_url>`
2. Install the dependencies using `poetry install`
3. Run the development server using `python manage.py runserver`
4. Access the API using a REST client or a web browser

**Dependencies**
--------------

* **Django**: The Loan Model API relies on Django as the web framework.
* **Django Rest Framework**: The API uses Django Rest Framework for building the RESTful API.
* **Pickle**: The API uses pickle for loading the machine learning model.
* **Pandas**: The API uses pandas for data manipulation.
