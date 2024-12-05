from flask import Flask, render_template_string
from colorama import init, Fore, Style
import random

# Inicializar colorama para suporte de cores
init()

app = Flask(__name__)

# Template HTML interativo com animações e efeitos
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Interactive Hello World</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f4f8;
            transition: background-color 0.5s;
        }
        .container {
            text-align: center;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            background-color: white;
            max-width: 500px;
            width: 90%;
            transition: all 0.3s ease;
        }
        .hello-text {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
            transition: transform 0.3s, color 0.5s;
        }
        .interactive-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }
        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
        }
        .btn:hover {
            transform: scale(1.05);
        }
        #click-counter {
            margin-top: 15px;
            font-size: 18px;
            color: #666;
        }
        .emoji {
            transition: transform 0.3s ease;
        }
        .emoji:hover {
            transform: scale(1.5) rotate(20deg);
        }
    </style>
</head>
<body>
    <div class="container" id="main-container">
        <div class="hello-text" id="hello-text" style="color: {{ color }};">
            Hello, World! v1 <span class="emoji">🌍</span>
        </div>
        <div class="interactive-buttons">
            <button class="btn" style="background-color: #4CAF50; color: white;" onclick="changeColor()">Change Color</button>
            <button class="btn" style="background-color: #2196F3; color: white;" onclick="toggleBackground()">Toggle Background</button>
        </div>
        <div id="click-counter">Clicks: 0</div>
    </div>

    <script>
        let clickCount = 0;
        
        function changeColor() {
            const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FDCB6E', '#6C5CE7', '#FF8A5B'];
            const randomColor = colors[Math.floor(Math.random() * colors.length)];
            
            const helloText = document.getElementById('hello-text');
            helloText.style.color = randomColor;
            
            // Increment and update click counter
            clickCount++;
            document.getElementById('click-counter').textContent = `Clicks: ${clickCount}`;
        }
        
        function toggleBackground() {
            const body = document.body;
            const container = document.getElementById('main-container');
            
            body.style.backgroundColor = 
                body.style.backgroundColor === 'rgb(240, 244, 248)' ? '#e0e7f0' : '#f0f4f8';
            
            container.style.transform = 
                container.style.transform ? '' : 'rotate(5deg)';
            
            // Increment and update click counter
            clickCount++;
            document.getElementById('click-counter').textContent = `Clicks: ${clickCount}`;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def hello():
    # Gera uma cor aleatória para tornar cada visita única
    colors = [
        "#FF6B6B",  # Vermelho coral
        "#4ECDC4",  # Turquesa
        "#45B7D1",  # Azul claro
        "#FDCB6E",  # Amarelo dourado
        "#6C5CE7",  # Roxo
        "#FF8A5B"   # Laranja pêssego
    ]
    random_color = random.choice(colors)
    
    # Log colorido no terminal
    print(Fore.GREEN + "Alguém acessou a página!" + Style.RESET_ALL)
    print(Fore.CYAN + f"Cor gerada: {random_color}" + Style.RESET_ALL)
    
    return render_template_string(HTML_TEMPLATE, color=random_color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)