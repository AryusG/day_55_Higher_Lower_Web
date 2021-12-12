from flask import Flask
from higher_lower import HigherLower
import random

server = Flask(__name__)
hl = HigherLower()
answer = hl.answer
# check if answer is correct -> if correct restart new game in decorator function


happy_gifs = ['https://media.giphy.com/media/Ch0JvNvkk7PH2/giphy.gif', 'https://media.giphy.com/media/13ByqbM0hgfN7y/giphy-downsized-large.gif',
'https://media.giphy.com/media/KtyTa7XH5ueJLYwmaG/giphy-downsized-large.gif', 'https://media.giphy.com/media/U2ii5GIzMGU3m/giphy.gif']

sad_gifs = ['https://media.giphy.com/media/HSvpy6Jk396SI/giphy.gif', 'https://media.giphy.com/media/ySM2PakMSmw7u/giphy.gif', 'https://media.giphy.com/media/3o7WTutp8jXuC9IUMg/giphy.gif', 
'https://media.giphy.com/media/saJYuwjsF8Kfm/giphy.gif']

@server.route("/")
def main():
    return "<h1 style='text-align:center'>Guess a number between 0 - 9</h> \
        <img src='https://media.giphy.com/media/JdFEeta1hLNnO/giphy.gif'>"

@server.route("/<int:guess>")
def tries(guess):
    sad_idx = random.randint(0, len(sad_gifs) - 1)
    happy_idx = random.randint(0, len(happy_gifs) - 1)

    if guess > answer:
        return f"<h1 style='color: red'>Wrong! {guess} is too high!</h> \
            <img src={sad_gifs[sad_idx]}>"
    if guess < answer:
        return f"<h1 style='color: orange'>Wrong! {guess} is too low!</h> \
            <img src={sad_gifs[sad_idx]}>"
    else:
        
        return f"<h1 style='color: green'>Congratulations! {guess} is the right number!</h> \
            <img src={happy_gifs[happy_idx]}>"