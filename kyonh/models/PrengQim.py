# coding=utf-8
from django.db import models

#拼音
class PrengQim(models.Model):
  #標識
  identifier = models.CharField(primary_key=True, max_length=6)
  polyhedron = models.CharField(verbose_name="古韻羅馬字", max_length=8, null=True)
  hiovNivv = models.CharField(verbose_name="有女羅馬字", max_length=8, null=True)
  thuaiDauh = models.CharField(verbose_name="推導現代漢語", max_length=8, null=True)
  
  class Meta:
    app_label = 'kyonh'
