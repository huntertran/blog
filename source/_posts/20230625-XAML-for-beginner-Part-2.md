---
title: XAML for beginner - Part 2
tags:
  - XAML
  - Windows Store App
categories:
  - XAML
date: 2023-06-25 10:31:36
---

This is part 2 of post "XAML for beginner". In this part, I will introduce the list control: `ListBox`, `GridView`. Also included a super short introduction to MVVM and data binding in XAML.

<!-- more -->

# 1. `ListBox` control

`ListBox` allows you to display a list of item. Each item in the list box would have the same type, with the same UI.

For example, "top 30 most stream songs on Spotify" is a kind of data that we could use `ListBox` to display.

![listbox](/images/2023/06/7.png)

## 1.1. `ListBox` property: `ItemsSource`

`ItemsSource` is the source for the items that you want to display on the UI. `ItemsSource` can be a object of type `List`, or type `ObservableCollection`. We will talk a bit about this property in DataBinding section

## 1.2. `ListBox` property: `SelectedIndex` and `SelectedItem`

When user select an item on the list box, both `SelectedIndex` and `SelectedItem` property will be updated with the corresponding data. The index is start from 0.

# 2. DataBinding

If you familiar with Angular, React, or Vuejs, you probably know what is data binding. In short, the data you have in memory will automatically displayed on UI. If the data got updated (by calculation, replaced from a call to API, user changed it), the UI will update the view as well.

There are 3 types of `DataBinding`, which is `One time binding`, `One way binding` and `Two way binding`

* In `One time binding`, the data got prepared, then send to the UI one time only, usually when you load the view.
* In `One way binding`, whenever the data updated in memory, the UI will update it view too. But when the data on UI updated (think of the user modify the data in a text box), the data in memory is not getting updated.
* In `Two way binding`, the data between UI and memory are kept in sync.

## 2.1. Design Pattern for DataBinding - MVVM

> This is optional, there are multiple way for you to "bind" the data with UI.

Microsoft invented and advocated for the MVVM pattern. They support this pattern and use it everywhere in there newer first-party applications, especially the one that you can download from Windows Store (WPF, UWP apps)

> MVVM stands for Model-View-ViewModel. This pattern is a variation of Martin Flower's Presentation design pattern.

In short, `Model` is the model classes that define your data. In the Spotify example above, the model class could be like this:

```csharp
public class Song
{
    // simplified for the blog post
    public int Id { get; set; }
    public string Name { get; set; }
    public DateTime DatePublished { get; set; }
}
```

`ViewModel` is a special class that was use as a converter. It converts the data in model into something that can be displayed on screen. On the `ViewModel` class, you would need to handle the update mechanism of the data you have in `Model` to `View`.

In other to do this, the `Model` would need to implement the interface `INotifyPropertyChanged`, or `INotifyCollectionChanged`.

`INotifyPropertyChanged` is for update the property of the model. `INotifyCollectionChanged` is for update the list if you add/remove/re-arrange the item in the list. `ObservableCollection` already implemented the `INotifyCollectionChanged` for you.

Using the same Spotify example, the `ViewModel` would be something like this

```csharp
public class MainViewModel
{
    public ObservableCollection<Song> SongList { get; set; }
}
```

Now you just need to populate the data for your song list, and put that in `DataContext` of the `MainWindow.xaml` page

## 2.2. `DataContext`

`DataContext` is the way you tell the page which data to display on UI. You can set the data context by assigning the `DataContext` property of `Window` or `Page`. 

The code for the `MainWindow.xaml.cs` should look like this:

```csharp
public partial class MainWindow : Window
{
    public MainViewModel MainVm = new MainViewModel();

    public MainWindow()
    {
        // Here I set the Window's data context
        DataContext = MainVm;
        MainVm.SongList = new ObservableCollection<Song>
        {
            new Song(1, "Test 1", DateTime.UtcNow.AddDays(1)),
            new Song(2, "Test 2", DateTime.UtcNow.AddDays(2)),
            new Song(3, "Test 3", DateTime.UtcNow.AddDays(3)),
            new Song(4, "Test 4", DateTime.UtcNow.AddDays(4))
        };

        InitializeComponent();
    }
}
```

## 2.3. `ItemTemplate` of ListBox

You would need to declare a "template" for your data in `ListBox`. This is called `ItemTemplate`.

Modify your XAML code as follow:

```xml
<ListBox ItemsSource="{Binding SongList}">
    <ListBox.ItemTemplate>
        <DataTemplate>
            <Grid>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="20" />
                    <ColumnDefinition Width="*" />
                </Grid.ColumnDefinitions>
                <Grid.RowDefinitions>
                    <RowDefinition Height="5*" />
                    <RowDefinition Height="5*" />
                </Grid.RowDefinitions>
                <TextBlock Grid.Row="0"
                           Grid.RowSpan="2"
                           Grid.Column="0"
                           Text="{Binding Id}" />
                <TextBlock Grid.Row="0"
                           Grid.Column="1"
                           Text="{Binding Name}" />
                <TextBlock Grid.Row="1"
                           Grid.Column="1"
                           Text="{Binding DatePublished}" />
            </Grid>
        </DataTemplate>
    </ListBox.ItemTemplate>
</ListBox>
```

In this xaml, we set `ItemsSource={Binding SongList}`, which is the name of the property in the `MainViewModel` class. Later, we bind each `TextBlock` to the property of `Song` class.

Now if you run the application, you should see something like this:

![wpf listbox](/images/2023/06/8.png)

It's ugly, but hey it worked ;)

# `GridView` view mode

`GridView` displays data as a table, with headers and rows. You would need to use `GridView` with `ListView` control, in `View` property

```xml
<ListView ItemsSource="{Binding SongList}">
    <ListView.View>
        <GridView AllowsColumnReorder="true"
                  ColumnHeaderToolTip="Song list">
            <GridViewColumn DisplayMemberBinding="{Binding Id}"
                            Header="ID" />
            <GridViewColumn DisplayMemberBinding="{Binding Name}"
                            Header="Name" />
            <GridViewColumn DisplayMemberBinding="{Binding DatePublished}"
                            Header="Published date" />
        </GridView>
    </ListView.View>
</ListView>
```

Run the application, then you will see something like this:

![wpf gridview](/images/2023/06/9.png)

# Source Code

Source code for this whole sample is available at: [SampleWPF on Github](https://github.com/huntertran/SampleWPF)

I hope you can learn something new about XAML today. See you in next post