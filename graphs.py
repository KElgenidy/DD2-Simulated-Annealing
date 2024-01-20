import matplotlib.pyplot as plt

def plotCR():
    coolingRates = [0.75, 0.80, 0.85, 0.90, 0.95]
    twld0 = [36, 37, 37, 34, 35]
    twld1 = [67, 63, 67, 64, 66]
    twld2 = [1300, 1109, 1123, 1112, 1072]
    twld3 = [1066, 1000, 1004, 971, 910]
    twlt1 = [2421, 2315, 2037, 2078, 1863]
    twlt2 = [9977, 9407, 8421, 7716, 5924]
    twlt3 = [13771, 13210, 11963, 11595, 10888]

    plt.figure(figsize=(10, 6))
    plt.plot(coolingRates, twld0, label = "d0")
    plt.plot(coolingRates, twld1, label = "d1")        
    plt.plot(coolingRates, twld2, label = "d2")
    plt.plot(coolingRates, twld3, label = "d3")
    plt.plot(coolingRates, twlt1, label = "t1")
    plt.plot(coolingRates, twlt2, label = "t2")
    plt.plot(coolingRates, twlt3, label = "t3")

    plt.xlabel('Cooling Rate')
    plt.ylabel('Wirelength')
    plt.title('Cooling Rate vs. Wirelength')
    plt.legend()
    plt.show()

def plotT(tempsFile, twlFile):
    twls = []
    temperatures = []

    with open(tempsFile, 'r') as file:
        for line in file:
            temperatures.append(float(line.strip()))
    
    with open(twlFile, 'r') as file:
        for line in file:
            twls.append(int(line.strip()))

    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, twls)
    plt.xlabel('Temperature')
    plt.ylabel('Wirelength')
    plt.title('Temperature vs. Wirelength')
    plt.show()

def plotIterCR(iterFile):
    coolingRates = [0.75, 0.80, 0.85, 0.90, 0.95]
    iterations = []

    with open(iterFile, 'r') as file:
        for line in file:
            iterations.append(int(line.strip()))
    
    plt.figure(figsize=(10, 6))
    plt.plot(coolingRates, iterations)
    plt.xlabel('Cooling Rates')
    plt.ylabel('Iterations')
    plt.title('Cooling Rates vs. Iterations')
    plt.show()

def plotIterTemps(iterFile, tempsFile):
    iterations = []
    temperatures = []

    with open(tempsFile, 'r') as file:
        for line in file:
            temperatures.append(float(line.strip()))

    with open(iterFile, 'r') as file:
        for line in file:
            iterations.append(int(line.strip()))
    
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, temperatures)
    plt.xlabel('Iterations')
    plt.ylabel('Temperatures')
    plt.title('Temperatures vs. Iterations')
    plt.show()

tempsFile = "temps.txt"
twlFile = "twl.txt"
iterFileTemps = "it.txt"
iterFileCR = "iterd0.txt"
# plotCR()
# plotT(tempsFile, twlFile)
# plotIterCR(iterFileCR)
plotIterTemps(iterFileTemps, tempsFile)