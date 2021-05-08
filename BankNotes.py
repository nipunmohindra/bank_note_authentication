# -*- coding: utf-8 -*-
"""
Created on Mon May 03 19:36:32 2021

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float