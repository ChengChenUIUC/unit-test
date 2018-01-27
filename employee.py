# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:19:32 2018

@author: Cheng
"""
import requests

class Employee:
    raise_amt = 1.05
    
    def __init__(self, firstName, lastName, pay):
        self.first = firstName
        self.last = lastName
        self.pay = pay
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    def monthly_schedule(self, month):
        response = requests.get('http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return '_Bad Response_'