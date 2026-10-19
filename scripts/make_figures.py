#!/usr/bin/env python3
"""Regenerate main paper Figures 2–4 as SVG/PDF from aggregate, frozen evidence."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

R=Path(__file__).resolve().parents[1]
OUT=R/'figures';OUT.mkdir(exist_ok=True)
A=R/'results/olist'

def save(fig,name):
    fig.tight_layout()
    fig.savefig(OUT/f'{name}.svg',format='svg',bbox_inches='tight')
    fig.savefig(OUT/f'{name}.pdf',format='pdf',bbox_inches='tight')
    plt.close(fig)
    print('saved',name)

def ci_plot(ax,df,labcol,dcol,lcol,hcol,horizontal=False):
    v=df[dcol].to_numpy(); lo=v-df[lcol].to_numpy(); hi=df[hcol].to_numpy()-v
    yy=list(range(len(df)))
    if horizontal:
        ax.errorbar(v,yy,xerr=[lo,hi],fmt='o',capsize=3)
        ax.axvline(0,linewidth=0.8);ax.set_yticks(yy,df[labcol]);ax.invert_yaxis()
        ax.set_xlabel('Paired Brier difference')
    else:
        ax.errorbar(yy,v,yerr=[lo,hi],fmt='o',capsize=3)
        ax.axhline(0,linewidth=0.8);ax.set_xticks(yy,df[labcol]);ax.set_ylabel('Paired Brier difference')
    ax.grid(alpha=0.18,axis='x' if horizontal else 'y')

m=pd.read_csv(A/'four_origin_s1.csv').sort_values('Origin')
fig,ax=plt.subplots(figsize=(6.2,3.15));ci_plot(ax,m,'Origin','BrierDelta','BrierCI_low','BrierCI_high')
ax.set_title('S1: Expanding minus Raw across four origins')
save(fig,'Figure2_four_origins')

c=pd.read_csv(A/'calendar_encoding_all_origins.csv');c=c[c.Origin.eq('O2')].sort_values('Version')
fig,ax=plt.subplots(figsize=(6.2,3.15));ci_plot(ax,c,'Version','BrierDelta','BrierCI_low','BrierCI_high')
ax.set_title('O2: sensitivity to calendar encoding')
save(fig,'Figure3_O2_encoding')

p=pd.read_csv(A/'window_s1_contrasts.csv').copy();p['Comparison']=p.Origin+': '+p.Contrast
p=p.sort_values(['Origin','Contrast'])
fig,ax=plt.subplots(figsize=(8.1,4.6));ci_plot(ax,p,'Comparison','BrierDelta','BrierCI_low','BrierCI_high',horizontal=True)
ax.set_title('S1: historical-window definitions')
save(fig,'Figure4_window_definitions')
