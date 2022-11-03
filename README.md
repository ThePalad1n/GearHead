Team Gear Heads

Abstract
	This paper aims to outline the work and processes needed to achieve the eventual goal. The group intends to create a data structure named “Train of Gears”, the goal of the project, this data structure will be used to encrypt data from user input. The data structure will use lists to simulate gears rotating along one another and will swap data between these “gears” with each rotation. These “gears” or rotating lists will be able to “turn” in both directions in order to transfer data along the first and last index.. 
	      
Goal
  “Train of Gears” is intended to be a data structure based on a Binary Search Tree(BST). This is a data structure that will be able to encrypt user input by swapping elements between lists. In this case, the user input can be converted into a list and will be inserted as the root node of the tree. Based on the number of elements in the aforementioned list, two other lists or “gears” will be formed. The first and last elements of these gears will be swapped in order to encode or decode a message. Decoding, however, can only be done using a special passcode provided by the user. Without the password, the gears will stay locked and the message will remain encoded.

Objectives
  Create a gear data structure via making a circular list.
    Gear Data Structure Attributes
    name
    ag
    locked
  Gear Data Structure Methods
    nameGear()
      Give the name attribute a value
    addTooth()
      Add value to gear
    rotR()
      Rotate Right
    rotL()
      Rotate Left
    lock()
      Can no longer rotate
    free()
      Can rotate again
    printGear()
      Prints: [‘name’,[values]]
      
  Create the gear train data structure using the gear data structure as nodes
    In the train of gears, the gears should interact with one another.
     Interactions should be rotation and data transfer
     
    Gear Train Data Structure Methods
    isLocked()
      If a gear within the tree is locked this method should return the name of that gear.
    pRotL()
      The parent gear will rotate left causing the two immediate child gears to rotate right.
      Data transfer should happen on the first and last index after every rotation.
    pRotR()
      The parent gear will rotate right causing the two immediate child gears to rotate left.
      Data transfer should happen on the first and last index after every rotation.
    pLock()
      Will lock the parent gear.
    pFree()
      Will free the parent gear after password entry
    setPass()
      Sets new password after entry of old password
