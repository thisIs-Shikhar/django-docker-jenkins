node {
    // git credentialsId: 'private-key', url: 'git@github.com:by-sabbir/django-docker-jenkins.git'
    checkout scm
    try {

        stage ("notify") {
            sh "curl -X POST -H 'Content-Type: application/json' -d '{\"chat_id\": \"-1001556850823\", \"text\": \"Started Building App\", \"disable_notification\": true}' https://api.telegram.org/bot1750146504:AAE5lT-GQNVtEF48xQwH3IvecZa8WrytYY8/sendMessage"
        }
        stage ('Login to Newroz Private Repository') {
            withEnv(["DOCKER_USER=${DOCKER_USER}",
                     "DOCKER_PASSWORD=${DOCKER_PASSWORD}"]) {
                sh "make login "
                
            }
        }
        
        stage ('Run unit/integration tests'){
            sh 'make test'    
        }
        
        
        stage ('Building Project') {
            sh 'make build'
        }
        
        
        stage ('Project Release') {
            sh 'make release'
        }
        stage ('Tag and Publish release image') {
            sh 'make tag latest \$(git rev-parse --short HEAD) \$(git tag --points-at HEAD)'
            sh 'make buildtag master \$(git tag --points-at HEAD)'
            sh "make publish"
            sh "curl -X POST -H 'Content-Type: application/json' -d '{\"chat_id\": \"-1001556850823\", \"text\": \"App Released to Newroz Docker repo\", \"disable_notification\": true}' https://api.telegram.org/bot1750146504:AAE5lT-GQNVtEF48xQwH3IvecZa8WrytYY8/sendMessage"
        }
    }
    
    finally {
        stage ('collect test reports') {
            stage "cleanup"
            sh 'make clean'
            sh 'make logout'
        }
        sh "curl -X POST -H 'Content-Type: application/json' -d '{\"chat_id\": \"-1001556850823\", \"text\": \"Deployed App\", \"disable_notification\": true}' https://api.telegram.org/bot1750146504:AAE5lT-GQNVtEF48xQwH3IvecZa8WrytYY8/sendMessage"
    }
    
}