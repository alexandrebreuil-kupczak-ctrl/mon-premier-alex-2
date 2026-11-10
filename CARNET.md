# 📒 Mon carnet de bord

**Nom :** _(à compléter)_

**Prénom :** Alexandre

**Adresse de mon site :** _(à compléter après création/configuration du site PythonAnywhere)_

> Les réponses ci-dessous sont des réponses de référence basées sur le code et les notions de l’atelier. Les observations qui dépendent de votre navigateur, de votre déploiement ou des journaux sont indiquées comme telles : vérifiez-les pendant les exercices.

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Le code source est conservé sur GitHub et une copie déployée s’exécute sur le serveur PythonAnywhere. Le navigateur reçoit la réponse du serveur.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Son navigateur se connecte au serveur par Internet et reçoit la page à afficher ; le programme du site tourne sur le serveur, pas sur son ordinateur.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Le domaine est `www.google.com` et le chemin est `/maps`.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ La ressource demandée n’a pas été trouvée (404). C’est la réponse du serveur, affichée par le navigateur.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Flask/Python peut échouer au démarrage lors de l’enregistrement de la deuxième fonction/route avec ce nom, avec une erreur de correspondance de vue ou de syntaxe selon la façon dont le doublon est écrit.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie du texte HTML ; le navigateur interprète les balises et rend la page visuelle.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ `<h1>` marque le titre principal, `<p>` un paragraphe, `<ul>` une liste non ordonnée et `<li>` un élément de cette liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ Le navigateur fait une autre requête vers l’adresse externe de l’image et la télécharge depuis ce serveur.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Cela sépare la logique et la présentation : chacun peut travailler et modifier sa partie plus facilement.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Le serveur les remplace avec Jinja avant d’envoyer la page. Avec « Afficher le code source », on voit la valeur finale et non les expressions `{{ ... }}`.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ HTML décrit la structure et le contenu ; CSS règle l’apparence et la mise en page.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Au minimum deux depuis notre site : le document HTML et la feuille CSS. Il peut aussi demander la favicon et l’image externe.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Le navigateur peut réutiliser une ancienne copie en cache. Le rechargement forcé demande de nouveaux fichiers.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol. Le navigateur/client envoie la requête ; le serveur renvoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ À vérifier dans l’onglet Réseau de mon navigateur. Il y a au moins la requête du document `/presentation` et celle de `/static/style.css`; l’image et la favicon peuvent ajouter des requêtes.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ 200 signifie que la requête a réussi. 404 signifie que la ressource demandée (ici l’icône favicon) n’a pas été trouvée.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Elles ne modifient que la copie de la page dans mon navigateur ; le code du serveur n’a pas changé.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le paramètre est `search_query` et sa valeur est `chat`.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ `int("bonjour")` ne peut pas convertir ce texte en nombre et déclenche une erreur. Il faut vérifier/valider la valeur et gérer l’exception en répondant proprement, par exemple avec une erreur 400.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Une entrée pourrait contenir du HTML ou du JavaScript malveillant. Il faut échapper le texte (comme le fait Jinja dans un template) et valider les entrées.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ Avec GET les champs apparaissent dans l’URL ; avec POST ils sont dans le corps de la requête, pas dans la barre d’adresse.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ GET convient à la recherche, car l’URL peut être partagée ou mise en favori. Pour un mot de passe, POST évite de l’afficher dans l’URL, mais il faut aussi HTTPS et une vraie protection : POST seul ne rend pas les données secrètes.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non. Elles sont visibles dans les outils réseau et peuvent être interceptées sans HTTPS ; POST ne chiffre pas les données.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Une 4xx indique généralement un problème dans la demande du client ; une 5xx indique une erreur ou une panne côté serveur.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Le serveur répond avec un statut 3xx et un en-tête `Location`. Le navigateur suit cette adresse et envoie la deuxième requête.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Après connexion, un site peut rediriger vers la page d’accueil ou la page demandée ; un ancien lien peut aussi rediriger vers une nouvelle URL.

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ Il peut recevoir l’adresse IP (ou celle du relais/proxy), le navigateur via `User-Agent` et les langues préférées via `Accept-Language`.

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ Il peut aider le site à proposer une version dans une langue que le navigateur préfère.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ À relever dans mon propre Access log PythonAnywhere après le déploiement ; je ne peux pas connaître ce journal depuis le dépôt.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ La navigation n’est pas totalement anonyme pour le site : certaines informations techniques sont envoyées automatiquement. Des outils peuvent réduire les traces, mais ne garantissent pas un anonymat absolu.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ HTML décrit une page à afficher aux humains ; JSON est une structure de données facile à traiter par des programmes (et aussi lisible par une personne).

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Flask calcule la date et l’heure et renvoie le JSON de `/api/heure`. Le JavaScript de la page s’exécute dans le navigateur, appelle l’API et met à jour le contenu sans recharger toute la page.

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ Une application météo peut demander à un serveur les prévisions d’une ville et recevoir température, conditions et horaires sous forme de données.

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ Le navigateur utilise l’adresse pour joindre le serveur et lui envoie une requête HTTP. Le serveur exécute le code correspondant à la route et renvoie une réponse (par exemple du HTML). Le navigateur interprète le HTML, puis demande les ressources liées comme le CSS et les images, avant d’afficher la page.
