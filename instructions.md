Django API Development Exercise: Simplified Airline Booking System
Objective:
This exercise is designed to assess your understanding of building API-based applications in Django. You will develop a simplified API for an airline booking system that manages flights and passengers. The focus is on creating models, serializers, and views/viewsets.
Task Overview:
You are required to build an API-based application that simulates a simplified airline booking system. The application should include models for flights and passengers. The API should allow for creating, retrieving, updating, and deleting (CRUD) operations for each of these entities.
Requirements:
1. Models:
Flight:
Represents a flight in the airline system:
•	flight_number: CharField, unique identifier for the flight.
•	departure: DateTimeField, the date and time of departure.
•	arrival: DateTimeField, the date and time of arrival.
•	origin: CharField, the origin airport.
•	destination: CharField, the destination airport.
•	capacity: IntegerField, the total number of seats available on the flight.
Passenger:
Represents a passenger in the system:
•	first_name: CharField, the first name of the passenger.
•	last_name: CharField, the last name of the passenger.
•	email: EmailField, unique email address of the passenger.
•	phone_number: CharField, contact number of the passenger.
•	flight: ForeignKey to Flight, relates the passenger to a specific flight.
2. Serializers:
•	Create serializers for each of the models. The PassengerSerializer should include details about the related flight.
3. Views/ViewSets:
Use Django Rest Framework's ViewSets to create views for each of the models. 
Implement endpoints for the following operations:
•	List all flights and passengers.
•	Retrieve a single flight or passenger by ID.
•	Create a new flight or passenger.
•	Delete a flight or passenger.
4. Relationships and Constraints:
•	A Flight can have multiple Passengers.
•	A Passenger must be associated with exactly one Flight.
5. Optional Enhancements:
•	Add filtering options to viewsets (e.g., filter passengers by flight).
Implement pagination for list endpoints.
Deliverables:
•	A GitHub repository containing your Django project. Name of the Repo should include your student ID.
•	A README.md file with instructions on how to set up and run the project.
•	A detailed explanation of the models, serializers, views/viewsets, and any other notable design decisions.

