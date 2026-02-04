
"""
std::vector → list en Python

Pas besoin d’indiquer les types (String)

push_back() → append()

Les {} deviennent une indentation

studentFile = dossierEtudiant
to  borrow = emprunter
loanDate = dateEmprunt
"""

"""
Mission 1:Système de prêt de livres
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


