# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:44:17 2019

@author: Richy
"""

import random
import pandas as pd


purch = []
# Make spending categories
descriptions = ['Grocries', 'Dining', 'Clothes', 'Bills', 'Dining'] #Extra dining to make more prevalent

for i in range(100):
    price = round(random.randint(-200, -1) + random.random(), 2)
    desc = random.choice(descriptions)
    
    purch.append([price, desc])
    
  
# Make example stores     
groc = ['Harris Tetter', 'Target', 'Publix', 'Food Lion']
dine = ['Pizza Hut', 'Taco Bell', 'Firehouse Subs', 'Outback', 'Sycamore', 'Red Lobster', 'Cook Out', 'Bojangles']
Clothes = ['Belks', 'Macys', 'Nike', 'Polo']
Bill = ['Metro', 'Water', 'Electricity', 'Gas', 'Spotify']



for item in purch:
    if item[1] == 'Grocries':
        item.append(random.choice(groc))
        
    elif item[1] == 'Dining':
        item.append(random.choice(dine))
        
    elif item[1] == 'Clothes':
        item.append(random.choice(Clothes))
        
    else:
        item.append(random.choice(Bill))
        
        
spend_df = pd.DataFrame(purch)