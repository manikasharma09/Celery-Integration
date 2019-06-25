# Celery-Integration
Celery Integration with Redis as message broker.
To define an async task, simply import and add the decorator @shared_taskto each method or function.
By adding @shared_task decorator, you method can now run asynchronously, but it doesn’t run naturally. We have to call the method in a way telling it to run asynchronously. To do so, simply call your method with the suffix apply_async() or delay() .
Make sure your Redis is up and running. Run redis_server to start your server if you are running it in your local machine. You can also run redis_cli to attempt connection to your Redis server.
