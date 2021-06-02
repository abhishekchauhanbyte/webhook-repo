# Dev Assessment - Webhook Receiver


* Achieved output 
![Capture](https://github.com/abhishekchauhanbyte/webhook-repo/blob/master/app/img/webhoook_assign/Capture.PNG?raw=true)


*Database snip (mongodb atlas)
![database_snip_mongodb_atlas](https://github.com/abhishekchauhanbyte/webhook-repo/blob/master/app/img/webhoook_assign/database_snip_mongodb_atlas.PNG?raw=true)



Please use this repository for constructing the Flask webhook receiver.

*******************

## Setup

* Create a new virtual environment

```bash
pip install virtualenv
```

* Create the virtual env

```bash
virtualenv venv
```

* Activate the virtual env

```bash
source venv/bin/activate
```

* Install requirements

```bash
pip install -r requirements.txt
```

* Run the flask application (In production, please use Gunicorn)

```bash
python run.py
```

* The endpoint is at:

```bash
POST http://127.0.0.1:5000/webhook/receiver
```

You need to use this as the base and setup the flask app. Integrate this with MongoDB (commented at `app/extensions.py`)

*******************

