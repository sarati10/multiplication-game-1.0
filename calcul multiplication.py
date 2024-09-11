# -*- coding: utf-8 -*-
# module1 créé par augus_hqciuly le 04/09/2024
# Sujet :
#
#
#-------------------------------------------------------------------------------
def DemandeReponseOperation(op,a,b,score,partie):
    global temps
    S = str(a)+op+str(b)
    if op =='*' : op_aff = chr(215)
    else : op_aff = op
    s_aff = str(a)+' '+op_aff+' '+str(b)
    td = time.time()

    resultat=eg.saisie_entier(msg="combien fait " + s_aff+' ? (score = '+str(score)+', parties = ' + str(partie)+', temps = '+str(int(temps))+')', titre = "Jeu des opérations", defaut='', borneinf = 0, bornesup = 100)
    tf = time.time() -td
    temps = temps + tf
    u = int(eval(S))
    if u == resultat: z = -1
    else: z = u
    return z


import random
import easyguifr as eg
import time

operations = ['*']
scoreOp = [0,0,1,2,3,2,3,4,4,4,1]
nombreOp = 9
jeuFini = False
score = 0; temps = 0 ; partie = 0 ; flemme=1

while not jeuFini:
    if flemme==1:
        a=random.randrange(2,10)
        b=random.randrange(2,10)
    RR = DemandeReponseOperation(op,a,b,score,partie)
    msg = '. Continuer?'
    if RR == -1 :
        score = score+scoreOp[a]+scoreOp[b]
        partie = partie + 1
        msg = 'Ok, bonne réponse '+msg
    else:
        msg='Erreur : bonne réponse = '+str(RR)+msg
    Reponse = eg.boite_continuer_annuler(titre='Jeu des opérations',msg=msg)
    if Reponse == 0:
        jeuFini = True



