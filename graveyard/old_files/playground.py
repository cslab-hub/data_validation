#%%
options_totake = ['Home','test','newtest']
# [lambda x: 'Home' if x == 'Home' else f"Chapter: {x}"]
lambda x: 'Home' if x == 'Home' else f"Chapter: {x}"


[f"Chapter {x}: {y}" if y != "Home" else y for x,y in enumerate(options_totake)]
# [lambda x,y: "Home" if x == "Home" else f"Chapter {x}: {y}"]

#%%

# [(x,t)[0] for t in range(len(options_totake))]


[(x,t) for x,t in enumerate(options_totake)]

#%%
['Home' if y == 'Home' else f"Chapter {x}:{y}" for x,y in enumerate(options_totake)]
# %%
