# quotify-backend

## Set up Locally
1. Clone Repo `git clone https://github.com/Quotify-Bot/quotify-backend.git`
2. Change directory `cd quotify-backend`
3. Install virtual environment `virtualenv env`
4. Activate environment  `env\Scripts\activate`
5. Install requirements `pip install -r requirements.txt`
6. Install pytorch cpu `pip install torch==1.7.1+cpu -f https://download.pytorch.org/whl/torch_stable.html`
7. Start the server `uvicorn main:app --host 0.0.0.0 --port 8080`


## Create Docker Image
1. `docker build -t <image_name>:<tag_name> .`


## Deploy to GCP
1. Login using gcloud CLI `	`
2. Tag the image in the correct format for deployment `docker tag <image_name>:<tag_name> gcr.io/<project_name>/<image_name>:<tag_name>`
3. Push to GCP container registry `docker push gcr.io/<project_name>/<image_name>:<tag_name>`
4. Go to GCP and deploy using cloud run
