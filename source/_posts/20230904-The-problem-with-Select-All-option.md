---
title: The problem with Select All option
tags:
  - ui
categories:
  - UI
date: 2023-09-04 16:59:10
---


In a list of checkbox, it's convenient to have a `Select all` option at the top. But this option is not as simple as it seems. Let's walk through the ideas, and the logic behind it.

<!--more-->

# 1. The idea of Select All

You've got an email. It is a spam mail from an online store that you've never heard of. The other 50 mails in your inbox is the same. You want to delete all of them. Selecting each of these email is taking too much time.

Luckily, we all familiar with that `Select all` checkbox on top

![Select all checkbox](/images/2023/09/001.png)

# 2. The complication behind Select All

How can something as simple as a select all option can get complicated? Because we didn't know what is the expectation of the users. Everyone has their own ideas and expectation on how a certain function works.

So what are the expectation of `Select All` function?

* Does the `Select All` has 3 states? Checked - Unchecked - Intermediate (between checked and unchecked)
* If there are multiple pages of item, does the item on other pages affected too?
* If there are only 1 item in the list, do you need to show the `select all` option?

Also, there is some other expectations, from the point of view of a developer

* Is `Select All` option an option from the data?
    * If it is a special option and not present in the data, should it be styled the same way as other option?
* Should you put the `Select All` option on the top of the list

> Obviously, the below implementation of select all in Angular doesn't looks good
> 
> ![Select all as a special option](/images/2023/09/002.png)
>
> From this [StackBlitz](https://stackblitz.com/edit/angular-material-select-all-checkbox?file=src%2Fapp%2Fapp.component.html)

Each of these expectation add some complication to the existing code. For some points, you would need to change the model of the data as well to support it.

# 3. What user expected from `Select All`

As a developer, I would like to give my users an adequate amount of information, not too little (so they would need to infer), not too much (so they would lost in all the non-necessary information). Here is my list

1. Has 3 states
    1. If all items selected: Checked
    2. If some items selected: Intermediate
    3. If no items selected: Unchecked
2. Only affect the current page
    1. Will notify user that only items of the current page are selected.
    2. Provide a way to select all item
3. Hide if there is only `n` items in the list. `n` could be 1, 2, or 5
4. On top of the list, and sticky too

# 4. Implementation logic

## 4.1. Approach 1: Select All as an option in data

Meaning that you have a list, let's say `Steak`, `Pizza`, and `Tacos`. The `Select All` would be an item in that list too.

Pros:
* Implementation once, reuse as many as you like (if your language of choice support inheritance)
* No need to special care on styling. The option is rendered just like a regular item

Cons:
* Show/Hide it could be a problem
* Extra noise/pollution in the model class
* May not be able to use the built-in interation to loop through items

## Approach 2: Select All as an special option in the view

Meaning that when render the view, you "inject" the `select all` option and it's logic

Pros:
* Pure data model
* You can customize the behavior

Cons:
* You need to style the option to match with other item (could not be a problem if you use the default style)
* Need to re-implement for each list (could be a lot of work)
* May hit on performance (the state of the `Select all` checkbox depend on the state of all other items)

I'm sure that there are other hidden problem with each approach, depending on the frontend framework you're using, the data you're handling, and a bunch of other things that not in the picture yet.

Choose wisely, my fellow developers

![Choose wisely](/images/2023/09/003.webp)