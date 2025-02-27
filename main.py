from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from rapidfuzz import process, fuzz

app = FastAPI()

# --- 1. Memuat Data Referensi (Nama Konsultan & No Konsultan) ---
df_names = pd.read_csv('train_data.csv', dtype=str, low_memory=False)


# Membuat dictionary Nama -> No Konsultan
name_to_id_mapping = {
    row['Nama_konsultan'].strip().upper(): row['Nama_konsultan']
    for _, row in df_names.iterrows()
    if pd.notna(row['Nama_konsultan']) and row['Nama_konsultan'].strip() != ''
}

# Membuat daftar nama resmi konsultan untuk fuzzy matching
official_names = list(name_to_id_mapping.keys())


# --- 2. Fungsi Fuzzy Matching Nama Orang ---
def fuzzy_match_name(text, official_names, fuzzy_threshold=85):
    text = text.upper().strip()
    
    best_match, score, _ = process.extractOne(text, official_names, scorer=fuzz.token_sort_ratio)
    if score >= fuzzy_threshold:
        matched_name = best_match
        consultant_id = name_to_id_mapping[matched_name]  # Ambil No Konsultan dari dictionary
        return matched_name, consultant_id
    return None, None


# --- 3. FastAPI Model Input ---
class InputData(BaseModel):
    Nama_Konsultan: str
    No_Konsultan: str
    Alamat_Korespondensi: str
    Email: str
    No_Telp: str


# --- 4. Endpoint FastAPI untuk Membersihkan Nama Konsultan ---
@app.post("/clean/")
async def clean_name(data: InputData):
    matched_name, consultant_id = fuzzy_match_name(data.Nama_Konsultan, official_names)

    return {
        "clean_text_nama": matched_name if matched_name else data.Nama_Konsultan,
        "clean_no_konsultan": consultant_id if consultant_id else data.No_Konsultan
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

