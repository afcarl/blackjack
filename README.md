## Blackjack code

Hi! I wrote up a set of objects to play blackjack, and simulate
the basics of the game. it was an interesting exercise.

After a while, I wondered about the optimal strategy for placing
bets. I'm familiar with a couple of strategies, such as +/-1 or 
rules about hitting or standing when the value of a hand is 
above a certain number.

### Simulation code

I took my code and created a simulation to test out different
strategies. The total number of hands played was output for
1000 games of poker with the strategy

I ran it simply with my main calling findBestStrategy()

    python blackjack.py > col

And in ipython,

    df = pd.read_csv('col')
    df.hist(bins=100)
    plt.show()

No fancy data analysis for now, let's just load it up and
create a histogram of hands of poker until the human player
goes broke.

### 16, hit or stand

When we have a more conservative strategy, we seem to get
a bigger spread of values. Some games go on as long as 17
but others seem to end kind of quicker, too

![16, hit or stand](img/16hitorstand.png)

### 17, hit or stand

The dealer in this code always hits when its hand is below 17
and will stand when it's 17 or higher. 

Let's see what happens when our human player does something
similar.

![17, hit or stand](img/17hitorstand.png)

### 17, hit or stand, randomly bet 1 to 3 dollars

Well, this was unfortunate. I'm willing to 'bet' that 
randomly betting is not a good strategy.


![17, hit or stand](img/17hitorstandRandomBet.png)

### 18, hit or stand

It seems like we get slightly better results with a more
aggresive strategy. It's interesting that there are a few
games that got to almost 1000 rounds!

![18, hit or stand](img/18hitorstand.png)

### 19, hit or stand

Aggresive is good, until we get to here. It seems like we 
do very poorly.

![19, hit or stand](img/19hitorstand.png)

### Average purse size

Let's have a look at the histogram of average values for the
human purse.

![18, hit or stand histogram of purse value](img/18hitorstandHist.png)

As a final piece, let's look at the average value of the purse, 
keeping in mind that the game starts with one a 100 and ends when
it's 0.

![18, hit or stand, average purse value](img/18hitorstandPrintPurseByAverage.png)


### Time to win

Let's see what histogram for total hands played until one goes broke

First, with a 18, hit or stand strategy

![18, average number of wins](img/18WinLoss.png)


With a 17 hit or stand strategy, we seem to do a little bit better

![17, number of wins](img/17winLos.png)

Still, in an average casino, a few dozen hands of poker can take
a while, so maybe a player could get comp'ed by the casino for free drinks, a 
night out, even some free food if they make poker look easily to convince 
other visitors that it's worth their time (and money).

In reality, real poker games aren't going to go like this, and I imagine
that the amount of money bet is different, as well as the speed of the
poker games, along with the special rules I didn't implement.

![](http://mjk.freeshell.org/blackjack.gif)
[![ghit.me](https://ghit.me/badge.svg?repo=emmjaykay/blackjack)](https://ghit.me/repo/emmjaykay/blackjack)
