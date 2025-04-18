# Pizzbot

### About
A conversational assistant chat with on my personal website.

### Getting Started
> install first [Rasa](https://rasa.com/docs/rasa/user-guide/installation/#installation)


### Train the chatbot
```
rasa train
```

### Test chatbot
```https://github.com/jankomp/HMD-AJ
rasa test
```

### Talk to chatbot
```
rasa shell
```
In case it doesn't predict any response please use specifying the model folder:
```commandline
rasa shell -m models/
```

## Interactive Rasa Tool
No more available for free users
Install first [Rasa X](https://rasa.com/docs/rasa-x/)
```
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

```
rasa x
```


## TODO:
- update domain file
- remove useless actions
- make sure nlu train works
- make sure policy train works
