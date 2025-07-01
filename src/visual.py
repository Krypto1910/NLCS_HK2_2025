import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import mplcursors

def main(s, Checkpoints):
    #check if input is empty
    if len(s) == 0:
        return None

    #init the sets of x and y
    x = [i for i in range(len(s) + 1)]
    y = [0]
    for i in range(len(s)):
        if s[i] == '_':
            y.append(y[-1])
        elif s[i] == '\\':
            y.append(y[-1] - 1)
        elif s[i] == '/':
            y.append(y[-1] + 1)

    #convert to numpy array
    x = np.array(x) 
    y = np.array(y)

    #create figure with scale (9:4.5)
    fig, ax = plt.subplots(figsize=(9, 4.5))

    #set smallest division
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(1))

    #grid layout
    ax.grid(True, which="major", linestyle="-", linewidth=0.5, color="gray", alpha=0.6)
    ax.grid(True, which="minor", linestyle=":", linewidth=0.3, color="gray", alpha=0.3)

    #set responsive size
    if len(s) <= 10:
        temp_markersize = 8
        temp_fontsize = 10
    elif len(s) <= 20:
        temp_markersize = 6
        temp_fontsize = 8
    else:
        temp_markersize = 5
        temp_fontsize = 6

    #draw line
    line = ax.plot(x, y, color="black", linewidth=2, marker="o", markerfacecolor="#FF6F00", markeredgecolor="black", markersize=temp_markersize)

    #set limits for x and y axis
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y) + 1)

    #adjust the position of the plot
    plt.subplots_adjust(left=0.06, bottom=0.115, right=0.95, top=0.85)

    #hide the border
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_color("gray")
    ax.spines['left'].set_alpha(0.6)
    ax.spines['left'].set_linewidth(0.5)  
    ax.spines['right'].set_color("gray")
    ax.spines['right'].set_alpha(0.6)
    ax.spines['right'].set_linewidth(0.5)  

    #hide axis's label
    ax.set_xticklabels([])  
    ax.set_yticklabels([]) 
    ax.tick_params(axis='x', which='both', bottom=False, top=False) 
    ax.tick_params(axis='y', which='both', left=False, right=False)   

    #color mountain
    ax.fill_between(x, y, min(y), where=(x >= 0) & (x <= len(s)), color="brown", alpha=0.8)

    #algo visualization
    total_flood_volume = 0 
    while Checkpoints:
        #get first pair of 
        (start_index, end_index) = Checkpoints.popleft()  

        #color flooded areas
        ax.fill_between(x, y[start_index], y, where=(x >= start_index) & (x <= end_index+1), color="deepskyblue", alpha=0.8)
        
        #show total flood volume
        total_flood_volume += (end_index - start_index)
        ax.set_title(f"Total Flood Volume: {total_flood_volume}", fontsize=12, fontweight="bold", color='yellow', bbox=dict(facecolor='black', alpha=0.8))

        #show pairs of checkpoints
        temp_startpoint = ax.text(start_index+0.5, y[start_index], start_index, ha='center', fontsize=temp_fontsize, fontweight="bold", color='white', bbox=dict(facecolor='black', alpha=0.8, boxstyle="round,pad=0.2"))
        temp_endpoint = ax.text(end_index+0.5, y[end_index+1],  end_index, ha='center', fontsize=temp_fontsize, fontweight="bold", color='white', bbox=dict(facecolor='black', alpha=0.8, boxstyle="round,pad=0.2"))
        
        #animation
        plt.pause(0.75)

        #remove text
        temp_startpoint.remove()  
        temp_endpoint.remove()
        
    #show index on hover
    cursor = mplcursors.cursor(line, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"index = {int(sel.target[0])}"))

    plt.show()

    return plt

if __name__ == "__visual__":
    main()