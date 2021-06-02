from app import create_app
from waitress import serve
import time

app=create_app()

if __name__=='__main__':
    # serve(app)                 //for production purpose use waitress
    #                              command->waitress-serve --port=<running-port> myapp:api
    app.run(debug=True)
    time.sleep(15)