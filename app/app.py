from flask import Flask  # Flask creates a simple web server.
import redis  # Connects to Redis.

app = Flask(__name__)  # Creates the Flask app.
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Route for the homepage.
@app.route('/')
def counter():
    count = redis_client.incr('counter')  # Increment the counter in Redis.
    return f"Visitor Count: {count}"  # Show the visitor count on the webpage.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the app on port 5000.

