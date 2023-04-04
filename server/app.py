#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    query = Animal.query.filter(Animal.id == id).first()
    return f'''
    <ul>
    <ul>ID: {query.id}</ul>
    <ul>Name: {query.name}</ul>
    <ul>Species: {query.species}</ul>
    <ul>Zookeeper: {query.zookeeper_id}</ul>
    <ul>Enclosure: {query.enclosure_id}</ul>
    '''

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    query = Zookeeper.query.filter(Zookeeper.id == id).first()
    animals = str()
    for a in query.animals:
        animals+=f'<ul>Animal: {a.name}</ul>'
    return f'''
    <ul>ID: {query.id}</ul>
    <ul>Name: {query.name}</ul>
    <ul>Birthday: {query.birthday}</ul>
    {animals}
    '''

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    query = Enclosure.query.filter(Enclosure.id == id).first()
    animals = str()
    for a in query.animals:
        animals+=f'<ul>Animal: {a.name}</ul>'
    return f'''
    <ul>ID: {query.id}</ul>
    <ul>Environment: {query.environment}</ul>
    <ul>Open to Visitors: {query.open_to_visitors}</ul>
    {animals}
    '''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
