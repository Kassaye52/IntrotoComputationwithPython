{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 14. MONTE CARLO SIMULATION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def rollDie():\n",
    "    return random.choice([1,2,3,4,5,6]) \n",
    "\n",
    "def checkPascal(numTrials):\n",
    "    \"\"\"Assumes numTrials an int > 0\n",
    "    Prints an estimate of the probability of winning\"\"\"\n",
    "    numWins = 0.0\n",
    "    for i in range(numTrials):\n",
    "        for j in range(24):\n",
    "            d1 = rollDie()\n",
    "            d2 = rollDie()\n",
    "        if d1 == 6 and d2 == 6:\n",
    "            numWins += 1\n",
    "            break\n",
    "    print('Probability of winning =', numWins/numTrials)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Probability of winning = 1e-06\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "checkPascal(1000000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "class CrapsGame(object):\n",
    "    def __init__(self):\n",
    "        self.passWins, self.passLosses = (0,0)\n",
    "        self.dpWins, self.dpLosses, self.dpPushes = (0,0,0)\n",
    "        \n",
    "    def playHand(self):\n",
    "        throw = rollDie() + rollDie()\n",
    "        if throw == 7 or throw == 11:\n",
    "            self.passWins += 1\n",
    "            self.dpLosses += 1\n",
    "        elif throw == 2 or throw == 3 or throw == 12:\n",
    "            self.passLosses += 1\n",
    "            if throw == 12:\n",
    "                self.dpPushes += 1\n",
    "            else:\n",
    "                self.dpWins += 1\n",
    "        else:\n",
    "            point = throw\n",
    "            while True:\n",
    "                throw = rollDie() + rollDie()\n",
    "                if throw == point:\n",
    "                    self.passWins += 1\n",
    "                    self.dpLosses += 1\n",
    "                    break\n",
    "                elif throw == 7:\n",
    "                    self.passLosses += 1\n",
    "                    self.dpWins += 1\n",
    "                    break\n",
    "    def passResults(self):\n",
    "        return (self.passWins, self.passLosses)\n",
    "    def dpResults(self):\n",
    "        return (self.dpWins, self.dpLosses, self.dpPushes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def crapsSim(handsPerGame, numGames):\n",
    "    \"\"\"Assumes handsPerGame and numGames are ints > 0\n",
    "    Play numGames games of handsPerGame hands, and print results\"\"\"\n",
    "    games = []\n",
    "\n",
    "    #Play numGames games\n",
    "    for t in range(numGames):\n",
    "        c = CrapsGame()\n",
    "        for i in range(handsPerGame):\n",
    "            c.playHand()\n",
    "        games.append(c)\n",
    "    \n",
    "    #Produce statistics for each game\n",
    "    pROIPerGame, dpROIPerGame = [], []\n",
    "    for g in games:\n",
    "        wins, losses = g.passResults()\n",
    "        pROIPerGame.append((wins - losses)/float(handsPerGame))\n",
    "        wins, losses, pushes = g.dpResults()\n",
    "        dpROIPerGame.append((wins - losses)/float(handsPerGame))\n",
    "\n",
    "    #Produce and print summary statistics\n",
    "    meanROI = str(round((100.0*sum(pROIPerGame)/numGames), 4)) + '%'\n",
    "    sigma = str(round(100.0*stdDev(pROIPerGame), 4)) + '%'\n",
    "    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev. =', sigma)\n",
    "    meanROI = str(round((100.0*sum(dpROIPerGame)/numGames), 4)) + '%'\n",
    "    sigma = str(round(100.0*stdDev(dpROIPerGame), 4)) + '%'\n",
    "    print('Don\\'t pass:','Mean ROI =', meanROI, 'Std Dev =', sigma)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "crapsSim(20, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def playHand(self):\n",
    "    #An alternative, faster, implementation of playHand\n",
    "    pointsDict = {4:1/3.0, 5:2/5.0, 6:5/11.0, 8:5/11.0,\n",
    "    9:2/5.0, 10:1/3.0}\n",
    "    throw = rollDie() + rollDie()\n",
    "    if throw == 7 or throw == 11:\n",
    "        self.passWins += 1\n",
    "        self.dpLosses += 1\n",
    "    elif throw == 2 or throw == 3 or throw == 12:\n",
    "        self.passLosses += 1\n",
    "        if throw == 12:\n",
    "            self.dpPushes += 1\n",
    "        else:\n",
    "            self.dpWins += 1\n",
    "    else:\n",
    "        if random.random() <= pointsDict[throw]: # point before 7\n",
    "            self.passWins += 1\n",
    "            self.dpLosses += 1\n",
    "        else: # 7 before point\n",
    "            self.passLosses += 1\n",
    "            self.dpWins += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def throwNeedles(numNeedles):\n",
    "    inCircle = 0\n",
    "    for Needles in range(1, numNeedles + 1):\n",
    "        x = random.random()\n",
    "        y = random.random()\n",
    "        if (x*x + y*y)**0.5 <= 1.0:\n",
    "            inCircle += 1\n",
    "    #Counting needles in one quadrant only, so multiply by 4\n",
    "    return 4*(inCircle/float(numNeedles))\n",
    "\n",
    "def getEst(numNeedles, numTrials):\n",
    "    estimates = []\n",
    "    for t in range(numTrials):\n",
    "        piGuess = throwNeedles(numNeedles)\n",
    "        estimates.append(piGuess)\n",
    "    sDev = stdDev(estimates)\n",
    "    curEst = sum(estimates)/len(estimates)\n",
    "    print('Est. = ' + str(round(curEst, 5)) + ', Std. dev. = ' + str(round(sDev, 5)) + ', Needles = ' + str(numNeedles))\n",
    "    return (curEst, sDev)\n",
    "\n",
    "def estPi(precision, numTrials):\n",
    "    numNeedles = 1000\n",
    "    sDev = precision\n",
    "    while sDev >= precision/2.0:\n",
    "        curEst, sDev = getEst(numNeedles, numTrials)\n",
    "        numNeedles *= 2\n",
    "    return curEst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "def stdDev(X):\n",
    "    \"\"\"Assumes that X is a list of numbers.\n",
    "    Returns the standard deviation of X\"\"\"\n",
    "    mean = float(sum(X))/len(X)\n",
    "    tot = 0.0\n",
    "    for x in X:\n",
    "        tot += (x - mean)**2\n",
    "    return (tot/len(X))**0.5 #Square root of mean difference"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Est. = 3.14284, Std. dev. = 0.04899, Needles = 1000\n",
      "Est. = 3.14244, Std. dev. = 0.03681, Needles = 2000\n",
      "Est. = 3.14525, Std. dev. = 0.02117, Needles = 4000\n",
      "Est. = 3.14075, Std. dev. = 0.0158, Needles = 8000\n",
      "Est. = 3.14074, Std. dev. = 0.01423, Needles = 16000\n",
      "Est. = 3.14084, Std. dev. = 0.00949, Needles = 32000\n",
      "Est. = 3.14165, Std. dev. = 0.00632, Needles = 64000\n",
      "Est. = 3.14155, Std. dev. = 0.0046, Needles = 128000\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "3.1415499999999996"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estPi(0.01, 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
