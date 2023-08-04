# Kanban Board Project

This is a Kanban Board project built with ReactJS and Django. The project allows users to manage tasks in a Kanban-style board, where tasks can be categorized into three columns: "Not Started," "In Progress," and "Completed." Users can register with their username, email, and password, and login using their email and password. The backend securely hashes the password and responds with a token for authentication.

## Features

- Home Page: The home page displays login and register buttons to access the Kanban board functionalities.

- User Registration: Users can register on the platform by providing a unique username, valid email address, and a strong password.

- User Login: Registered users can log in to the Kanban board using their email and password. The password is securely hashed on the backend, ensuring the security of user credentials.

- Kanban Board: The Kanban board consists of three columns: "Not Started," "In Progress," and "Completed." Users can create tasks and move them between columns to track their progress.

- Task Management: Users can create new tasks with a task name and description. The start date, end date, updated at, and created at attributes are automatically set and updated in the database. Users can also search for the tasks as well as get only the tasks based on the time period selected in the dropdown

- Identicon Generation: Each user is assigned a unique identicon generated based on their username.

- Logout: The Kanban board includes a logout button that allows users to securely log out from their session.

## Technologies Used

- ReactJS: Frontend library for building user interfaces.
- Django: Backend framework for building secure and scalable web applications.
- Django REST framework: Enables building RESTful APIs with Django.
- Identicon: Library for generating unique user identicons based on usernames.

## Getting Started

1. Clone the repository: `git clone https://github.com/sanskarjaiswal2001/kanban-board.git`
2. Install frontend dependencies: `cd kanban-board/frontend && npm install`
3. Install backend dependencies: `cd ../kanban-board-backend-1939 && pip install -r requirements.txt`
4. Set up the database and run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## Usage

1. Open your browser and navigate to `http://localhost:8000/Home` to access the home page.
2. Click on the "Register" button to create a new account or use the "Login" button to log in with your existing credentials.
3. After successful login, you will be automatically redirected to the Kanban board.
4. Use the "Create Task" button to create new tasks, and drag and drop tasks between the columns to track their progress.
5. You can also update existing tasks by clicking on them and editing the details.

## Note

This project is for educational and demonstration purposes only. Do not use it in production without proper security considerations and additional features like user authentication, authorization, and validation. Ensure you follow best practices for password management and security when deploying it in a production environment.
