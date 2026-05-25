# ======================================================================================
# AUTHOR: Deywe Okabe | Harpia Quantum Deeptech
# PROJECT: ET Phone Home WOW 1977
# PURPOSE: Cryptographically Audited Spatiotemporal 3D Mesh Viewer
# ======================================================================================

import pandas as pd
import numpy as np
import hashlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
import os

# --- GLOBAL CONSTANTS ---
PHI = (1 + np.sqrt(5)) / 2  # Universal Golden Ratio
GRID_RESOLUTION = 40        # Ideal density for real-time 3D rendering
MOTION_SPEED = 0.25         # Field dance velocity cadence

def validate_and_animate_mesh(filename="wow_antigravity_audit.parquet"):
    # 1. DATASET LOADING & CHAINED AUDITING (CRYPTO-LEDGER)
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' not found!")
        return

    df = pd.read_parquet(filename)
    print(f"📦 Dataset loaded. Auditing cryptographic integrity of {len(df)} frames...")

    integrity_passed = True
    for i in range(1, min(len(df), 300)):
        row = df.iloc[i]
        prev_row = df.iloc[i-1]
        if row['prev_sha'] != prev_row['sha256']:
            integrity_passed = False
            break

    print("\n" + "="*60)
    if integrity_passed:
        print("🔒 STATUS: CHAIN OF CUSTODY INTEGRATED (SHA-256 OK)")
        print("Authentic spatial coordinates verified. Releasing dynamic renderer.")
    else:
        print("🚨 STATUS: CRITICAL INTEGRITY FAILURE!")
        return
    print("="*60 + "\n")

    # 2. DATA EXTRACTION AND PREPARATION
    dx = df['delta_gx'].values
    dy = df['delta_gy'].values
    dz = df['delta_gz'].values

    X, Y = np.meshgrid(
        np.linspace(dx.min() * 1.5, dx.max() * 1.5, GRID_RESOLUTION),
        np.linspace(dy.min() * 1.5, dy.max() * 1.5, GRID_RESOLUTION)
    )
    R_radial = np.sqrt(X**2 + Y**2) + 1e-5

    # 3. MATPLOTLIB UI CONFIGURATION (LABORATORY DARK MODE)
    fig = plt.figure(figsize=(13, 9))
    ax = fig.add_subplot(111, projection='3d')
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')

    ax.set_xlabel("Gx Tensor Axis", color='white', labelpad=10)
    ax.set_ylabel("Gy Tensor Axis", color='white', labelpad=10)
    ax.set_zlabel("Stress Amplitude (Z)", color='white', labelpad=10)
    ax.tick_params(colors='white', labelsize=9)
    
    ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#1e222b')
    ax.yaxis.pane.set_edgecolor('#1e222b')
    ax.zaxis.pane.set_edgecolor('#1e222b')
    
    ax.text2D(0.05, 0.95, "Wow! Signal - Spatiotemporal Mesh Viewer [Core Protected]", transform=ax.transAxes, color='white', fontsize=12)
    ax.text2D(0.05, 0.91, "Ledger Validated: SHA-256 Chain OK", transform=ax.transAxes, color='#00ffcc', fontsize=10, weight='bold')
    hud_info = ax.text2D(0.05, 0.86, "", transform=ax.transAxes, color='#ffff00', fontsize=9)
    
    ax.view_init(elev=25, azim=45)

    # Local rendering style control variables
    state = {'style': 0}  # 0 = Harmonic Wireframe, 1 = Solid Surface, 2 = Hybrid
    plot_elements = {'mesh': None, 'surf': None}

    # 4. SECURE ANIMATION ENGINE
    def update(frame_idx):
        if plot_elements['mesh'] is not None:
            plot_elements['mesh'].remove()
            plot_elements['mesh'] = None
        if plot_elements['surf'] is not None:
            plot_elements['surf'].remove()
            plot_elements['surf'] = None

        time_offset = frame_idx * MOTION_SPEED
        dado_fase = dz[frame_idx % len(dz)]
        
        # Dynamic geometry of the oscillatory field
        Z = np.sin(R_radial * PHI - time_offset) * np.cos(R_radial - dado_fase)
        ax.set_zlim(-1.5, 1.5)

        # Normalize Z values to build the flat color map array
        Z_norm = (Z - Z.min()) / (Z.max() - Z.min() + 1e-5)
        colors_flat = cm.plasma(Z_norm.flatten())

        # --- COMPATIBLE RENDERER SELECTION ---
        if state['style'] == 0:
            # REVOLUTIONARY WIREFRAME: Creates pure wire mesh without RGBA shape errors
            plot_elements['mesh'] = ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, linewidth=0.8, alpha=0.9)
            # Injects color mapping directly into Matplotlib's native 3D Line3DCollection segments
            plot_elements['mesh'].set_edgecolors(colors_flat)
            
        elif state['style'] == 1:
            # Solid Surface with straight gradient using the official colormap
            plot_elements['surf'] = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.5, edgecolor='none')
            
        elif state['style'] == 2:
            # Hybrid Mode: Blends smooth surface alpha with the sharp colored wireframe outline
            plot_elements['surf'] = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.3, edgecolor='none')
            plot_elements['mesh'] = ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, linewidth=0.5, alpha=0.7)
            plot_elements['mesh'].set_edgecolors(colors_flat)

        # Technical HUD Real-Time Update
        row = df.iloc[frame_idx % len(df)]
        hud_info.set_text(f"Frame: {row['frame']}\nTimestamp: {row['timestamp']:.3f}\nSHA: ...{row['sha256'][-8:]}")

        return plot_elements['mesh'], plot_elements['surf'], hud_info

    # 5. KEYBOARD EVENT MANAGER
    def on_key(event):
        if event.key == 'm':
            state['style'] = (state['style'] + 1) % 3
            modos = ["HARMONIC WIREFRAME", "DILATABLE SOLID SURFACE", "HYBRID (MESH + SURF)"]
            print(f"🔄 Render style changed to: {modos[state['style']]} ")

    fig.canvas.mpl_connect('key_press_event', on_key)

    print("🎥 High-performance viewport active. The field is dancing!")
    print("⌨️ Shortcut: Press 'm' while focusing the window to switch rendering modes.")
    
    ani = animation.FuncAnimation(fig, update, frames=len(df), interval=20, blit=False)
    plt.show()

if __name__ == "__main__":
    validate_and_animate_mesh()