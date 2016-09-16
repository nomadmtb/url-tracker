# Run the test server with this file here...
from app import app
#app.run(host='0.0.0.0', port=8080, debug=False)

app.run(
    host=app.config['SERVER_NAME'].split(':')[0],
    port=int(app.config['SERVER_NAME'].split(':')[1]),
    debug=app.config['DEBUG']
)
