# Hello-World: CircleCI & Snowflake

Simple CircleCI Workflow to demonstrate how to:

* Use CircleCI's Python 3.6.5 Docker Image
* Set environment variables
* Install Python dependencies and Snowflake connector
* Execute shell scripts
* Execute SQL command on Snowflake and fetch the result

Steps:

* Import your GitHub project into CircleCI
* Go to CircleCI's project settings -> Environment Variables and set up
`SF_USER` and `SF_PASSWORD` to be associated with your Snowflake account.
* Build the project and cross your fingers!
