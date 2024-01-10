# BlackJack counting agent

A BlackJack counting agent which utilises machine learning to apply card counting in BlackJack.

# BlackJack hand 

The inital function tests that the blackjack envirmoment is able to take cards and find the total of the hand

![image](https://github.com/fraser-steven/blackjack/assets/92175405/b394ed9e-5f79-4b0f-962d-3613ba841dba)

# Basic Strategy 

The function takes all the information about the players hand and begins to run through the hard coded basic strategy options for the agent depending on the player card.  
![image](https://github.com/fraser-steven/blackjack/assets/92175405/f1bff9a0-6d97-466e-9829-eb68cb06a845)                                  
Here is an example of the the hard coded options 
![image](https://github.com/fraser-steven/blackjack/assets/92175405/630f5695-6aee-4fc2-976e-fa4de1d1b61b)

# Gathering the testing data set 

 A BlackJack enviroment is established as to gather information from the already hard coded basic strategy to form a data set for the Nureal network to learn from. It is simulated over 100,000 hands and the hand total, dealer card and outcome of each hand is recored and put into septerate
 ![image](https://github.com/fraser-steven/blackjack/assets/92175405/d5e68795-b2e0-43eb-99fe-af290e965cb1)

# Neural Network 

The Nueral Network was then trained on the 100,000 hands that were previously played. 
![image](https://github.com/fraser-steven/blackjack/assets/92175405/5a7d00e7-08fe-45b8-9b11-786be91a1ca4)

This created an agent that was agressive in it's strategy and prodcued a win rate of 46.7%
![image](https://github.com/fraser-steven/blackjack/assets/92175405/564aed88-7cba-400f-88d3-df8955e3ffdc)



