import iterators as IT

#  *separate script for assembling words and junctions to be layout friendly
# ? determined junctions are picked from non determined junctions
# ? words with more possible junctions are described as a high degree of entanglement
# ? entanglent has a direct relationship with layout flexibility
# ? order of junction determines flexibility.
#	todo: determine junctions (junctions)

#	todo: sort by entanglement

#	todo: check for overlap
# ? need the ability to identify where letters are with coordinates.
# ? characters should be assigned coords that can be easily accessed
#	todo: getCoordinate(tupple)
#	todo: setCoordinate(char,incrType,lastCoor)
def setCoordinate(params):
    tile = {'char':params['char'], 'coord': None}
    if(params['incrType'] == 'x'):
        tile['coord'] = [params['lastCoord'][0]+1, params['lastCoord'][1]]
    else:
        tile['coord'] = [params['lastCoord'][0], params['lastCoord'][1]+1]

def getCoordinate(tile):
    return tile['coord']
