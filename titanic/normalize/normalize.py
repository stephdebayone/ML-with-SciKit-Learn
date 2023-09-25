import numpy as np 



# extraire du champ name le statut Mr M Miss Misses 
def nmName(row): 
    strName = row[3]
    strSex  = row[4]
    newValue = "" 
#    if not hasattr(nmName, 'n'):
#        nmName.n = 0 
    d = { 'Mr.' : 0 ,  'Master.' : 0 , 'Major.' : 0 , 'Capt.' : 0 , 'Sir.' : 0 , 'Col.' : 0 , 'Don.' : 0 , 
          'Mrs.' : 1 , 'Dona.' : 1  ,   'Mme.' : 1 , 'Lady.' : 1, 'Countess.' : 1 , 'Ms.' : 1 , 
          'Miss.' : 2 , 'Mlle.' : 2 }
    for k,v in d.items():
         if strName.find(k) > -1:
             newValue = v 
    if strName.find('Dr.') > -1:
        if strSex == 'male':
            newValue = 0  
        elif strSex == 'female':
            newValue = 1  
    elif strName.find('Rev.') > -1:
        newValue = 0 
    else:
        if strSex == 'male':
            newValue = 0
        else:
            newValue = 1 
    
#   print("name : %s sex : %s" % (strName,strSex ))
#   nmName.n += 1 
#   print('%s. %s' % (nmName.n,strName) ) 

      
    return newValue
    

def normalize_name(df):
    df['Gender'] = df.apply(nmName,axis=1)
         
def nmSex(row):
    strSex  = row[4]
    if strSex == 'male':
        return 0
    elif strSex == 'female':
        return 1
    
    print('Erreur sex : %s' % strSex  )
        
        
# extraire du champ sex 0 si il s'agit d'un homme 1 s'il s'agit d'une femme
def normalize_sex(df):
    df['Sex'] = df.apply(nmSex,axis=1)  

# Remplacer les valeurs nulles du champ age
def normalize_age(df):
    median = df['Age'].median()
    print(median) 
    df = df.fillna(value= {'Age' : median }) 
    return df 
    

def nmEmbarked(row):
    embarked = row[11]
    d = { 'S' : 0 , 'C' : 1 , 'Q' : 2}
    try:
        return d[embarked]
    except KeyError:
        return 0 

# remplacer le champ embarked par une valeur numérique
def normalize_embarked(df):
    df['Embarked'] = df.apply(nmEmbarked,axis=1) 


def normalize(df): 
    df_copy = df.copy() 
    # extraire du champ name le statut Mr M Miss Misses 
    normalize_name(df_copy) 
    # extraire du champ sex 0 si il s'agit d'un homme 1 s'il s'agit d'une femme
    normalize_sex(df_copy) 
    # remplacer le champ embarked par une valeur numérique
    normalize_embarked(df_copy)
    # Remplacer les valeurs nulles du champ age
    df_copy = normalize_age(df_copy)
    df_copy = df_copy.drop(columns=['Name','Cabin','Ticket' , 'PassengerId' , 'Gender' ])
    return df_copy 
 
