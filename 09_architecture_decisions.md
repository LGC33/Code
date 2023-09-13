# Architecture Decisions

1. [Choose Backend Framework](#choose_backend_framework)
2. [Choose Database](#choose_database)
3. [Choose Frontend Framework](#choose_frontend_framework)
4. [Choose Frontend Library](#choose_frontend_library)
5. [Choose XDF2 File Storage Location](#choose_xdf2_file_storage_location)
6. [Choose authentication token solution](#token_solution)
7. [Internal Id for Codelists](#internal_id_for_codelists)
8. [Use of sqladmin library](#sqladmin)

<a name="choose_backend_framework"></a>

## 1. Choose Backend Framework

### Status

Accepted

### Context

We are in the process of developing a web application, and we need to choose a framework for building the backend API. Our team has experience with both Flask and FastAPI, but we need to decide which one to use for this project.

### Decision

After careful consideration, we have decided to use FastAPI for the following reasons:

#### 1. Performance

FastAPI is built on top of the ASGI server, which is designed to handle asynchronous requests. This makes it much faster than Flask, which uses the traditional WSGI server. In benchmarks, FastAPI has been shown a lot faster than Flask for certain use cases.

#### 2. Type Annotations and Automatic API Documentation

FastAPI makes use of Python's type annotations to automatically generate API documentation, which can save developers a lot of time and effort. Additionally, it provides a built-in interactive API documentation system, Swagger UI, that allows users to interact with the API and see the responses in real-time.

#### 3. Easy to Use

FastAPI is designed to be easy to use, with a simple and intuitive API that requires minimal boilerplate code. It also has excellent support for modern Python features like async/await, data classes, and type hints.

#### 4. Integration with Modern Python Libraries

FastAPI is built using modern Python libraries, like Pydantic for data validation and Starlette for async I/O handling. This makes it easier to integrate with other modern Python libraries and frameworks.

#### 5. Asynchronous Support

FastAPI is designed with first-class support for asynchronous programming, making it easier to handle long-running I/O-bound tasks without blocking the event loop. This can be especially useful in API and backend focused applications.

### Consequences

While there are some downsides to choosing FastAPI over Flask, we believe that the benefits outweigh the costs. Here are some of the consequences of our decision:

#### 1. Learning Curve

FastAPI has a steeper learning curve than Flask, especially for developers who are not familiar with modern Python features like async/await and type annotations. However, we believe that the benefits of using FastAPI make it worth the investment in learning.

#### 2. Ecosystem

Flask has a larger ecosystem of plugins and extensions than FastAPI, which means that it may be easier to find solutions to common problems in Flask. However, we believe that the advantages of FastAPI's performance and ease of use outweigh this disadvantage.

#### 3. Compatibility

FastAPI is only compatible with Python 3.6 and higher, while Flask can be used with Python 2.7 and higher. This means that FastAPI may not be the best choice for projects that need to support older versions of Python.

### Conclusion

After weighing the pros and cons of both frameworks, we have decided to use FastAPI for our project. We believe that its performance, ease of use, and automatic API documentation features make it the best choice for our needs.

<a name="choose_database"></a>

## 2. Choose database

### Status

Proposed

### Context

In order to store data schema files based on the XDatenfelder2 and [XDatenfelder3](https://www.xrepository.de/details/urn:xoev-de:fim:standard:xdatenfelder) standard, a backend data storage is required.

### Decision

After careful consideration, the team has decided to use PostgreSQL as the database management system for the project. PostgreSQL is a widely used and well-known database management system that is suitable for the simple purpose at hand. The team is familiar with PostgreSQL, and it offers excellent support for complex data structures.

### Consequences

By choosing PostgreSQL, the team will be able to easily analyze data schema files for overlap and reuse. It will also be possible to convert XDF2 and XDF3 files to a common database format, which will serve as the basis for XDF2-XDF3 and XDF3-XDF2 conversions. The team can also expect excellent performance and scalability, as PostgreSQL is designed to handle large amounts of data with ease.

<a name="choose_frontend_framework"></a>

## 3. Choose Frontend Framework

### Status

Proposed

### Context

The goal of the project FIM-Sammelrepository is to provide users with an API. For educational and presentation purposes it was agreed upon that a slick and simple User Interface (UI) is required.

### Decision

The team will not employ a frontend framework (react, vue-js etc.) but will stick with what's readily available with python, fast API, ninja etc. This decision is made in order to enhance speed and reduce dependencies, and avoid unnecessary complexity.

### Consequences

- It will be closely monitored if the decision results in a less user friendly user interface (e.g. dynamic search field)
- It will be easier for new developers to understand and work with the existing less complex setup.
- There is one less technical dependency to take care of.

<a name="choose_frontend_library"></a>

## 4. Choose Frontend Library

### Status

Proposed

### Context

Our team is developing a web application that requires a responsive and easy-to-use front-end framework. We need a framework that can help us build consistent and visually appealing user interfaces quickly.

#### Options

    Twitter Bootstrap
    Foundation
    Materialize
    Semantic UI

### Criteria

We evaluated each framework based on the following criteria:

    Ease of use and speed of development
    Customizability and flexibility
    Cross-browser compatibility
    Community support and documentation
    Accessibility

### Decision Evaluation

1. Ease of use and speed of development: Twitter Bootstrap provides an extensive set of pre-built components and classes that can be easily used to develop responsive user interfaces quickly. This allows our team to focus on building functionality instead of spending time on styling and layout.
2. Customizability and flexibility: While Twitter Bootstrap provides a lot of pre-built components, it also allows for customization through SASS variables and mixins. This gives us the flexibility to create unique designs while still leveraging the framework's core features.
3. Cross-browser compatibility: Twitter Bootstrap is well-tested and supports all major browsers, including IE11. This ensures that our application will work seamlessly across different devices and browsers.
4. Community support and documentation: Twitter Bootstrap has a large community of developers who contribute to the project and provide support through forums, documentation, and tutorials. This makes it easy for our team to get help and stay up-to-date with the latest features and best practices.
5. Accessibility: Twitter Bootstrap has built-in accessibility features, such as ARIA labels and roles, that help ensure our application is accessible to all users.

### Consequences

Using Twitter Bootstrap for front-end development will allow our team to build consistent and visually appealing user interfaces quickly, while also providing the flexibility to create unique designs. The framework's extensive community support and documentation will help us stay up-to-date with the latest features and best practices, while its built-in accessibility features will ensure that our application is accessible to all users.

### References

- Twitter Bootstrap documentation: https://getbootstrap.com/docs/5.1/getting-started/introduction/
- Bootstrap Accessibility Plugin: https://github.com/paypal/bootstrap-accessibility-plugin

<a name="choose_xdf2_file_storage_location"></a>

## 5. Choose XDF2 File Storage Location

### Status

Proposed

### Context

A requirement for the development of system data exchange in the realm of public IT is the addressability of XDatenfelder2 (XDF2) conformant files. These files contain data schema (Datenschema) and meta data (Dokumentsteckbrief). They will need to be made available even after some or most of the newer files will abide to the XDF3 standard, an updated version of XDF2.

It was proposed to store existing XDF2 files on a file share that would allow these files to be adressed in a simple fashion, e.g. http://public-address-of-fileshare/dataschema-id.xdf. Alternatively these files could be made available through the API of the FIM-Sammelrepository, e.g. http://public-address-of-sammelrepository/api-details/dataschema-id.xdf.

### Decision

The fileshare approach has advantages w.r.t. to technical simplicity. Existing scripts to transport xdf files to the FIM-Portal that access xdf files from "Landesrepository" locations need no changes except for the xdf file location adresses (urls)

The Sammelrepository approach has advantages w.r.t. to the ability to conduct data analysis, support both xdf2 and xdf3 from a single repository, a unified maintenance and support approach for all types of stakeholders (both public and private IT service providers) and a one-stop-solution for both FIM-Stammdaten and OZG-Referenzdaten.

The project team strongly favors the FIM-Sammelrepository over the fileshare approach.

### Consequences

Making XDF2 available for an indefinite time as a fallback option for xdf3 adverse scenarios implies that they must not be tranformed to XDF3 ever but they need to be kept "as is" inside the database. The same goes for codelists, Excel and CSV files that commonly accompany XDF2 files (Datenschema, Dokumentsteckbrief).

As a further consequence it is recommended for this FIM-Sammelrepository project to implement the M2M interface that are hitherto provided by FJD based Landesredaktionssysteme. This would allow existing interfacing system to continue using the M2M interface and XDF2 files up to the point in time when they are ready for XDF3 migration.

<a name="token_solution"></a>

## 6. Choose authentication token solution

### Status

Proposed

### Context

The solution described in this architecture documentation must incorporate  some sort of authentication system. A key decision we need to make is how to manage authentication for user groups (distinct groups of users). The two main options we've considered are:

1. Developing a full-fledged authentication system that securely stores hashed and salted passwords, manages sessions, supports password reset and account verification mechanisms, and possibly implements two-factor authentication.
2. Storing authentication tokens for each usage group in a database table. The usage group would provide their token as part of API requests to authenticate themselves.

### Decision

We've decided to choose the second option: storing authentication tokens for each usage group in a database table.
The main factors driving this decision are time, cost, and resource constraints.
Developing a comprehensive authentication system is complex and time-intensive. It involves handling numerous edge cases and adhering to security best practices. On the other hand, the token-based approach is much simpler to implement and understand. 
Moreover, the costs and resources required for the more complex solution would be considerably higher. Choosing the token-based approach allows us to allocate those resources towards enhancing our core features and user experience.
Though a full-fledged authentication system has its merits in terms of robustness and scalability, we believe that given our current use case and audience size, the token-based approach will suffice. This is mainly because, in our current development phase, the tokens will be used only for uploading schemas. The simplicity of these operations makes token-based authentication a sufficient choice.
In addition, this approach does not eliminate the possibility of implementing a more complex authentication system in the future as our application grows.
Finally, a token-based approach is secure when implemented correctly, meeting our application's needs without the overhead associated with a more complex authentication system.

#### Distribution of Tokens

Once the tokens are generated, they will be securely exported to the corresponding usage groups. The tokens will serve as the means of authenticating and authorizing the group's operations, specifically for uploading schemas.

### Consequences

By choosing a token-based authentication system, we can save time, money, and resources, which we can then reinvest into other areas of our project.
However, as we scale and potentially handle more sensitive data, we may need to revisit this decision and consider implementing a full authentication system.

<a name="internal_id_for_codelists"></a>

## 7. Internal Id for Codelists

### Status

Accepted

### Context

There are currently multiple problems with the unique identification of code lists with the existing identifiers:

- In xdf2, both a FIM-Id (e.g. `C00000009`) and genericode identifiers (e.g. `urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat_2017-01-01`) are provided for every code list.
  However, these are never globally checked for consistency when created.
  As a result, the same FIM-Id/genericode identifier can point to different code lists (e.g. two authors working on different local repositories create/edit two code lists with identical IDs but non identical contents).
- In xdf3, the genericode identifier is the only identifier for a code list and _must_ link to a code list in the XRepository. Therefore, for xdf3, the global uniqueness is checked.
- In xdf2, code lists with the same identifiers must not be considered identical, whereas in xdf3, code lists with the same identifier are by design identical.
  The solution should therefore allow for multiple code lists with the same identifiers to be saved, while also allowing to easily reuse identical code lists.
- Ideally, the solution can be used for both xdf2 and xdf3 and does not introduce version-specific behaviour.

### Decision

To handle the inconsistencies with the identifiers, each code list receives a new, unique identifier when imported.
These are then linked to the schemas via a many-to-many relationship.
The API will also work with the new identifiers, while still returning the existing genericode identifiers for convenience.

### Consequences

The solution is flexible enough to allow for easy sharing of existing code lists among multiple schemas.
Within the context of the project, code lists are only identified via this new, unique identifier, which
results in consistent behaviour between xdf2 and xdf3 without extra complexity.

The addition of a new identifier could potentially introduce some additional complexity when starting to work with the API.
However, we think that this effect will be more than offset by providing a simple, unique and version-independent way of working with code lists.

<a name="sqladmin"></a>

## 8. Use of sqladmin library

### Status

Accepted

### Context

Our FastAPI-based application requires an admin dashboard to perform CRUD operations on tokens and potentially other database tables.
Implementing an admin dashboard from scratch can be resource-intensive and deviate our focus from building the core application.
There are several libraries available that provide ready-to-use admin dashboards. Among these, the sqladmin library (https://github.com/aminalaee/sqladmin) promises a quick setup without extensive coding.

### Decision

We have decided to utilize the sqladmin library to set up our admin dashboard.

Benefits:
  - Rapid Development: sqladmin allows us to quickly set up an admin dashboard without the need for extensive coding.
  - Focus on Main Application: By using sqladmin, we can keep our development team focused on improving and building the main application, without being sidetracked by the intricacies of building an admin panel from scratch.
  - Extensibility: The library offers easy means to extend the dashboard and provide access to other tables in our database.
  - Convenience: sqladmin's user-friendly interface ensures that even non-developers can access and manage the data without complications.
  - Community and Maintenance: Having a library that is well-maintained ensures that we have fewer issues to manage, and the community support can be helpful for troubleshooting.

### Consequences

  - Dependency: Adopting sqladmin means we'll be dependent on it for updates and maintenance. If the library becomes deprecated or is no longer maintained, it may lead to issues in the future.
  - Customization Limitations: While sqladmin is extensible, there may be limitations when it comes to deep customizations. However, for our current needs, it seems sufficient.
  - Potential Learning Curve: While the library is user-friendly, there might be an initial learning curve for those unfamiliar with it.
