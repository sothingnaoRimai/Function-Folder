def checkage(age):
    if age <18:
        return False
    return True

def chooseparty():
    parties=['BJP','INC']
    return parties [1]

def vote(name):
    party=chooseparty()
    print(name,"has chosen ",party,"as his party")
    votingcomplete=True
    return votingcomplete,party

def sentwarningmessage(name):
    print(name,"is still not eligible for voting")

def voter(name, age):
    eligible=checkage(age)
    if eligible:
        vote_status,party=vote(name)
        if vote_status:
            print(name,"has successfully voted for ",party)
        else:
            sentwarningmessage(name)
    else:
        sentwarningmessage(name)
voter("soso",23)


