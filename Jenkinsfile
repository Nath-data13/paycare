pipeline {
    agent any  // Utilise n’importe quel agent Jenkins disponible

        stage('Construire l’image Docker') {
            steps {
                script {
                    docker.build('paycare.img')
                }
            }
        }
        stage('Lancer les tests') {
            steps {
                script {
                    docker.image('paycare.img').inside {
                        sh 'pytest tests/'  // Lance les tests dans le conteneur
                    }
                }
            }
        }

        stage('Exécuter l\'application') {
            steps {
                script {
                    // Arrête le conteneur s’il existe déjà
                    sh 'docker rm -f paycare-app || true'
                    // Lance l’application
                    sh 'docker run -d --name paycare-app -p 8090:8090 paycare.img'
                }
            }
        }
    }
