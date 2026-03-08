#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.

import numpy as np
import matplotlib.pyplot as plt

def plot_constellation(chaindata, constellation_color='magenta', title="Prime Constellation"):
    # Deep space black for a cosmic background (Hex code: #010111)
    space_background = '#010111'
    plt.figure(figsize=(10, 10), facecolor=space_background)

    # Polar coordinate plot
    ax = plt.subplot(111, projection='polar', facecolor=space_background)

    # --- Data Processing ---
    n_arr = np.array(chaindata)

    # 1. Radius r (Logarithmic space)
    ln_n = np.log(n_arr)
    r = ln_n - ln_n[0]

    # 2. Angle theta (2 * pi * Logarithmic space)
    theta = 2 * np.pi * ln_n

    # --- Rendering: Drawing the glowing constellation ---

    # A. Connecting lines (Constellation lines)
    ax.plot(theta, r, linestyle='-', color=constellation_color,
            linewidth=1.2, alpha=0.5, label='Constellation Lines')

    # B. Glowing stars (Layering markers)
    # 1st layer: Large halo (highly translucent)
    ax.scatter(theta, r, marker='*', s=350, facecolors=constellation_color, edgecolors='none', alpha=0.1)

    # 2nd layer: Medium glow (slightly translucent)
    ax.scatter(theta, r, marker='*', s=150, facecolors=constellation_color, edgecolors='none', alpha=0.3)

    # 3rd layer: Small core (opaque and whitish)
    ax.scatter(theta, r, marker='*', s=50, facecolors='white', edgecolors=constellation_color, alpha=0.8, label='Stars')

    # --- Visual Adjustments ---
    ax.set_title(title, color='white', pad=20, fontsize=18, fontweight='bold', fontname='serif')

    # Extremely faint grid lines
    ax.grid(True, color='gray', linestyle=':', alpha=0.1)

    # Completely hide labels
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    plt.tight_layout()
    plt.show()

# --- Execution Data (Newly discovered L9 Collatz-type prime chain) ---
chaindata = [
    35014031359,
    52521047039,
    78781570559,
    118172355839,
    177258533759,
    265887800639,
    398831700959,
    598247551439,
    897371327159
]

# --- Draw the Collatz Constellation (Pentagram) ---
plot_constellation(
    chaindata,
    constellation_color='magenta',
    title="Collatz Prime Constellation (Pentagram)"
)


# In[ ]:




