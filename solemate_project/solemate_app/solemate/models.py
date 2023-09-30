from django.db import models

# i solemnly swear i will not cut alan off

# all strings
# CID - shoe id
# Category - footwear category
# SubCategory - shoe type category
# Heel/Height
# Insole
# Closure
# Gender
# Material
# ToeStyle

class Sneaker(models.Model):
    cid = models.CharField(max_length=20, primary_key=True)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    heel_height = models.CharField(max_length=50)
    insole = models.CharField(max_length=50)
    closure = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    material = models.CharField(max_length=50)
    toestyle = models.CharField(max_length=50)

    def __str__(self):
        return f"CID: {self.cid}, Category: {self.category}, Subcategory: {self.subcategory}, Heel/Height: {self.heel_height}, Insole: {self.insole}, Closure: {self.closure}, Gender: {self.gender}, Material:{self.material}, ToeStyle: {self.toestyle}"

