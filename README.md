
---

# 📦 TP - Création Automatique d’une Instance EC2 avec Python & Terraform

---

## 🚀 Présentation

Ce projet permet de **créer automatiquement une instance EC2** AWS via une interface web simple développée avec **Flask (Python)** et en utilisant **Terraform** pour gérer l’infrastructure.

---

## 🧱 Fonctionnalités

* 📄 Formulaire web pour saisir le nom, choisir l’AMI et le type d’instance.
* ⚙️ Génération dynamique du fichier Terraform à partir d’un template Jinja2.
* 🔧 Exécution des commandes Terraform (`init`, `apply`) via Python.
* 🗑️ Option pour détruire l’instance EC2 (à ajouter si besoin).
* 📍 Région AWS fixée à `eu-north-1` (modifiable).

---

## 📁 Structure du projet

```
TP-EC2-AUTO-WITH-PYTHON/
├── app.py                     # Application Flask principale
├── templates/
│   └── form.html              # Formulaire HTML pour créer l’instance EC2
├── terraform/
│   ├── main.tf.j2             # Template Terraform (Jinja2)
│   └── variables.tf           # Variables Terraform (optionnel)
└── README.md                  # Ce fichier
```

---

## ⚙️ Prérequis

* Python 3.x
* Terraform installé et accessible en ligne de commande
* AWS CLI configuré avec tes identifiants AWS
* Modules Python : Flask, Jinja2 (installer via `pip install flask jinja2`)

---

## 🚀 Lancer le projet

1. **Cloner le dépôt** (ou copier les fichiers)

2. **Installer les dépendances Python**

```bash
pip install flask jinja2
```

3. **Configurer AWS CLI**

```bash
aws configure
```

4. **Lancer l’application Flask**

```bash
python app.py
```

5. **Ouvrir dans un navigateur**

```
http://127.0.0.1:5000/
```

6. **Remplir le formulaire et créer l’instance EC2**

---

## 🗑️ Supprimer l’instance

Dans le dossier `terraform/`, exécuter :

```bash
terraform destroy -auto-approve
```

---

## 🔧 Personnalisation

* Modifier la région AWS dans `main.tf.j2`
* Ajouter d’autres paramètres Terraform dans le template

---

## 📚 Ressources

* [Terraform](https://www.terraform.io/)
* [Flask](https://flask.palletsprojects.com/)
* [AWS CLI](https://aws.amazon.com/cli/)

---

## 🙋‍♂️ Auteur

*Ousmane KA*

---
