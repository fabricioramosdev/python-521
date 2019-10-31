pipeline{
    agent any;
     stages{
        stage('Preparation'){
            steps{
                echo "Preparando ..."
                steep 10;
            }
        }
        stage('Build'){
            steps{
                echo "Buildando ..."
                steep 10;
            }
        }
        stage('Resultados'){
            steps{
                echo "Finalizado o deploy ..."
                steep 10;
            }
        }
     }
}