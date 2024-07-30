points = [(3,6),(5,6),(5,8),(8,9),(10,5),(9,7)]

def euclideanDistance(points):
    distances=[]
    for i in range(len(points)-1):
       distances.append(((points[i][0]- points[i+1][0])**2 + (points[i][1]- points[i+1][1])**2)**(1/2)) 

    min = float("inf") #sonsuz demek
    for i in range(len(distances)-1):
        if distances[i]<min:
            min=distances[i]
        else:
            min=min
    return min

print(euclideanDistance(points))
    