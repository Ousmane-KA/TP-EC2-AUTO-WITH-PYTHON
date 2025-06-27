# Fournisseur AWS et région de déploiement
provider "aws" {
  region = "eu-north-1"  # Région Stockholm (modifiable)
}

# Ressource EC2
resource "aws_instance" "example" {
  ami           = "ami-042b4708b1d05f512"            # ID de l'image AMI (Ubuntu, Amazon Linux, etc.)
  instance_type = "t3.micro"     # Type d'instance (ex: t3.micro)

  tags = {
    Name = "SRV-Linux-02"            # Nom de l'instance (tag AWS)
  }
}