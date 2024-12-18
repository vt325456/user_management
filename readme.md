

# The User Management System Final Project:🎉✨🔥

## Introduction: Buckle Up for the Ride of a Lifetime 🚀🎬

Welcome to the User Management System project - an epic open-source adventure crafted by the legendary Professor Keith Williams for his rockstar students at NJIT! 🏫👨‍🏫⭐ This project is your gateway to coding glory, providing a bulletproof foundation for a user management system that will blow your mind! 🤯 You'll bridge the gap between the realms of seasoned software pros and aspiring student developers like yourselves. 

## Goals and Objectives: Unlock Your Coding Superpowers 🎯🏆🌟

## Submission: 📝✏️📈

1. **Reflection Document**: A reflection document is added with the details of what i have done and listed the learning outcomes from the project I have made.Included the links to the closed issues for the **5 QA issues, 10 NEW tests, and 2 Features**.After successfully deploying the project to DockerHub I have included a link to my Docker repository in the document.📄🔗💥

2. **Commit History**: I have added valid commits for everything I have done and I have followed the industry practices to commit the code only when its working and I am confident. Every issue i have addressed have a branch and once everything is working fine then i have merged the changes to the main branch for deployment. 💻🔄🔥

3. **Deployability**: My project is completely deployed on DockerHub and it passes all the automated tests on the GitHub actions. Added New Test Cases for pytest and all those are working fine on the gitHub Actions.

4. **GitHUB Repository Link**: [User Management Final Project](https://github.com/vt325456/user_management)

5. **DockerHub Link**: [DockerHub Deployed Project](https://hub.docker.com/repository/docker/vt325/user_management/general)

6. **Reflection Document Link**: [Reflection Document](./IS601_FINALPROJECT_VT325.docx)

## Managing the Project Workload: Stay Focused, Stay Victorious ⏱️🧠⚡

1. **Feature Implementation**: I have selected features from the [given features list](features.md). I have worked on below features like [User Search and Filtering](https://github.com/vt325456/user_management/issues/9) and [QR Code Generation User Invites with Minio](https://github.com/vt325456/user_management/issues/6). 
I gained a solid understanding of using FastAPI to design APIs,including how to handle requests, dependencies,and connect logic.Implementing RESTful endpoints that follow industry standards like BREAD and HATEOAS was another aspect of my work.I was able to manage asynchronous sessionsunderstand connection poolingand design and implement normalised relational database schemas using SQLAlchemy ORM.I gained experience in using Pydantic models for API input validation and response serialization,as well as advanced SQLAlchemy querying techniques including joins, filters, and pagination.Creating QR codes using the qrcode package,adding custom parameters, and safely encoding user data with base64 all helped me expand my skill set. I also solved difficult technical issues with database transaction management, base64 encoding, and matching SQLAlchemy models with Pydantic schemas. Debugging complicated issues and testing API functioning in a variety of scenarios—including simulating practical uses and incorrect input handling—improved my analytical skills. I have worked on the searching and filtering as well to learn more about these functionality implementations.

2. **Quality Assurance (QA)**🔍🔬: 
I have Raised Issues on the project are below:

[Bug - Profile picture validation not present](https://github.com/vt325456/user_management/issues/5)
When testing the APIs in Swagger URL , The create user API end point is creating users even when the profile_picture_url is not in an image format.

[Bug - Dependency issues in Image Scanning with Vulnerabilities](https://github.com/vt325456/user_management/issues/3)
While the docker scan step is being done the docker image push is failed due to vulnerabilities of High and Critical.

[Bug - Email Verification without RoleBased approach](https://github.com/vt325456/user_management/issues/4)
The verify_email API is using token to verify the email which is successful for every user who is an AUTHENTICATED user. This is not correct for the users who are ANONYMOUS or in higher positions.

[Bug - Docker Build Failure](https://github.com/vt325456/user_management/issues/2)
The Docker Build is failing because 

[Bug - Mismatching Nickname](https://github.com/vt325456/user_management/issues/1)
When we run the create user API the nickname that is given in the API request is not the same that is stored in the database.


3. **Test Coverage Improvement**: Reviewed the existing test suite. Created 10 additional tests to cover edge cases, error scenarios, and important functionalities related to your chosen feature. Increased the test coverage by adding new test cases for the features I have worked on. ✅🧪

5. **Maintain a Working Main Branch**: Throughout the project, I have ensured always to have a working main branch deploying to Docker like a well-oiled machine. This will prevent any last-minute headaches and ensure a smooth submission process. 😊🚢⚓

## Project Setup  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/vt325456/user_management.git
   cd user_management  
   ```  

2. **Run Docker Containers**  
   ```bash  
   docker-compose up --build -d  
   ```  

3. **Run Migrations and Start Server**  
   ```bash  
   alembic upgrade head  
   uvicorn app.main:app --reload  
   ```  

4. **Access the Application**  
   - API Documentation: [http://localhost/docs](http://localhost/docs)  

---

