def args_kwargs(*banana, **kwargs):
    print("kwargs: ", kwargs)
    print("args:", banana)


args_kwargs("love it?", hell = "yes", heaven = "yes, too")