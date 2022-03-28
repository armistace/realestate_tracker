# Little App to track hyper local real estate prices

This app will eventually provide a simple web app to track and analyse real estate prices and a hyper local level

currently requires

mariadb

a user and database called realestate

Done
1. Data Design

Roadmap
1. Generate Flask route to update DB
2. Generate Flask route to analyse incoming information
    - including:
    - Expect Price vs Actual
    - Owneres Expectation vs Actual
    - Suburb Slicer
    - Rating Slicer
3. Use flask to generate a preview of the realestate.com link
4. Generate Flask grpc/rest api to push data to android app (TODO will be seperate repo)
5. input data