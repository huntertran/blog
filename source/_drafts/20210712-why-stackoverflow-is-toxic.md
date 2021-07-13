https://stackoverflow.com/questions/63118067/how-can-i-remove-vs-code-debugger/63118193#63118193

Possible duplicate: How to disable 'Debug' from showing in package.json - https://stackoverflow.com/questions/62358131/how-to-disable-debug-from-showing-in-package-json

Anyway, that is just a function for you to quickly launch the debugging session. Nothing added to your code.

When you press "debug", because you don't specify which script to run, VSCode shows you a list of options for you to choose. Use the up and down buttons to select.

If you hover your mouse a script, a small "tooltips" appear, click on it to run the script under the mouse.

![image](https://user-images.githubusercontent.com/4468525/125376610-64f05a80-e359-11eb-8284-f68120444364.png)

In this picture, if I click Run Script, the terminal windows will run npm run compile

Comments:

Don't want to downvote, because it's valuable information to new users, but it would be good to at least address the main question of How can I remove VS code debugger?, in my opinion anyways – soulshined Jul 27 '20 at 16:17

I think OP is thinking VSCode adds something to the code, therefor asking for a way to "remove" it. Also, OP don't familiar with the VSCode dialogue box, as he misunderstands it with a search box. So I assumed OP is new to vscode. – Tuan Tran Jul 27 '20 at 20:13

It technically is adding something to the [editor] code. I'm not saying your answer isn't helpful, it just doesn't address the question. They want to remove it, and there is a way to do so – soulshined Jul 27 '20 at 20:21

thank you your answer! Sorry for my bad asking, Im very new to VS code. The reason that I said I want to remove is , if I build up my react-native app with expo, command expo start, Error happens.. Expo open browser and expo says "Error Loading DebugTools". before yesterday, I never see this error, But debug function appeared, Expo start showing error.. I did run app from small tooltips you told me, app build with no problem. Actually I really want to remove it but my heavy problem disappeard. Anyway Thanks! – Odayan Jul 27 '20 at 23:22

By the way, is there some way to remove it? (Im saying no to remove from VS CODE, I just want to disappear it) Or this is always appear everyone's code? – Odayan Jul 27 '20 at 23:28

@Odayan you can review the comment i posted on your question. This question is essentially a duplicate – soulshined Jul 27 '20 at 23:37

@Odayan I think something wrong with the code itself, not the vscode. You can try to run your react-native app from a command prompt without vscode. Otherwise, you can always ask a new question. – Tuan Tran Jul 28 '20 at 0:28

@Tuan I could understand what you advised! I edit VS code setting, script debugger => never I could make debugger disabled!! Thank you so much! – Odayan Jul 28 '20 at 3:35

![image](https://user-images.githubusercontent.com/4468525/125377147-725a1480-e35a-11eb-819c-292473d49551.png)

You cannot delete the accepted answer!

