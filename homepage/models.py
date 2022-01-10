from django.db import models
from users.models import Profile
# Create your models here.
class Projects(models.Model):
    """
    Class to create a new project
    """
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    project_image = models.ImageField(upload_to='images')
    project_link = models.URLField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    date_created= models.DateField(auto_now_add=True )

    def save_projects(self):
        """
        Class method to save project
        """
        self.user

    def delete_projects(self):
        """
       Class method to delete project(id) 
        """
        self.delete()    


    @classmethod
    def search_projects(cls, name):
        """
        Class method to search for a project
        """
        return cls.objects.filter(title__icontains=name).all()

RATE_CHOICES = [
(1,'1- Trash'),
(2,'2- Horrible'),
(3,'3- Terrible'),
(4,'4- Bad'),
(5,'5- Ok'),
(6,'6- Watchable'),
(7,'7- Good'),
(8,'8- Very Good'),
(9,'9- perfect'),
(10,'10- Master Piece'),
]
class Review(models.Model):
    """
    model class to create reviews
    """
    projects = models.ForeignKey(Projects,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=3000,blank=True)
    design = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default= 0)
    usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    content = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    


    def __str__(self):
        """
        returns a stringified representation of the object
        """
        return self.projects
