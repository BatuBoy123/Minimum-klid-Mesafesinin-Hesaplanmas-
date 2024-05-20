import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1,point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

# Noktaları Tanımlama
points = [(1,2),(3,4),(6,8),(2,1),(5,7)]

distances = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)
        print(distance)
       
# Minimum mesafenin bulunması 
min_distance = min(distances)

print(f"Points: {points}")
print(f"Distances: {distances}")
print(f"Minimum distance: {min_distance}")

