from django.db import models


class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=8)
    email = models.EmailField()

    def __str__(self):
        return self.nom + ' ' + self.prenom + ' ' + self.telephone

class Post(models.Model):
    image = models.ImageField()
    TYPE_CHOICES = [
        (0, 'Offre'),
        (1, 'Demande'),
    ]
    title = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + str(self.type)

class Reaction(models.Model):
    comment = models.TextField()
    like = models.BooleanField()
    rd = models.ForeignKey(User, on_delete=models.CASCADE)
    pt = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment + ' ' + str(self.like)

class Stage(models.Model):
    TYPE_CHOICES = [
        (1, 'Ouvrier'),
        (2, 'Technicien'),
        (3, 'PFE'),
    ]
    typeStg = models.IntegerField(choices=TYPE_CHOICES)
    societe = models.CharField(max_length=200)
    duree = models.IntegerField()
    sujet = models.CharField(max_length=200)
    contactInfo = models.CharField(max_length=200)
    specialite = models.CharField(max_length=200)

    def __str__(self):
        return str(self.typeStg) + ' ' + self.societe + ' ' + str(self.duree) + ' ' + self.sujet

class Logement(models.Model):
    localisation = models.CharField(max_length=200)
    description = models.TextField()
    contactInfo = models.CharField(max_length=200)

    def __str__(self):
        return self.localisation + ' ' + self.description

class Transport(models.Model):
    depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=200)
    heuredep = models.TimeField()
    nbresieges = models.IntegerField()
    contactInfo = models.CharField(max_length=200)

    def __str__(self):
        return self.depart + ' ' + self.destination + ' ' + str(self.heuredep) + ' ' + str(self.nbresieges)

class Recommandation(Post):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Event(Post):
    intitule = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    lieu = models.CharField(max_length=200, default='')
    contactInfo = models.CharField(max_length=200, default='')
    post_ptr = models.OneToOneField(
        Post, 
        on_delete=models.CASCADE, 
        parent_link=True, 
        default=None
    )

    def __str__(self):
        return self.intitule + ' ' + self.description + ' ' + self.lieu + ' ' + self.contactInfo

class EvenClub(Event):
    club = models.CharField(max_length=200)
    

    def __str__(self):
        return self.club

class EvenSocial(Event):
    prix = models.DecimalField(max_digits=15, decimal_places=3)
    

    def __str__(self):
        return str(self.prix)
