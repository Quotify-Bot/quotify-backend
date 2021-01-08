# quotify-backend

## Set up Locally
1. Clone Repo `git clone https://github.com/Quotify-Bot/quotify-backend.git`
2. Change directory `cd quotify-backend`
3. Install virtual environment `virtualenv env`
4. Activate environment  `env\Scripts\activate`
5. Install requirements `pip install -r requirements.txt`
6. Install pytorch cpu `pip install torch==1.7.1+cpu -f https://download.pytorch.org/whl/torch_stable.html`
7. Start the server `uvicorn main:app --host 0.0.0.0 --port 8080`
