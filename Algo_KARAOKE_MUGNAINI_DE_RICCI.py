class Karaoke:
    def __init__(self):
        self.joueurs = []
        self.musiques = ["Wicked Game", "Blinding lights", "Counting Stars", "Faded"]

    def afficheMusiques(self):
        for i in range(len(self.musiques)):
            print(str(self.musiques[i]) + " --> " + str(i))
    
    def ajouteJoueur(self):
        pass
        # Je n'ai pas réussi cette méthode ;_;

    def supprimeJoueur(self):
        if len(self.joueurs) > 1:
            for i in range(len(self.joueurs)):
                print(str(self.joueurs[i].pseudo) + " --> " + str(i))
            choix = int(input("Quel joueur voulez vous supprimer ? "))
        else:
            print("il doit y avoir plusieurs joueurs pour en supprimer un ...")

    def meilleurScoreChanson(self):
        chanson = int(input("Numéro de la chanson ? "))
        meilleur = 0
        for i in range(len(self.joueurs)):
            if self.joueurs[i].scores[chanson] > meilleur:
                meilleur = self.joueurs[i].scores[chanson]
        print("Le meilleur score est : " + str(meilleur))

    def meilleurScoreTotal(self):
        meilleur = 0
        for i in range(len(self.joueurs)):
            if self.joueurs[i].scoreTotal() > meilleur:
                meilleur = self.joueurs[i].scoreTotal()
        print("Le meilleur score total est : " + str(meilleur))

    def meilleurScoreConfondu(self):
        meilleur = 0
        for i in range(len(self.joueurs)):
            if self.joueurs[i].meilleurScore() > meilleur:
                meilleur = self.joueurs[i].meilleurScore()
        print("Le meilleur score toutes musiques confondues est : " + str(meilleur))

    def meilleurMoyenne(self):
        meilleur = 0
        for i in range(len(self.joueurs)):
            if self.joueurs[i].moyenne() > meilleur:
                meilleur = self.joueurs[i].moyenne()
        print("La meilleure moyenne est : " + str(meilleur))


class Player:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.scores = []
        for i in range(len(salle1.musiques)):
            self.scores.append(0)

    def moyenne(self):
        compteur = 0
        moyenne = 0
        for i in range(len(self.scores)):
            if self.scores[i] != 0:
                moyenne += self.scores[i]
                compteur += 1
        if moyenne != 0:
            moyenne = moyenne / compteur
            #print("La moyenne de " + self.pseudo + " est de : " + str(moyenne))
            return moyenne
        else:
            #print(self.pseudo + " n'a pas de scores enregistrés")
            return 0

    def scoreTotal(self):
        total = 0
        for i in range(len(self.scores)):
            total += self.scores[i]
        #print(self.pseudo + " a un score total de : " + str(total))
        return total

    def meilleurScore(self):
        #print("Le meilleur score de " + self.pseudo + " est : " + str(max(self.scores)))
        return max(self.scores)

    def pireScore(self):
        scores = []
        for i in range(len(self.scores)):
            if self.scores[i] != 0:
                scores.append(self.scores[i])
        #print("Le pire score de " + self.pseudo + " est : " + str(min(scores)))
        return min(scores)

    def afficheScores(self):
        print("Tableau des scores de " + self.pseudo + " : ")
        for i in range(len(self.scores)):
            print(str(salle1.musiques[i]) + " : " + str(self.scores[i]))

    def ajouteScore(self):
        salle1.afficheMusiques()
        num = int(input("Quel est le numéro de la chanson sur laquelle vous avez fait un score ? "))
        while num>len(salle1.musiques) or num<0:
            num = int(input("Quel est le numéro de la chanson sur laquelle vous avez fait un score ? "))
        score = int(input("Quel est le score ? "))
        while score>100 or score<0:
            score = int(input("Entre 0 et 100 ! "))
        if self.scores[num] < score:
            self.scores[num] = score


salle1 = Karaoke()

pseudo = input("Choisissez un pseudo : ")
joueur1 = Player(pseudo)

salle1.joueurs.append(joueur1)

pseudo = input("Choisissez un pseudo : ")
joueur2 = Player(pseudo)

salle1.joueurs.append(joueur2)

joueur1.ajouteScore()
joueur1.ajouteScore()
joueur1.ajouteScore()
joueur1.moyenne()
joueur1.scoreTotal()
joueur1.meilleurScore()
joueur1.pireScore()
joueur1.afficheScores()

joueur2.ajouteScore()
joueur2.ajouteScore()
joueur2.ajouteScore()
joueur2.moyenne()
joueur2.scoreTotal()
joueur2.meilleurScore()
joueur2.pireScore()
joueur2.afficheScores()

salle1.meilleurScoreChanson()
salle1.meilleurScoreTotal()
salle1.meilleurScoreConfondu()
salle1.meilleurMoyenne()
salle1.supprimeJoueur()
