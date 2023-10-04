from dotenv import dotenv_values

ENV = dotenv_values()

# ENV VARIABLES
SECRET_KEY = ENV['SECRET_KEY']
HOST = ENV['HOST']
PORT = ENV['PORT']
USER = ENV['USER']
PASSWORD = ENV['PASSWORD']
DATABASE = ENV['DATABASE']