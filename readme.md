## Clavax School Management System

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


