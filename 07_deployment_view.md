# Deployment View

The following text details the target architecture. REF and PROD are not available as of July 24th, 2023.

## Infrastructure Level 1

![Deployment View](./diagrams/Deployment_View.png "Deployment View")

Motivation  
This view provides information about the infrastructure and the processes required to move assets across nodes.

Quality and/or Performance Features  
Quality is assured via automated tests that are part of the Continuous Integration (CI) pipeline. Performance optimization is currently not a prime focus considering the small number of users and small amount of data.

Mapping of Building Blocks to Infrastructure  
The application is deployed to a single node - there is no architectural need to distribute execution or storage logic over several nodes.

## Infrastructure Level 2

### DEV

Development takes place on decentralized developer workstations. Local tests are executed as a first line of defense against coding errors. Collaboration is based on git.

### OpenCode

The central **git repository** is provided by [OpenCode](https://opencode.de), the open source repository of Germany's public administration maintained by Baden-Württemberg's Komm.ONE.

Gitlab has integrated **CI pipelines** that execute [tests from the code repository](https://gitlab.opencode.de/fitko/fim/schema-repository/-/tree/main/tests).

### TEST

This project utilizes resources from https://uber.space to allow for quick testing. With each successfull branch and CI based test, code is deployed to this node to allow for API and [GUI based](http://test.fim.uber.space) tests. API routes and database contents may change without notice.

### STAGING

This project utilizes resources from \[to be determined\] to allow for testing by external stakeholders. With each finished two week sprint, code is deployed to this node to allow for API and GUI based tests. API route changes are documented in the change log.

### PROD

This project utilizes resources from \[to be determined\] to provide production level quality and performance external stakeholders. With each finished milestone, code is deployed to this node to allow for API and GUI based access to FIM-Sammelrepository. API route changes are announced and will be documented in the change log.
