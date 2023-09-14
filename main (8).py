class Player:
  def play(self):
    print("The Player is Playing  cricket")
#define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The Batsman is Bating")
#define the derived class Batsman
class Bowler(Player):
  def play(self):
    print("The Bowler is bowling")
#create objects of Batsman and bowler classes
batsman=Batsman()
bowler=Bowler()
#call the play()method for ecah object
batsman.play()
bowler.play()