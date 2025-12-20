# Wordle

This is a rendition of Wordle with the goal of being fully modular.

## Modular/Decoupled Design

I want the Wordle engine and the rules to be independent 
from each other. This will allow rules to be added and removed at a
given time without breaking the engine. 
This makes it easy for developers to add additional modes and rules to the
game that we know a love, Wordle.

## Example

Let's say a developer wants to add an additional element to the game.
Well that's fine that can be another 'if' statement or some sort of 
conditional. Now what if the developer wants to add one hundred rules? One thousand rules?
Well that wouldn't be so easy.. No one wants to refactor the entire engine.
This Wordle is meant to be fun while teaching you about modular and independent design.
Modular + Extensible = Ressiliency and Beautiful Design.
