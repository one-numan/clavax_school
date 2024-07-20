## Clavax School Management System



## Table of Contents


- [About](#about)
- [Modules Versioning](#modules)
- [Installation](#installation)
- [Run this Project](#run)
- [Task](#task)





________________________



<a name='about'></a>
__Assignment: School Management System using Django Backend and Django Rest API__

Backend Part:
1. Create a Class Model and Form View to Add a Class (2 Marks)

    - Design a Django model for classes with necessary fields (e.g., class name).
    - Create an admin view where an admin can input class details, including class names.

2. Register Students and Assign Classes (3 Marks)

    - Develop a Django Rest API endpoint to register students with the following fields: first
name, last name, phone, email, password, date of birth, status (default is inactive),
image upload, and a dropdown to select a class created in the Class model.
    - Ensure that the endpoint includes proper validation to enhance data integrity and
security.

3. Activate/Deactivate Students from Admin Panel (1 Mark)
    - Add a feature in the Django admin panel to activate or deactivate student accounts and send an email or SMS if the account is de-activated

4. Implement Student Login (2 Marks)
    - Create a Django Rest API endpoint for student login.
    - Only activated students should be able to log in. Implement a mechanism for the admin
to activate/deactivate students through the API.

5. Student Profile Update (2 Marks)

    - Develop an API endpoint that allows students to update their profiles, including their
image and other fields.
• Ensure the endpoint is protected and requires authentication.




---
## Modules
<a name="modules"></a>
| Modules / Library Name | Version |
| ---------------------- | ------- |
| Python                 | 3.10.8  |
| Django                 | 5.0.7 |
| Django Rest Framework  | 3.15.2       |
| HTML                   | 5       |
| Bootsrap               | 5.3   |

## Installation

- Clone this Repo
      - `git clone https://github.com/one-numan/clavax_school.git`
- Install Python3
- Installing Required Python Modules from File **Requirements.txt**
  - Command `pip install -r requirements.txt`

## Run
<a name="run"> </a>
- Installed IDE like VSCode or Pycharm
- Go Dir **cd clavax_school**
- check Manage.py file exist If Exist your are in correct path
    - `python manage.py runserver` this Django Project run

## Home Page 
- ![image](https://github.com/user-attachments/assets/e142bce9-2484-496d-92ca-64bf333da31f)

## Task   
### 1. Student Model
- ![image](https://github.com/user-attachments/assets/df3cc9fc-c719-4602-bd08-8ab5ee50bb1d)

