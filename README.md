# SE.Core.Achievement
This is the library for achievements.

## Getting Started
 - Download the latest source code from GitHub app

## Prerequisites
For correct conducting the app, you need:
```
Newtonsoft.Json library
```

## Describing
The statis class is for saving and loading achievements
```
Config.cs
```
The class is for the model of achievement
```
AchievementModel.cs
```
The class is for the main logic for controlling achievements
```
AchievementSettings.cs
```
### Config.cs
The method is for loading data from json at the start
```
public static void Load()
```
The method is for saving edits to json
```
public static void Save()
```
The method is for loading achievements from json
```
public static void LoadAchievements()
```

### AchievementModel.cs
The event fires when the current amount of achievement score is changed. 
```
public event EventHandler CurrentAmountChanged;
```
The event fires when the current amount is up to the required amount of achievement and the achievement becomes available for user.
```
public event EventHandler BecomeAvailable;
```


### AchievementSettings.cs
The property of achievement models
```
public ObservableCollection<AchievementModel> Achievements
```
The method is for adding a new element to achievement model collection
```
public void Add(string title, string description, BitmapImage picture, int required)
```
The method is for remove a selected element 
```
public void Remove(AchievementModel model)
```
The method is for conducting achievement score on value variable for element 
```
public void Counter(int id, int value)
```
The method is for choosing a picture for a new achievement
```
public string ChoosePic()
```
