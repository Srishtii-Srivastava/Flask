from flask import Flask

app = Flask(__name__,instance_relative_config=True)

#load default config
app.config.from_object('config.default')

#load config from instance folder
app.config.from_pyfile('config.py')

#get environment using env variable 
app.config.from_envvar('APP_CONFIG_FILE')

if __name__ == "__main__":
    app.run()