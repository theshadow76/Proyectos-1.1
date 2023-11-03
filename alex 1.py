import webbrowser as w1

v1=input("Écrire le verbe que vous voulez: ")
s1,s2= 'áÁéÉíÍóÓúÚàÀèÈìÌòÒùÙâÂêÊîÎôÔûÛäÄëËïÏöÖüÜñ ','aAeEiIoOuUaAeEiIoOuUaAeEiIoOuUaAeEiIoOuUn+'
trans = str.maketrans(s1,s2)
v1= v1.translate(trans)
s3='https://leconjugueur.lefigaro.fr/french/verb/' + v1 + '.html'
w1.open(s3, new=2, autoraise=True)