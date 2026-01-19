import numpy as np
import dsp_utils as dsp

# ================= CONFIGURATION =================
# Raw data file path (Not included in repo)
DATA_FILE = "../data/Prac2_data.raw" 
FS = 2.4e6 

def run_bpsk_pipeline(data_burst):
    print("\n--- Processing BPSK ---")
    
    # 1. Coarse Frequency Sync
    freq_est = dsp.coarse_freq_sync(data_burst, FS, power_order=2)
    
    # 2. Carrier Recovery
    # tuned_phase = <HIDDEN>
    synced_data = dsp.apply_carrier_correction(data_burst, freq_est, phase_offset=0.0, fs=FS)
    
    # 3. Symbol Timing Recovery
    symbols = dsp.symbol_sync_sampling(synced_data, freq_clk=0.0, phase_clk=0.0, fs=FS)
    
    # 4. Phase Locked Loop (Costas)
    clean_symbols = dsp.phase_locked_loop(symbols, alpha=0.1, beta=0.01, loop_type='costas')
    
    # 5. Slicing & Decoding
    # Implementation hidden
    print("Pipeline Complete")

if __name__ == "__main__":
    # Load and process data bursts
    pass
