# MicroService
Applications exécutées sur différents pods.

Dans cet exercice on va générer des valeurs aléatoires qui seront stockées dans une base de données mysql.
Ensuite on recupéra les valeurs dans la base de données, qu'on va sauvegarder dans un fichier.
Les applications vont tourner sur des pods différents.
Nous allons construire des images docker, que nous allons déployer sur les pods.

Étape 1: construction des images 
Dans les dossiers avec le préfix `image`, ouvrez le fichier json `params` et entrez le <mot de pass> que vous souhaitez utiliser,
et le nom qu'aura votre base de donnée.

Exécutez les commandes suivantes, selon l'environnement sur lequel vous travaillez.
Nous partons du fait que vous avez un cluster minikube.

Linux:
`eval $(minikube docker-env)` -> cette commande est executée une seule fois

windows:
`minikube docker-env | Invoke-Expression` -> cette commande est executée une seule fois

Linux / windows: Dans chaque dossier avec le préfix image, exécutez les commandes suivantes:
`docker build -t "image-name" .`
`minikube image load "nom de l'image"`

Étape 2: Mot de passe en BASE64
Codez votre mot de passe enregistré dans le fichier json "params" en BASE64

Linux:
`echo -n "your_password" | base64`
windows:
`[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("your_password"))`

Sauvegardez le mot de passe dans le fichier `configYML\mysqldbserver.yml`,
dans la section `kind: Secret`

Étape 3: Appliquez les fichiers yaml
Dans le dossier `configYML`, nous avons 4 fichiers.
1) le fichier mysqldbserver.yml deploie un server mysql.

2) le fichier myDB.yml deploie une application qui crée notre base de donnée avec un tableau nommé measurements, un pod.

3) le fichier generator.yml crée une tache périodique qui exécute chaque 5 minutes, une application qui génère une valeur entre 37 et 38, sauvegardée dans notre tableau `measurements`,
dans notre base de donnée. Un fichier log est sauvegardée sur le volume du pod.

4) le fichier db_to_file crée une tache périodique qui exécute chaque 10 minutes, une application qui exporte les valeurs enregistrées dans la base de donnée,
vers un fichier. Un fichier log est sauvegardée sur le volume du pod.

# MicroService
Applications running on different pods.

In this exercise, we will generate random values ​​that will be stored in a MySQL database.
Then, we will retrieve the values ​​from the database and save them to a file.
The applications will run on different pods.
We will build Docker images, which we will deploy to the pods.

Step 1: Building the images
In the folders with the `image` prefix, open the `params` JSON file and enter the password you want to use,
and the name you want your database to have.

Run the following commands, depending on your environment.
We assume you have a Minikube cluster.

Linux:
`eval $(minikube docker-env)` -> this command is executed only once

Windows:
`minikube docker-env | Invoke-Expression` -> This command is executed only once.

Linux/Windows: In each folder with the `image` prefix, run the following commands:
`docker build -t "image-name"`
`minikube image load "image-name"`

Step 2: Base64 Password Encode your password stored in the "params" JSON file into Base64.

Linux: `echo -n "your_password" | base64`
Windows: `[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("your_password"))`

Save the password in the `configYML\mysqldbserver.yml` file,
in the "kind: Secret" section.

Step 3: Apply the YAML Files
In the `configYML` folder, there are 4 files.

1) The mysqldbserver.yml file deploys a MySQL server.

2) The myDB.yml file deploys an application that creates our database with an array named `measurements`, a pod.

3) The generator.yml file creates a periodic task that runs every 5 minutes, an application that generates a value between 37 and 38, saved in our `measurements` array,
in our database. A log file is saved on the pod's volume.

4) The db_to_file file creates a periodic task that runs every 10 minutes, an application that exports the values ​​recorded in the database,
to a file. A log file is saved on the pod's volume.


 
