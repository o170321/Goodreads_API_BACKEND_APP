# Goodreads_API_BACKEND_APP

# Goodreads API

The Goodreads API is a simple web service that allows users to interact with a database of books and user profiles. It provides endpoints for accessing book information, user registration and login, and user profile details. The API is built using Node.js and SQLite for data storage, and it incorporates authentication and authorization mechanisms using JSON Web Tokens (JWT).

## Table of Contents

- [Getting Started](#getting-started)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Get Books](#get-books)
  - [Get Book](#get-book)
  - [User Register](#user-register)
  - [Get Profile](#get-profile)
  - [User Login](#user-login)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Before using the Goodreads API, you need to set up your environment and initialize the database. Follow these steps:

1. Clone the repository to your local machine.
2. Install the required Node.js packages by running:

   ```bash
   npm install
   ```

3. Initialize the SQLite database:

   ```bash
   npm run initialize
   ```

4. Start the server:

   ```bash
   npm start
   ```

The server will be running at `http://localhost:3000/`.

## Authentication

The Goodreads API uses JSON Web Tokens (JWT) for authentication. To access protected routes, you must include a JWT in the `Authorization` header of your requests. You can obtain a JWT by registering as a user and then logging in.

## Endpoints

### Get Books

#### `GET /books/`

This endpoint allows you to retrieve a list of all books in the database.

- **Authentication Required**: Yes

#### Example Request:

```http
GET /books/
Authorization: Bearer <JWT>
```

### Get Book

#### `GET /books/:bookId/`

Retrieve information about a specific book by providing its `bookId`.

- **Authentication Required**: Yes

#### Example Request:

```http
GET /books/123/
Authorization: Bearer <JWT>
```

### User Register

#### `POST /users/`

Register a new user with the following details:

- Username
- Name
- Password
- Gender
- Location

If the username is unique, the user will be created in the database.

- **Authentication Required**: No

#### Example Request:

```http
POST /users/
Content-Type: application/json

{
  "username": "newuser",
  "name": "John Doe",
  "password": "password123",
  "gender": "Male",
  "location": "New York"
}
```

### Get Profile

#### `GET /profile/`

Retrieve the user profile for the currently authenticated user.

- **Authentication Required**: Yes

#### Example Request:

```http
GET /profile/
Authorization: Bearer <JWT>
```

### User Login

#### `POST /login/`

Log in as an existing user by providing a valid username and password. If successful, you will receive a JWT for authentication.

- **Authentication Required**: No

#### Example Request:

```http
POST /login/
Content-Type: application/json

{
  "username": "existinguser",
  "password": "password123"
}
```

## Usage Examples

Here are some usage examples for the Goodreads API:

### Get a List of Books

```http
GET /books/
Authorization: Bearer <JWT>
```

### Retrieve Book Information

```http
GET /books/123/
Authorization: Bearer <JWT>
```

### Register a New User

```http
POST /users/
Content-Type: application/json

{
  "username": "newuser",
  "name": "John Doe",
  "password": "password123",
  "gender": "Male",
  "location": "New York"
}
```

### Get User Profile

```http
GET /profile/
Authorization: Bearer <JWT>
```

### Log In as a User

```http
POST /login/
Content-Type: application/json

{
  "username": "existinguser",
  "password": "password123"
}
```

## Contributing

Contributions to the Goodreads API are welcome. You can contribute by opening issues, providing feedback, or submitting pull requests. Please follow the [contribution guidelines](CONTRIBUTING.md) when contributing to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
