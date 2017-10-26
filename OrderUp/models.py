from __future__ import unicode_literals

from django.db import models

class Resturant (models.Model): 
  name = models.CharField(max_length = 160,blank = True)
  image = models.ImageField(upload_to="images", default='images/usr1.jpg')
  category = models.CharField(max_length = 160,blank = True)
  phone = models.CharField(max_length = 160,blank = True)
  address = models.CharField(max_length = 160,blank = True)
  menu = models.CharField(max_length = 160,blank = True)
  price = models.CharField(max_length = 160,blank = True)

  def __unicode__(self):
        return 'id=' + str(self.id) + 'name' + str(self.name) + "category" + str(self.category)

class Order (models.Model): 
  quantity = models.CharField(max_length = 160,blank = True)
  resturant = models.ForeignKey(Resturant,default = None)
  timestamp = models.DateTimeField(auto_now = True)
  ordernumber = models.CharField(max_length = 160,blank = True)
  totalprice = models.CharField(max_length = 160,blank = True)
