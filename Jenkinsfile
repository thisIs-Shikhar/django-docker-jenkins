node {
    // git credentialsId: 'private-key', url: 'git@github.com:by-sabbir/django-docker-jenkins.git'
    checkout scm
    try {

        stage ('Login to Newroz Private Repository') {
            withEnv(["DOCKER_USER=${DOCKER_USER}",
                     "DOCKER_PASSWORD=${DOCKER_PASSWORD}"]) {
                sh "make login "
                sh "curl -X POST -H 'Content-Type: application/json' -d '{\"chat_id\": \"-1001556850823\", \"text\": \"Started ${JOB_NAME}-${BUILD_NUMBER}\", \"disable_notification\": true}' https://api.telegram.org/bot1750146504:AAE5lT-GQNVtEF48xQwH3IvecZa8WrytYY8/sendMessage"
            }
        }
        
        stage ('Run unit/integration tests'){
            sh 'make test'
            sh "curl -X POST -H 'Content-Type: application/json' -d '{\"chat_id\": \"-1001556850823\", \"text\": \"Test Results: ${RUN_TESTS_DISPLAY_URL}\", \"disable_notification\": False}' https://api.telegram.org/bot1750146504:AAE5lT-GQNVtEF48xQwH3IvecZa8WrytYY8/sendMessage"
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
            sh "curl -X POST -H 'Content-Type: application/json' -d '{\"chat_id\": \"-1001556850823\", \"text\": \"Pipeline Completed: ${RUN_ARTIFACTS_DISPLAY_URL} for logs\", \"disable_notification\": true}' https://api.telegram.org/bot1750146504:AAE5lT-GQNVtEF48xQwH3IvecZa8WrytYY8/sendMessage"
        }
    }
    
    finally {
        stage ('Collect Test Reports') {
            junit '**/reports/*.xml'
        }
        stage ("cleanup and logout"){
            sh 'make clean'
            sh 'make logout'
        }
    }
   
}