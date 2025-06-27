# Importation des modules nécessaires
from flask import Flask, render_template, request  # Flask pour le web, render_template pour afficher les pages, request pour récupérer les données du formulaire
import subprocess  # Pour exécuter des commandes système (terraform)
from jinja2 import Template  # Pour générer dynamiquement le fichier Terraform depuis un modèle

# Initialisation de l'application Flask
app = Flask(__name__)

# Route d'accueil (formulaire HTML)
@app.route('/', methods=['GET'])
def index():
    # Affiche la page HTML du formulaire
    return render_template('form.html')

# Route qui traite le formulaire (POST)
@app.route('/create-instance', methods=['POST'])
def create_instance():
    # Récupération des données envoyées par le formulaire HTML
    instance_name = request.form['instance_name']  # Nom de l'instance
    ami_id = request.form['ami_id']                # ID de l'image AMI
    instance_type = request.form['instance_type']  # Type d'instance (t3.micro, etc.)

    # Lecture du modèle Terraform (fichier Jinja2)
    with open('terraform/main.tf.j2') as f:
        template = Template(f.read())  # Création d'un objet Template avec le contenu du fichier

    # Génération du fichier Terraform avec les valeurs du formulaire
    tf_content = template.render(
        instance_name=instance_name,
        ami_id=ami_id,
        instance_type=instance_type
    )

    # Écriture du fichier Terraform final prêt à être utilisé
    with open('terraform/main.tf', 'w') as f:
        f.write(tf_content)

    # Initialisation de Terraform dans le dossier 'terraform'
    subprocess.run(['terraform', 'init'], cwd='terraform')

    # Application automatique du plan Terraform sans confirmation manuelle
    subprocess.run(['terraform', 'apply', '-auto-approve'], cwd='terraform')

    # Retour d'un message de succès dans le navigateur
    return f"Instance EC2 '{instance_name}' lancée avec succès !"

# Lancement de l'application Flask si le fichier est exécuté directement
if __name__ == '__main__':
    app.run(debug=True)
