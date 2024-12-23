# Django-project-165437
# Airline Booking System

## Overview
The Airline Booking System is a web application that allows users to manage flights and passengers. It provides functionalities for creating, retrieving, updating, and deleting (CRUD) operations for both flights and passengers. The application is built using Django for the backend and React for the frontend.

## Features
- User registration and login
- Role-based access control (admin and user roles)
- CRUD operations for flights and passengers
- Flight and passenger management through a user-friendly interface
- Responsive design using Bootstrap

## Technologies Used
- **Backend**: Django, Django Rest Framework
- **Frontend**: React, Axios, Bootstrap
- **Database**: SQLite (default for Django)

## Project Structure

## Setup Instructions

### Backend Setup
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd airline_booking_system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for accessing the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Django server**:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install frontend dependencies**:
   ```bash
   npm install
   ```

3. **Run the React application**:
   ```bash
   npm start
   ```

## Usage
- Access the application at `http://localhost:3000` for the frontend.
- Access the Django admin panel at `http://localhost:8000/admin` to manage flights and passengers.
- Use the application to register users, log in, and manage flight and passenger data.

## API Endpoints
- **Flights**:
  - `GET /api/flights/` - List all flights
  - `POST /api/flights/` - Create a new flight
  - `GET /api/flights/{id}/` - Retrieve a flight by ID
  - `PUT /api/flights/{id}/` - Update a flight by ID
  - `DELETE /api/flights/{id}/` - Delete a flight by ID

- **Passengers**:
  - `GET /api/passengers/` - List all passengers
  - `POST /api/passengers/` - Create a new passenger
  - `GET /api/passengers/{id}/` - Retrieve a passenger by ID
  - `PUT /api/passengers/{id}/` - Update a passenger by ID
  - `DELETE /api/passengers/{id}/` - Delete a passenger by ID

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Simplified Airline Booking System

This project is a simplified airline booking system built using Django and React. It provides an API for managing flights and passengers and a front-end interface for users to interact with the system.

---

## Features

1. **Django Backend**
   - Models for flights and passengers.
   - RESTful API endpoints for CRUD operations.
   - Filtering and pagination for enhanced user experience.
2. **React Frontend**
   - View available flights and passengers.
   - Add passengers to specific flights.
   - View detailed flight information, including associated passengers.

---

## Project Setup

### Prerequisites
 - **Backend**: Django, Django Rest Framework
- **Frontend**: React, Axios, Bootstrap
- **Database**: SQLite (default for Django)


### Backend Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd airline-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   - Update `settings.py` to include your database credentials under `DATABASES`.
   - Apply migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the React project:
   ```bash
   cd airline-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

4. Open your browser and go to `http://localhost:3000`.

---

## Detailed Explanation

### Models

#### **Flight Model**
Represents a flight in the airline system.
- **Fields:**
  - `flight_number`: Unique identifier for the flight.
  - `departure`: Date and time of departure.
  - `arrival`: Date and time of arrival.
  - `origin`: Origin airport.
  - `destination`: Destination airport.
  - `capacity`: Total number of seats available on the flight.

#### **Passenger Model**
Represents a passenger in the system.
- **Fields:**
  - `first_name`: First name of the passenger.
  - `last_name`: Last name of the passenger.
  - `email`: Unique email address of the passenger.
  - `phone_number`: Contact number of the passenger.
  - `flight`: ForeignKey to the `Flight` model.

---

### Serializers

#### **FlightSerializer**
- Converts the `Flight` model instances into JSON format.
- Includes all fields of the flight model.

#### **PassengerSerializer**
- Converts the `Passenger` model instances into JSON format.
- Includes a nested representation of the associated flight.

---

### Views/ViewSets

#### **FlightViewSet**
- Handles CRUD operations for the `Flight` model.
- Endpoints:
  - `GET /flights/`: List all flights.
  - `GET /flights/<id>/`: Retrieve details of a specific flight.
  - `POST /flights/`: Create a new flight.
  - `PUT /flights/<id>/`: Update an existing flight.
  - `DELETE /flights/<id>/`: Delete a flight.

#### **PassengerViewSet**
- Handles CRUD operations for the `Passenger` model.
- Endpoints:
  - `GET /passengers/`: List all passengers.
  - `GET /passengers/<id>/`: Retrieve details of a specific passenger.
  - `POST /passengers/`: Create a new passenger.
  - `PUT /passengers/<id>/`: Update an existing passenger.
  - `DELETE /passengers/<id>/`: Delete a passenger.
- Additional Features:
  - Filter passengers by flight using query parameters (e.g., `?flight=<flight_id>`).

---

### Design Decisions

1. **Django REST Framework**
   - Used for rapid development of API endpoints.
   - Leveraged ViewSets for CRUD operations to minimize boilerplate code.

2. **ForeignKey Relationship**
   - Enforced a `Passenger` to always be associated with a `Flight`.

3. **Frontend-Backend Integration**
   - Used Axios in React for making HTTP requests to the Django API.

4. **Filtering and Pagination**
   - Implemented filtering on passengers to improve usability.
   - Added pagination to list views for scalability.

---

## Optional Enhancements
- **Seat Availability Check**: Prevent booking if the flight is at full capacity.
- **User Authentication**: Secure APIs and provide role-based access (e.g., admin vs. user).
- **Styling**: Use a modern UI library (e.g., Material-UI) for an improved user interface.
- **Deployment**: Deploy the application on platforms like Heroku or AWS.

---

## Running Tests
To run the backend tests:
```bash
python manage.py test
```

---

## Conclusion
This project demonstrates a simplified airline booking system with robust API endpoints and a user-friendly interface. It can be extended with additional features such as payment integration, real-time notifications, and advanced filtering options.

---

For any questions or issues, feel free to contact the project maintainer.

