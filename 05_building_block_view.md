# Building Block View

## Searching and Getting schemas
The project has a search functionality for schemas, utilizing a web-based interface. The system is designed with a frontend that interfaces with a backend server to query a database and display the results to the user.
### Technology Stack

    Frontend: HTML, CSS, JavaScript (Vanilla JS))
    HTTP Client: Axios
    Backend: Python (FastAPI)
    ORM: SQLAlchemy
    Database: SQLAlchemy

### Data Flow
#### 1. User Interface
The user interface is created using HTML for the structure, CSS for styling using Twitter Bootstrap, and plain JavaScript to manage dynamic data and interactions. The user inputs their search parameters into an HTML form, and the JavaScript captures these parameters when the form is submitted.

#### 2. HTTP Request
Upon form submission, JavaScript passes the search parameters to Axios, an HTTP client. Axios packages these parameters into a GET request to the server running the FastAPI application. The endpoint it targets is `/schemas`, and the search parameters are appended as query parameters.

#### 3. Backend - FastAPI
FastAPI receives the GET request at the `/schemas` endpoint. The query parameters are automatically parsed into Python variables and passed as arguments to the `get_schemas` function.

#### 4. Fetching Schemas - SchemaFetcher
A SchemaFetcher instance is created using a Service instance. The Service instance is obtained via FastAPI's dependency injection system. The `fetch_schemas_by_criteria` method of the SchemaFetcher class is then invoked, passing the received search parameters.

#### 5. Service Layer
The `fetch_schemas_by_criteria` method communicates with the Service class, invoking its `get_schemas_by_criteria` method. The Service instance, acting as a liaison between the fetcher and the database, communicates with the Database class to retrieve the data from the database.

#### 6. Database Access
The Database class uses SQLAlchemy to build a SQL query in the `search_schemas_by_criteria` method. This SQL query fetches schemas matching the search parameters from the database. Pagination is also applied at this level. The results from the SQL query are SchemaModel instances.

#### 7. Service Layer (Continued)
Back in the Service class, the `get_schemas_by_criteria` function transforms these SchemaModel instances into SchemaOut instances. This represents data ready to be sent back to the client.

#### 8. Fetching Schemas (Continued)
The list of SchemaOut instances, along with the total pages count, are returned to the `fetch_schemas_by_criteria` function in the SchemaFetcher class.

#### 9. API Endpoint
The `get_schemas` function receives the SchemaOut instances and total pages count. If no schemas are found, a 404 HTTP exception is raised. Otherwise, a CustomPage object is created with the schemas and returned as a JSON response to the frontend.

#### 10. HTTP Response
Axios in the frontend receives the HTTP response, containing the paginated schema data.

#### 11. User Interface (Continued)
Upon receiving the response, JavaScript updates the DOM with the new data (the schemas), providing a visual representation of the results to the user.

#### 12. Flow Diagram
```mermaid

flowchart LR
    A(User Interface) --> B(Process Search)
    B --> C[Capture Search Parameters]
    C --> D{Parameters Valid?}
    D -- Yes --> E[Create HTTP Request]
    E --> F(Send HTTP Request)
    F --> G[Handle HTTP Response]
    G --> H{Response Valid?}
    H -- Yes --> I[Retrieve Schemas from Database]
    I --> J[Transform Schemas]
    J --> K[Create JSON Response]
    K --> L(Send JSON Response)
    L --> M[Update DOM with Results]
    M --> N(End)
    H -- No --> O[Display Error Message]
    O --> N
    
    D -- No --> P[Display Error Message]
    P --> N
    
    J --> Q{Continue Searching?}
    Q -- Yes --> B
    Q -- No --> N