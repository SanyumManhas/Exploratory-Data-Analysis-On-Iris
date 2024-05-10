#Exploratory Data Analysis on Iris Dataset.. Menu Driven with Different Statistics Shown
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pygame as py

df = pd.read_csv("iris.csv")

py.init()
width = 300
height = 200
screen = py.display.set_mode((width,height))
py.display.set_caption("EDAonIris")
running = True

def draw_Screen(screen):
    screen.fill((0,0,0))
    py.font.init()
    font = py.font.SysFont("comicsans", 15)
    label = font.render('1: CountPlot', 1, 'white', 'blue')
    label2 = font.render('2: ScatterPlot', 1, 'white', 'blue')
    label3 = font.render('3: PairPlot', 1, 'white', 'blue')
    label4 = font.render('4: HeatMaps', 1, 'white', 'blue')
    label5 = font.render('5: DistPlot', 1, 'white', 'blue')
    
    screen.blit(label,(0,0))
    screen.blit(label2,(0,25))
    screen.blit(label3,(0,50))
    screen.blit(label4,(0,75))
    screen.blit(label5,(0,100))
    py.display.update()

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_1:
                sns.countplot(x="species", data=df, palette=['blue','red','orange'])
                plt.tight_layout()
                plt.show()
            if event.key == py.K_2:
                # sns.scatterplot()
                # plt.legend(bbox_to_anchor=(0, 1), loc=2) 
                # plt.show()
                # d = {'color': ['r', 'b']}
                plot = sns.FacetGrid(df, hue="species")
                plot.map(sns.scatterplot, x="petal_length", y="petal_width",data=df)

                plot = sns.FacetGrid(df,hue="species")
                plot.map(sns.scatterplot, x="sepal_length", y="sepal_width",data=df)
                plt.tight_layout()
                plt.show()

            if event.key == py.K_3:
                sns.pairplot(df, hue="species")
                plt.tight_layout()
                plt.show()
            if event.key == py.K_4:
                df= df.apply(pd.to_numeric, errors="coerce")
                sns.heatmap(df.corr(method="pearson"),annot=True)
                plt.tight_layout()
                plt.show()
            if event.key == py.K_5:
                plot = sns.FacetGrid(df, hue="species")
                plot.map(sns.distplot, "sepal_length").add_legend()
                plot = sns.FacetGrid(df, hue="species")
                plot.map(sns.distplot, "sepal_width").add_legend()
                plot = sns.FacetGrid(df, hue="species")
                plot.map(sns.distplot, "petal_length").add_legend()
                plot = sns.FacetGrid(df, hue="species")
                plot.map(sns.distplot, "petal_length").add_legend()
                plt.tight_layout()
                plt.show()

            
        draw_Screen(screen)
py.display.quit()
            






