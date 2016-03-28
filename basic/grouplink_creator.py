__author__ = 'johnanderson1'
def creategroup_link(group):
    group=group.strip()
    if group.find(" "):
         x=group.replace(" ","-")
         return x
    else:
        return group


