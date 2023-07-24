# The Four Trains Problem 🚂🚂🚂🚂

This Python code is a classic example of a multithreading and concurrency problem. It consists of 4 trains 🚂, each moving on a specific track and at certain sections of these tracks, they share the rail with other trains. The trains can control their speed individually, and this is done through a user interface.

## Code Description 🧾

The application is built using the `pygame` library to render the user interface and move the trains. `pygame_gui` is used to create the sliders that control the speed of each train.

Each train is an instance of the `Trem` class, which contains its x and y coordinates, color, rail it is moving on, and its speed. The direction of each train is controlled by a `direcao` attribute that can be "DIREITA", "ESQUERDA", "CIMA", or "BAIXO".

Trains move on rails, which are instances of the `Trilho` class. Each rail has its own position and color.

The movement of the trains is controlled by individual threads that call the `mover_thread` function, which in turn calls the `mover` function to change the train's position.

To prevent collisions when the trains arrive at shared sections of the rails, semaphores and locks are used. Each shared rail has its own lock, and a semaphore is used to control access to all shared sections.

## Code Operation 🏃‍♀️

When the program is started, it opens a window that shows the four trains and four rails, along with four sliders. Each slider controls the speed of a corresponding train.

Each train moves along its rail in a specified direction, and when it arrives at a shared section, it acquires a lock for that section. If the lock is available, the train will continue; otherwise, it will wait until the lock is released.

The speed of each train can be adjusted in real time with the sliders.

## Execution Instructions 🖥️

To run this program, you will need to have Python and the `pygame` and `pygame_gui` libraries installed. Then you can run the program with the following command:

```bash
python train.py
```
Replace `train.py` with the name of the file that contains the code.

Then you will see a window open with four trains and four sliders. You can adjust the speed of each train with the sliders.

---

![Interface Screenshot](/img/train.png)

*Above is a screenshot of the interface showing the four trains, the rails they move on, and the sliders for controlling each train's speed.*

## Team Members 
- [Morsinaldo Medeiros](https://github.com/Morsinaldo)
- [Thaís Medeiros](https://github.com/thaisaraujo2000)