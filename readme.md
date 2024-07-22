## Clavax School Management System



## Table of Contents


- [About](#about)
- [Modules Versioning](#modules)
- [Installation](#installation)
- [Run this Project](#run)
- [Task Done](#task)
- [Admin Credentials](#admin)
- [Pending Task](#pending)
    





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
<a name="run"></a>
- Installed IDE like VSCode or Pycharm
- Go Dir **cd clavax_school**
- check Manage.py file exist If Exist your are in correct path
    - `python manage.py runserver` this Django Project run


## Home Page 
- ![image](https://github.com/user-attachments/assets/e142bce9-2484-496d-92ca-64bf333da31f)

## Task Done
<a name='task'></a>
### 1. Class Model | Class Name : StudentClass
- Souce Code
    - ![image](https://github.com/user-attachments/assets/df3cc9fc-c719-4602-bd08-8ab5ee50bb1d)
- GUI | URL : http://127.0.0.1:8000/class/
    - ![image](https://github.com/user-attachments/assets/e45a73e5-1e23-4fc2-b50f-4f4ef0318a71)
- API | URL : http://127.0.0.1:8000/api/v1/class/
    - ![image](https://github.com/user-attachments/assets/ac70db81-6eca-4013-bab6-6d8038092442)

### 2. Register Students and Assign Classes
- API | URL : http://127.0.0.1:8000/api/v1/register/
    - ![image](https://github.com/user-attachments/assets/3057581e-d162-4c43-a15d-e0c2465761fc)
- GUI | URL : http://127.0.0.1:8000/student/ 
    - ![image](https://github.com/user-attachments/assets/22d3d7a8-f92d-4a94-a88f-8053399d4be0)
 
      
### 4. Student Profile 
- Profile Information and Images
    - ```.json
          {
        "id": 7,
        "first_name": "Virat",
        "last_name": "Kholi",
        "email": "virat@kholi.com",
        "phone": 1234567890,
        "date_of_birth": "2012-02-12",
        "status": false,
        "images": "http://127.0.0.1:8000/media/student_images/Virat_5eezVGB.png",
        "student_class": 2
        }
      ```  
    - ![image](https://github.com/user-attachments/assets/dfe3dab7-ef2d-4b38-989c-57ff49104e3f)
    - ![image](https://github.com/user-attachments/assets/7b55f595-123e-41b5-b452-a6ea49950fca)



### 5. Student Profile Update
- CRUD operations | URL : http://127.0.0.1:8000/api/v1/student/
    - ![image](https://github.com/user-attachments/assets/1ed1e0f6-aa7a-4760-a556-a5e367244e24)
 
### Admin Page
<a name="admin"></a>

#### Admin Credentials     
- Admin username : admin
- Admin Password : admin

#### Web Pages
- Home Page
    - ![image](https://github.com/user-attachments/assets/a2b01b70-00c8-442f-8261-fdcbf0670f7f)
- Class Page
    - ![image](https://github.com/user-attachments/assets/bed0b22a-733c-419b-987f-f5487550733b)
- Student Page
    - ![image](https://github.com/user-attachments/assets/201915b1-ef73-4c1b-b2bb-011dc05c7bca)
 
 

### Pending Task
<a name='pending'></a>
- Customised Student Authentication and Authorization
- Task 3 Admin Page , Button For Deactive Not implemented
- JWT Token Implement 










# Thank You 




