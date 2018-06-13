The goal of this repo is to enable playing Hearthstone entirely by voice and audio feedback.
For example, you should be able to play while driving, without looking at the screen or pressing any buttons.

Ideally, this means you will be able to ask questions, and issue commands. For example:

Menu commands:
-start standard game
-start brawl
-get online friends
-challenge friend to game

In Game Questions:
-read enemy cards (lists cards visable on top side of the board)
-read my active cards (list cards visable on the bottom side of the board)
-read my hand (lists cards in you hand)
-read details on <card name> (reads heath, attack, and ability on a specific card)
-what is my/ememy health (states remaining heath)
-what is my/ememy mana (states remaining mana)
-etc...

In Game Commands:
-Play card one (plays first card in hand to board.  By default, plays to left side of board, but position can be specified)
-Atack face with card one (attacks emeny player with first active card)
-etc...

The basic mechanics of this program is that it runs on a computer that is already running hearthstone.  Hearthstone writes game logs in real time as you play, so this program can watch what is going on by activly reading the logs.  To play the game, this program manually moves the mouse and clicks around, just like a real player would.  It's not ideal, because it could be interupted by random other things happening on the computer, but it's the only way to actually control Hearthstone, without risking being banned as a bot.

To start building the program, I have been testing different components of the data pipes involved.  All of those tests are in the component_testing directory.  Hopefully, everything should be working now, and platform independent.  It does take a while to to get all the requirments installed, so a good place to start is trying to run each of the components, and making sure all the supporting libraries and requirments are installed.  The next step will be getting everything to work together :)
