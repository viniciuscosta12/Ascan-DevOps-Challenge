from flask import Flask, render_template_string
from colorama import init, Fore, Style
import random

# Inicializar colorama para suporte de cores
init()

app = Flask(__name__)

# Template HTML colorido e divertido
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Colorful Hello World</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .hello-container {
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            background-color: white;
        }
        .hello-text {
            font-size: 48px;
            font-weight: bold;
            transition: color 0.5s;
        }
    </style>
</head>
<body>
    <div class="hello-container">
        <div class="hello-text" style="color: {{ color }};">
            Hello, World! 🌍
        </div>
    </div>
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