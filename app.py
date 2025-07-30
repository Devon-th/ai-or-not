from flask import Flask, render_template

app = Flask(__name__)

lives = 3
images = {
    'static/ai/plane.png': 'Boeing jet lands after "Catastrophic" structural failure in wing', # images
    'static/ai/flower.png': 'Rare "Rainbow Bloom" Flower Discovered by Nature Enthusiast in Amazon, Emitting Previously Unknown Light Frequencies',
    'static/ai/roman.png': "Archaeologists Astonished after Discovery of Roman-era Mosaic in Woman's Backyard",
    'static/ai/chair.png': 'Company introduces monthly subscription for heated office chairs',
    'static/ai/tip.png': 'Self-Checkout Lanes Begin Asking for Tips at All Walmart Stores',
    'static/real/radioactive-wasps.png': 'Radioactive wasp nest found at site where US once made nuclear bombs',
    'static/real/ground-squirrel.png': 'Ground Squirrels Are Taking Over a North Dakota City and Officials Are Not Amused',
    'static/real/petroglyphs.png': 'Mystery over 500-year-old petroglyphs that have washed up on a beach',
    'static/real/.png': '',
    'static/real/.png': '',
}
is_real = [
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    True,
    True,
]

#def game_start():
#    while lives > 0:

def game_reset():
    lives = 3


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def game_play():
    #game_start()
    return render_template('game_page.html')

if __name__ == '__main__':
    app.run(debug=True)