
## About The Application

This is a simple python flask API application that able to request github statistic from one or more github repositories, as long the repos are public.

The application are made using python, with predefined connection for git statistic only to github (still changeable under the util -> backend.py code). And it will generate the report into csv file and will be created under result -> .csv file. 

The application is Docker ready, with requirements added and running using docker-compose command.

On top of that the application is also enable to send the csv report onto S3 buckets. You can just add the secret key and target bucket name under .app.env file and update accordingly.

## How To Run The Application

### Run as Docker

1. Run Docker using docker-compose
   ```sh
   docker-compose up
   ```

2. The application are using port 5100, make sure the port is not occupied (or you can change it inside .app.env file)

3. Once the container is running, use Postman / API testing tools to check the API.

* API url  : http://localhost:5100/api/git_status
* Method   : POST
* API body :
   ```sh
   {
	"repository" : ["aa/bb","bimanata/sampletestaah"],
	"output" : "csv"
    }
    ```
* Repository name format: orgname/repository or username/repository
* output type csv and s3 

4. Output input are csv if you want to generate it only to local folder, or using S3 if you want to push it to S3 bucket (access key and bucket name are provided by yourself)

### Run as Python

#### Optional
You can run the Python dependencies library first before run the python application. You can using pip to install it
   ```sh
   pip install -r requirements.txt
   ```

1. Run application using Python command
   ```sh
   python flask_app.py
   ```

2. The application are using port 5100, make sure the port is not occupied (or you can change it inside .app.env file)

3. Once the application is running, use Postman / API testing tools to check the API.

* API url  : http://localhost:5100/api/git_status
* Method   : POST
* API body :
   ```sh
   {
	"repository" : ["aa/bb","bimanata/sampletestaah"],
	"output" : "csv"
    }
    ```
* Repository name format: orgname/repository or username/repository
* output type csv and s3 

4. Output input are csv if you want to generate it only to local folder, or using S3 if you want to push it to S3 bucket (access key and bucket name are provided by yourself)
