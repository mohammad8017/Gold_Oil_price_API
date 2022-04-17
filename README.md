# Gold_Oil_price_API
Rest API with django-rest-api for give data of oil, Gold and Shakhes in a specific date.
## Installation

* **Docker** 
  - Install and signup in [Docker](https://hub.docker.com/)
  - pull mySQL image.
    - ```bash
      docker pull mysql
      ```
  - create container
    - ```bash
      docker run -d -p 3306:3306 --name=mysql-server --env="MYSQL_ROOT_PASSWORD=123456" mysql_db
      ```
  - Access to MySQL
    - ```bash
      docker exec -ti mysql-server bash 
      ```
    - note: use password 123456 to access MySQL
  - Create user and database for the connection
    - ```bash
      CREATE DATABASE db_api;
      CREATE USER 'mohammad'@'localhost' IDENTIFIED BY '123456';
      GRANT ALL PRIVILEGES ON db_api.* TO 'mohammad'@'localhost';
      FLUSH PRIVILEGES;
      QUIT
      ```
  - For see which users use Prices API use this command in MySQL shell in db_api database
    - ```bash
      select * from user_request;
      ```
      
* **Virtual Environment**
  - Create Environment
    - ```bash
      python -m venv virEnv
      ```
  - Activate Environment
    - ```bash
      virEnv\Scripts\activate
      ```
  - Install requirements
    - ```bash
      pip install -r requirements.txt
      ```
  - Deactivate Environment (For finishing your work)
    - ```bash
      virEnv\Scripts\deactivate.bat
      ```
      
      
## Explaination

  - This project has 6 APIs which I explain them in the following 
    - Admin
      - path: http://127.0.0.1:8000/admin/
      - what's doing: Admin panel for control users and data...
      - input(s): username and password of admin which wants to enter.
    - Prices
      - path: http://127.0.0.1:8000/prices/
      - what's doing: give prices of Gold, Oil and Shakhes in specific period.
      - Body: start_date, end_date   (Value ex. 20190102)
      - Headers: Authorization  (Value ex. Token c46970bbc11179910d7347588e651f41e75e1368)
      - response: request_time, start_date, end_date, oil_prices, gold_prices, shakhes
    - Reset Password
      - path: http://127.0.0.1:8000/rest-auth/password/reset/
      - what's doing: reset password for users with recovery mail.
      - Body: recovery mail
    - Register
      - path: http://127.0.0.1:8000/rest-auth/registration/
      - what's doing: Register users.
      - Body: Username, Email, Password1, Password2
      - response: Registration successfully completed
    - Login
      - path: http://127.0.0.1:8000/rest-auth/login/
      - what's doing: Login user and give user token for using Prices API.
      - Body: username, email, password
      - response: user token
    - Logout 
      - path: http://127.0.0.1:8000/rest-auth/logout/
      - what's doing: Logout user.
      - Headers: user token
      - response: Successfully logged out




## Run project
   - For running prject you should use these commands
      - Migrate and Migration
        - ```bash
          python manage.py makemigrations
          python manage.py migrate
          ```
      - Strat server
        - ```bash
          python manage.py runserver
          ```
      - For create admin user you can use this command
        - ```bashe
          python manage.py createsuperuser
          ```
        - Choose an username and a password for this user and after that you can use admin panel.








