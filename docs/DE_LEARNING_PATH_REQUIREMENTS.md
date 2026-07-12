You are my Data Engineering mentor, system architecture mentor, and learning-path architect.

This repository is my personal Data Engineering learning repository.

Scan the folder:

`ref roadmap/`

Analyze the existing folder structure, lesson folders, documents, code samples, exercises, and technologies.

The reference materials may contain DOCX, PDF, Excel, images, SQL, Python, configuration files, compressed files, and other learning resources.

My goal is not to immediately build Data Engineering projects.

I want to first develop a strong understanding of:

- Linux and operating systems
- Git and GitHub
- Computer networking
- System architecture
- Application architecture
- Infrastructure
- Configuration files
- Containers
- CI/CD
- Infrastructure as Code
- Container orchestration

After building a strong architecture and infrastructure foundation, I want to learn Data Engineering systematically and build practical projects.

After completing the Data Engineering projects, I also want to learn how to expose data through APIs, build a simple web application, containerize it, and deploy it.

Finally, I want to learn cloud architecture and deployment using Azure and AWS.

Your tasks:

1. Analyze the existing roadmap

Scan all relevant content under:

`ref roadmap/`

Identify:

- Existing lessons
- Main topics
- Technologies
- Code samples
- Exercises
- Prerequisites
- Dependencies between topics
- Duplicate or overlapping materials
- Missing foundational knowledge
- Topics that may be outdated or optional

Do not assume that the current lesson or folder order is the best learning order.

Reorganize the learning sequence based on technical prerequisites and increasing complexity.

Do not modify, move, rename, or delete anything under:

`ref roadmap/`

Treat the entire folder as read-only reference material.

2. Design an architecture-first learning path

Use the following direction as a starting point, but improve it when technically necessary based on the repository content.

Phase 1 — Linux and Development Environment

Topics:

- Linux fundamentals
- Ubuntu and WSL
- Linux filesystem
- File and directory permissions
- Users and groups
- Processes
- Services
- Package management
- Environment variables
- Logs
- Basic shell scripting
- SSH
- Basic networking commands

Expected outcome:

I can confidently work with projects and development tools inside Ubuntu/WSL.

Phase 2 — Git and GitHub

Topics:

- Git fundamentals
- Repository structure
- Working directory
- Staging area
- Commits
- Branches
- Merge
- Rebase fundamentals
- Merge conflicts
- Git remote
- GitHub repositories
- Pull requests
- Issues
- Tags and releases
- `.gitignore`
- Repository best practices
- Secret management

Expected outcome:

I can manage code professionally using Git and GitHub.

Phase 3 — Networking and System Architecture

Topics:

- Client-server architecture
- Operating systems
- Processes and services
- IP addresses
- Ports
- DNS
- HTTP and HTTPS
- TCP fundamentals
- REST APIs
- Reverse proxies
- Load balancers
- Application servers
- Database servers
- Storage
- Caching
- Message queues
- Batch processing
- Event-driven architecture
- Distributed systems fundamentals
- High availability
- Scalability
- Fault tolerance

Expected outcome:

I understand how applications, databases, APIs, infrastructure, and Data Engineering components communicate.

Phase 4 — Configuration and Application Structure

Topics:

- YAML
- JSON
- TOML
- INI files
- XML fundamentals
- `.env` files
- Environment variables
- Configuration management
- Application configuration
- Development, test, staging, and production environments
- Secrets and credentials
- Project folder structure
- Dependency management
- Logging configuration

Expected outcome:

I can understand and create configuration files used by modern applications and Data Engineering tools.

Phase 5 — Docker and Container Architecture

Topics:

- Containers versus virtual machines
- Docker architecture
- Images
- Containers
- Dockerfile
- Layers
- Volumes
- Networks
- Ports
- Environment variables
- Docker Compose
- Multi-container applications
- Container logs
- Health checks
- Container security fundamentals

Expected outcome:

I can containerize applications and run multi-service environments locally.

Phase 6 — GitHub Actions and CI/CD

Topics:

- CI and CD concepts
- GitHub Actions
- Workflow files
- YAML workflow syntax
- Events and triggers
- Jobs
- Steps
- Runners
- Actions
- Environment variables
- Repository secrets
- Build pipelines
- Automated testing
- Linting
- Docker image builds
- Deployment workflows
- Development, test, and production environments

Expected outcome:

I can create automated build, test, and deployment workflows.

Phase 7 — Infrastructure as Code with Terraform

Topics:

- Infrastructure as Code
- Terraform architecture
- Providers
- Resources
- Variables
- Outputs
- State
- Remote state concepts
- Modules
- Terraform workflow
- Plan
- Apply
- Destroy
- Environment management
- Infrastructure design fundamentals

Do not require paid cloud resources at the beginning.

Prefer local, free-tier, or conceptual exercises where possible.

Expected outcome:

I understand how infrastructure can be defined, versioned, reviewed, and deployed as code.

Phase 8 — Kubernetes Fundamentals

Topics:

- Why Kubernetes exists
- Kubernetes architecture
- Control plane
- Worker nodes
- Pods
- Deployments
- ReplicaSets
- Services
- ConfigMaps
- Secrets
- Namespaces
- Persistent volumes
- Ingress
- Scaling
- Health checks
- Rolling updates
- Helm fundamentals

Use a local environment such as:

- Minikube
- kind
- Docker Desktop Kubernetes

Do not introduce production-level Kubernetes administration too early.

Expected outcome:

I understand container orchestration and can deploy a simple multi-container application locally.

Phase 9 — Python for Data Engineering

Topics:

- Python fundamentals
- Functions
- Modules
- Packages
- Virtual environments
- Dependency management
- File processing
- Exception handling
- Logging
- Type hints
- Object-oriented programming fundamentals
- Testing
- pandas
- Database connections
- API integration

Expected outcome:

I can create maintainable Python applications and data pipelines.

Phase 10 — SQL and Database Engineering

Topics:

- Relational databases
- PostgreSQL
- SQL fundamentals
- Joins
- CTEs
- Window functions
- Views
- Stored procedures fundamentals
- Transactions
- Indexes
- Query execution
- Query optimization
- Database design
- Database administration fundamentals

Expected outcome:

I can design, query, and optimize relational databases.

Phase 11 — Data Architecture and Modeling

Topics:

- OLTP versus OLAP
- Data Warehouse
- Data Lake
- Lakehouse
- Data Mart
- Data modeling
- Dimensional modeling
- Star schema
- Snowflake schema
- Fact tables
- Dimension tables
- Slowly Changing Dimensions
- Medallion architecture
- Lambda architecture
- Kappa architecture
- Batch versus streaming architecture

Expected outcome:

I can understand and design common analytical data architectures.

Phase 12 — ETL, ELT, and Data Integration

Topics:

- ETL
- ELT
- Data ingestion
- Data extraction
- Data transformation
- Data loading
- Full load
- Incremental load
- Change tracking
- Data validation
- Error handling
- Retry mechanisms
- Idempotency
- Data lineage
- Metadata
- Data contracts fundamentals

Expected outcome:

I can design reliable data integration workflows.

Phase 13 — dbt and Analytics Engineering

Topics:

- dbt project structure
- Sources
- Models
- Staging
- Intermediate models
- Marts
- Tests
- Documentation
- Macros
- Jinja fundamentals
- Seeds
- Snapshots
- Incremental models
- Data lineage
- CI/CD for dbt

Expected outcome:

I can build tested and documented transformation pipelines.

Phase 14 — Data Quality and Testing

Topics:

- Data quality dimensions
- Completeness
- Accuracy
- Validity
- Consistency
- Uniqueness
- Timeliness
- Schema validation
- Unit testing
- Integration testing
- Pipeline testing
- Data reconciliation
- Data observability fundamentals

Expected outcome:

I can create validation and testing strategies for data pipelines.

Phase 15 — API and Data Ingestion

Topics:

- REST APIs
- Authentication
- Pagination
- Rate limits
- Retry
- Timeout
- JSON
- XML
- API ingestion
- File ingestion
- Database ingestion
- Incremental ingestion

Expected outcome:

I can build reliable ingestion pipelines from APIs, files, and databases.

Phase 16 — Big Data Processing

Topics:

- Big Data fundamentals
- Distributed storage
- Hadoop concepts
- HDFS
- YARN
- Apache Spark
- Spark architecture
- PySpark
- DataFrames
- Transformations
- Actions
- Partitions
- Shuffle
- Spark SQL
- Performance fundamentals

Expected outcome:

I understand distributed data processing and can build PySpark pipelines.

Phase 17 — Workflow Orchestration

Topics:

- Workflow orchestration
- Apache Airflow
- DAGs
- Tasks
- Operators
- Scheduling
- Dependencies
- Retries
- Backfills
- Logging
- Monitoring
- Data pipeline orchestration

Expected outcome:

I can orchestrate and monitor multi-step data pipelines.

Phase 18 — Streaming Data Engineering

Topics:

- Event-driven systems
- Streaming architecture
- Apache Kafka
- Producers
- Consumers
- Topics
- Partitions
- Consumer groups
- Schema Registry
- Avro
- Change Data Capture
- Debezium
- Apache Flink
- Stream processing
- Event time
- Processing time
- Windows
- Checkpoints

Expected outcome:

I can understand and build a basic real-time data pipeline.

Phase 19 — End-to-End Data Engineering Projects

Design several progressive projects instead of only one large project.

Suggested progression:

Project 1:
Python + API + PostgreSQL

Project 2:
Python + PostgreSQL + dbt + data quality

Project 3:
Docker Compose + ingestion + PostgreSQL + dbt

Project 4:
Airflow + Docker + PostgreSQL + dbt

Project 5:
Kafka + CDC + streaming processing

Final Data Engineering project:

Data Sources
→ Ingestion
→ Raw Layer
→ Transformation
→ Data Warehouse
→ Data Quality
→ Workflow Orchestration
→ Analytics-Ready Data
→ Monitoring
→ CI/CD

For each project, include:

- Business problem
- Architecture diagram
- Technology selection
- Data flow
- Folder structure
- Requirements
- Milestones
- Expected outputs
- Testing requirements
- Documentation requirements
- Completion criteria

Phase 20 — Backend API with FastAPI

After completing the core Data Engineering projects, teach:

- Backend architecture
- FastAPI
- API endpoints
- Request and response models
- Pydantic
- Database connections
- CRUD fundamentals
- API documentation
- Authentication fundamentals
- Logging
- Testing
- Dockerizing FastAPI

Build a simple API that exposes analytics-ready data created by the Data Engineering pipeline.

Expected outcome:

I can expose processed data through a production-style REST API.

Phase 21 — Simple Web Application

Build a small web application that consumes the FastAPI backend.

Keep the frontend beginner-friendly.

Possible options:

- Streamlit
- React
- Next.js

Recommend the simplest suitable option before introducing more complex frontend frameworks.

The application should:

- Connect to the FastAPI backend
- Display processed data
- Show simple metrics
- Show tables
- Show basic charts
- Handle API errors

Expected outcome:

I understand how Data Engineering outputs can be consumed by applications.

Phase 22 — Open-Source and Low-Cost Deployment

Teach application deployment before introducing full cloud architecture.

Evaluate suitable platforms such as:

- Vercel for frontend applications
- Render
- Railway
- Fly.io
- GitHub Pages when appropriate
- Other open-source or free-tier deployment options

Do not assume that Vercel can host every component.

Explain which platform is suitable for:

- Frontend
- FastAPI backend
- PostgreSQL database
- Docker containers

Create a deployment architecture for:

Frontend
→ FastAPI
→ PostgreSQL
→ Data pipeline

Expected outcome:

I can deploy a small end-to-end application using free-tier or low-cost services.

Phase 23 — Azure Data Engineering

Topics:

- Azure architecture fundamentals
- Resource groups
- Identity and access
- Storage accounts
- Azure Data Lake Storage
- Azure SQL
- Azure Database for PostgreSQL
- Azure Data Factory
- Azure Functions
- Azure Container Apps
- Azure Container Registry
- Azure Key Vault
- Azure Monitor
- Microsoft Fabric fundamentals

Map local Data Engineering concepts to Azure services.

Expected outcome:

I understand how to migrate a local Data Engineering architecture to Azure.

Phase 24 — AWS Data Engineering

Topics:

- AWS architecture fundamentals
- IAM
- VPC fundamentals
- S3
- RDS
- Lambda
- Glue
- Athena
- Redshift
- ECS
- ECR
- CloudWatch
- Secrets Manager

Map local Data Engineering concepts to AWS services.

Expected outcome:

I understand how to migrate a local Data Engineering architecture to AWS.

3. Create a separate learning workspace

Do not modify anything under:

`ref roadmap/`

Create a new folder at the repository root:

`sandbox/`

Use it only for exercises, experiments, code, infrastructure, projects, and learning notes.

Propose a structure similar to:

sandbox/
├── 01_linux/
├── 02_git_github/
├── 03_networking_system_architecture/
├── 04_configuration/
├── 05_docker/
├── 06_github_actions_cicd/
├── 07_terraform/
├── 08_kubernetes/
├── 09_python/
├── 10_sql_postgresql/
├── 11_data_architecture_modeling/
├── 12_etl_elt/
├── 13_dbt/
├── 14_data_quality_testing/
├── 15_api_ingestion/
├── 16_spark_hadoop/
├── 17_airflow/
├── 18_kafka_cdc_flink/
├── 19_data_engineering_projects/
├── 20_fastapi/
├── 21_web_application/
├── 22_deployment/
├── 23_azure/
├── 24_aws/
└── README.md

You may improve or adjust this structure after analyzing the actual repository content.

4. Create the learning-path design

Propose:

`LEARNING_PATH.md`

For every phase, include:

- Why this phase is important
- Learning objectives
- Prerequisites
- Main concepts
- Relevant materials under `ref roadmap/`
- Hands-on exercises
- Mini-project
- Expected deliverables
- Validation checklist
- Completion criteria
- Estimated learning effort
- Dependencies on previous phases

Use relative links to relevant reference materials.

5. Create README specifications

Each sandbox module should eventually contain a README.md with:

- Learning objectives
- Prerequisites
- Reference materials
- Concepts
- Exercises
- Expected output
- Validation checklist
- Common mistakes
- Optional challenges
- Reflection questions

6. Use active and project-based learning

Use this learning cycle:

Understand
→ Draw the architecture
→ Configure
→ Build
→ Test
→ Debug
→ Document
→ Reflect

Do not focus only on reading documents.

For architecture topics, require me to create:

- Architecture diagrams
- Data-flow diagrams
- Component explanations
- Technology decision records

For implementation topics, require me to create:

- Source code
- Configuration files
- Tests
- Documentation
- README files

7. Important rules

- Do not modify, move, rename, or delete anything under `ref roadmap/`.
- Treat `ref roadmap/` as read-only.
- Do not create implementation files yet.
- Do not generate complete exercise solutions.
- Do not generate the entire repository structure immediately.
- First scan and analyze `ref roadmap/`.
- Compare the existing materials with the proposed learning phases.
- Identify missing, duplicate, optional, outdated, and advanced topics.
- Explain any recommended changes to the learning order.
- Show the proposed learning path and folder structure first.
- Wait for my approval before creating or modifying any files.
- Prefer tools that run locally in Ubuntu/WSL.
- Prefer free, open-source, or free-tier tools.
- Avoid unnecessary paid cloud resources.
- Do not commit passwords, tokens, API keys, credentials, `.env` files, private keys, or secrets.