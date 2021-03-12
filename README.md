# quotify-backend

## About
API for the [Quotify webapp](https://github.com/Quotify-Bot/quotify-frontend) to generate quotes using a finetuned GPT2 model. The model can be downloaded from the [releases](https://github.com/Quotify-Bot/quotify-backend/releases/tag/v1.1) page. The backend was built using [FastAPI](https://fastapi.tiangolo.com/) and deployed with [Docker](https://www.docker.com/) on Google Cloud Platform.  

This was the best method we managed to find to deploy large models (>500MB) to the cloud. 

API Docs: https://quotify-engine-l6lhxur2aq-uc.a.run.app/docs

## Set up Locally
1. Clone Repo `git clone https://github.com/Quotify-Bot/quotify-backend.git`
2. Change directory `cd quotify-backend`
3. Install virtual environment `virtualenv env`
4. Activate environment  `env\Scripts\activate`
5. Install requirements `pip install -r requirements.txt`
6. Install pytorch cpu `pip install torch==1.7.1+cpu -f https://download.pytorch.org/whl/torch_stable.html`
7. Start the server `uvicorn main:app --host 0.0.0.0 --port 8080`

## Deploy to Google Cloud Platform (GCP)
1. Create docker image `docker build -t <image_name>:<tag_name> .`
1. Login using [gcloud CLI](https://cloud.google.com/sdk/docs/install) `gcloud auth login`
2. Tag the image in the correct format for deployment `docker tag <image_name>:<tag_name> gcr.io/<project_name>/<image_name>:<tag_name>`
3. Push to GCP container registry `docker push gcr.io/<project_name>/<image_name>:<tag_name>`
4. Go to GCP container registry and deploy using cloud run

