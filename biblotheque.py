
"""
std::vector → list en Python

Pas besoin d’indiquer les types (String)

push_back() → append()

Les {} deviennent une indentation

studentFile = dossierEtudiant
to  borrow = emprunter
loanDate = dateEmprunt
"""


books=[]
def addBook(author,book):

   books.append({
      "autor" : author,
       "book title" : book,
   })

StudentFile= []
def borrowBook(loanDate,dateFin,studentName,adress,book):
   StudentFile.append(
      {
         "loanDate" : loanDate,
         "date fin" : dateFin,
         "Name of student": studentName,
         "adress" : adress,
         "book": book,
         
      }
   )
   return f"book '{book}'emprunté par {studentName} avec succés."


def returnBook(studentName,book):
   return f"the book '{book}' est retourné par {studentName}."

message = returnBook("Alice Martin", "Python pour débutants")
print(message)  




"""
Mission 2:  Gestion des étudiants
"""
listesEtudiants =[]

def enregistreEtudiant(nom, cip,programme):
   for etudiant in listesEtudiants:
      if etudiant["cip"] == cip:
         return f"Erreur : Le cip {cip} existe déjà pour l'étudiant {etudiant["nom"]}"
   
   nouvel_etudiant = {
      "nom" : nom,
      "cip" : cip,
      "programme" : programme
   }

    
   listesEtudiants.append(nouvel_etudiant)
   return f"Etudiant {nom} cip: {cip} est enregistré dans le programme {programme}."

