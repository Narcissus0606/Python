#431103199806060933
def get_sex(id):
    if(int(id[-2:-1])== 0):
        return "famale"
    else:
        return "male"
def get_birth(id):
       return id[6:14]

id = "431103199806060933"
print("Sex:",get_sex(id))
print("Birthday:",get_birth(id))
