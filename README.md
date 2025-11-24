# 🎮 Kira Game - Bug Fixing Exercise

## About the Project

This is a simple 2D survival game where you control a character that must avoid vampires and shoot them down. The game includes:
- Player movement (arrow keys)
- Shooting mechanics (spacebar)
- Enemies that chase the player
- Health, score, and timer system
- Game over screen

**However, the code is broken!** There are **10 errors** that prevent the game from working correctly.

## Your Task

Fix all 10 errors in the code to make the game playable. Each error is marked with a comment `# ERROR X:` that tells you what's wrong in that function.

## 📍 Where to Look for Errors

### **ability.py** - 3 errors
- **ERROR 1** in `Bullet.update()`: Bullets are moving in the wrong direction (check the arithmetic operator)
- **ERROR 2** in `Bullet.is_alive()`: Bullets expire immediately instead of after 3 seconds (wrong comparison operator)
- **ERROR 3** in `Ability.update_bullets()`: The function removes alive bullets instead of dead ones (wrong condition)

### **character.py** - 2 errors
- **ERROR 4** in `Character.move()`: Attribute has a typo in the name (extra letter)
- **ERROR 5** in `Character.shoot()`: Missing one required argument when calling the ability's shoot method

### **enemy.py** - 3 errors
- **ERROR 6** in `Mob.__init__()`: Ability is assigned as a class instead of an object instance (missing parentheses)
- **ERROR 7** in `Mob.move()`: Attribute has a typo in the name (extra letter)
- **ERROR 8** in `Mob.update()`: Wrong attribute name used - Character uses `isAlive` not `alive`

### **main.py** - 2 errors
- **ERROR 9** in main game loop: Timer variable is reset every frame instead of once before the loop (wrong placement)
- **ERROR 10** in player movement: Missing the second required argument in the move() function call

## 💡 How to Fix

1. Open each file and find the `# ERROR X:` comments
2. Read the explanation of what's wrong
3. Fix the error on the line(s) near the comment
4. Run the game to test if that error is fixed
5. Move to the next error

## ✅ Expected Behavior When Fixed

- Player moves smoothly with arrow keys
- Bullets shoot in 4 directions when you press spacebar
- Bullets disappear after 3 seconds
- Enemies spawn and chase the player
- Health decreases when enemies touch you
- Score increases when bullets hit enemies
- Timer counts up from 0
- "Game Over" appears when health reaches 0

Good luck! 🚀
