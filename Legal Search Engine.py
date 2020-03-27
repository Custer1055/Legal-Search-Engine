from tkinter import*
import random 
import time;


root = Tk()
root.geometry("1600x800+0+0")
root.title("Whakaty Legal Search Engine")

text_Input = StringVar()
operator

#grid search
    model = WhakatyClassifier()
    searching_rate = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.3]
    param_grid = dict(searching_rate=searching_rate)
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=7)
    grid_search = GridSearchCV(model, param_grid, scoring="neg_results_", search=-0, cv=kfold)
    grid_result = grid_search.fit(X, y)

# search results
    print(); print("Saflii: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.Saflii_results_['mean_test_score']
    stds = grid_result.Safflii_results_['std_test_score']
    params = grid_result.Saflii_results_['params']

# search results
    print(); print("LexisNexis: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.LexisNexis_results_['mean_test_score']
    stds = grid_result.LexisNexis_results_['std_test_score']
    params = grid_result.LexisNexis_results_['params']

# search results
    print(); print("Juta Law: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.Juta Law_results_['mean_test_score']
    stds = grid_result.Juta Law_results_['std_test_score']
    params = grid_result.Juta Law_results_['params']

# search results
    print(); print("Sabinet: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.Sabinet_results_['mean_test_score']
    stds = grid_result.Sabinet_results_['std_test_score']
    params = grid_result.Sabinet_results_['params']

# search results
    print(); print("FLD: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.FLD_results_['mean_test_score']
    stds = grid_result.FLD_results_['std_test_score']
    params = grid_result.FLD_results_['params']

    for mean, WhakatyClassifier, param in zip(means, stds, params):
	     print("%f (%f) with: %r" % (mean, stdev, param))

Tops = Frame(root, width = 1600, height= 50, bg="powder blue" relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height= 700, bg="powder blue" relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height= 700, bg="powder blue" relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

lblInfo = Label (Tops, font=('arial' ,50, 'bold'),text="Whakaty Legal Search Engine" ,fg="steel Blue" ,bd=10 ,anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label (Tops, font=('arial' ,20, 'bold'),text="localtime" ,fg="steel Blue" ,bd=10 ,anchor='w')
lblInfo.grid(row=1, column=0)

def btnClick(CaseLaw):
    global operator
    operator=operator + str(search)
    text_Input.set(operator)

def btnClick(Journals):
    global operator
    operator=operator + str(search)
    text_Input.set(operator)

def btnClick(Legislation):
    global operator
    operator=operator + str(search)
    text_Input.set(operator)

def btnClick(Commentary):
    global operator
    operator=operator + str(search)
    text_Input.set(operator)


txtDisplay = Entry(f2, font=('arial' ,20, 'bold'), titletext=Saflii, bd=30, insertwidth=4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

search=button(f2, padx=16, pady=16, bd=8, fg='steel Blue', font=('arial',20,'bold'), textVarChar="98", command=lambda: btnClick(7)).grid(row=2,column=0)

txtDisplay = Entry(f2, font=('arial' ,20, 'bold'), titletext=LexisNexis, bd=30, insertwidth=4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

search=button(f2, padx=16, pady=16, bd=8, fg='steel Blue', font=('arial',20,'bold'), textVarChar="98", command=lambda: btnClick(1)).grid(row=3,column=0)

txtDisplay = Entry(f2, font=('arial' ,20, 'bold'), titletext=Juta Law, bd=30, insertwidth=4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

search=button(f2, padx=16, pady=16, bd=8, fg='steel Blue', font=('arial',20,'bold'), textVarChar="98", command=lambda: btnClick(1)).grid(row=4,column=0)

txtDisplay = Entry(f2, font=('arial' ,20, 'bold'), titletext=Sabinet, bd=30, insertwidth=4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

search=button(f2, padx=16, pady=16, bd=8, fg='steel Blue', font=('arial',20,'bold'), textVarChar="98", command=lambda: btnClick(1)).grid(row=5,column=0)

txtDisplay = Entry(f2, font=('arial' ,20, 'bold'), titletext=FLD, bd=30, insertwidth=4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

search=button(f2, padx=16, pady=16, bd=8, fg='steel Blue', font=('arial',20,'bold'), textVarChar="98", command=lambda: btnClick(1)).grid(row=6,column=0)



root.mainloop()