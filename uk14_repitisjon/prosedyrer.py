
def partall(tall):
    if tall % 2 == 0:
        print("Dette er et partall")
    else:
        print("Dette er ikke et partall")

def partall_v2(tall): #tall er alltid int
    if tall % 2 == 0:#tall er alltid int
        return True#tall er alltid int
    else:#tall er alltid int
        return False#tall er alltid int

funk_kall = partall_v2(11)
print(funk_kall)