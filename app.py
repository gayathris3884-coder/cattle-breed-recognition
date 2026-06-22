import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import os

st.set_page_config(
    page_title="PashuPehchan",
    page_icon="🐄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BREED_INFO = {
    "Gir":              {"origin":"Gir Forest, Gujarat",        "category":"Dairy · Indigenous Cattle", "milk_yield":"6–8 L/day",   "characteristics":"Distinctive curved horns, long pendulous ears, convex forehead. Highly heat-tolerant and disease-resistant.", "icar":"IN-GI-001","emoji":"🐄","tag":"Indigenous"},
    "Sahiwal":          {"origin":"Punjab (India & Pakistan)",   "category":"Dairy · Indigenous Cattle", "milk_yield":"8–12 L/day",  "characteristics":"Loose skin, short horns, reddish-brown coat. One of the best dairy breeds in tropical Asia.",              "icar":"IN-SA-002","emoji":"🐄","tag":"Indigenous"},
    "Red Sindhi":       {"origin":"Sindh region",               "category":"Dairy · Indigenous Cattle", "milk_yield":"5–7 L/day",   "characteristics":"Deep red coat, medium-sized, tick-resistant. Adapts well to tropical climates.",                            "icar":"IN-RS-003","emoji":"🐄","tag":"Indigenous"},
    "Tharparkar":       {"origin":"Thar Desert, Rajasthan",     "category":"Dual Purpose · Indigenous", "milk_yield":"4–6 L/day",   "characteristics":"White to grey coat, medium horns, extremely drought-hardy and heat-resistant.",                             "icar":"IN-TH-004","emoji":"🐄","tag":"Indigenous"},
    "Holstein Friesian":{"origin":"Netherlands / North Germany","category":"Dairy · Exotic Cattle",     "milk_yield":"20–30 L/day", "characteristics":"Black-and-white patches, large frame, highest milk yield among all cattle breeds worldwide.",                "icar":"EX-HF-001","emoji":"🐄","tag":"Exotic"},
    "Jersey":           {"origin":"Jersey Island, UK",          "category":"Dairy · Exotic Cattle",     "milk_yield":"12–18 L/day", "characteristics":"Fawn/brown, small frame, high butterfat milk (5-6%). Adapts well to Indian climate.",                       "icar":"EX-JR-002","emoji":"🐄","tag":"Exotic"},
    "Murrah":           {"origin":"Haryana",                    "category":"Dairy · Indigenous Buffalo","milk_yield":"10–16 L/day", "characteristics":"Jet-black body, tightly coiled horns. World's highest milk-yielding buffalo breed.",                        "icar":"BU-MU-001","emoji":"🐃","tag":"Buffalo"},
    "Jaffrabadi":       {"origin":"Jaffrabad, Gujarat",         "category":"Dairy · Indigenous Buffalo","milk_yield":"8–12 L/day",  "characteristics":"Massive body, heavy drooping horns, black skin. Largest buffalo breed in India.",                           "icar":"BU-JA-002","emoji":"🐃","tag":"Buffalo"},
    "Nili Ravi":        {"origin":"Sutlej Valley, Punjab",      "category":"Dairy · Indigenous Buffalo","milk_yield":"9–14 L/day",  "characteristics":"Black with white face/leg markings, blue wall eyes, high milk fat content.",                               "icar":"BU-NR-003","emoji":"🐃","tag":"Buffalo"},
}

CLASS_NAMES = ["Gir","Holstein Friesian","Jaffrabadi","Jersey","Murrah","Nili Ravi","Red Sindhi","Sahiwal","Tharparkar"]
IMG_SIZE    = (224, 224)
MODEL_PATH  = os.path.join("models", "fine_tuned_model.keras")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&family=Outfit:wght@400;500;600;700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body, [class*="css"] { font-family: 'Outfit', sans-serif !important; background: #0F1419 !important; }
[data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #0F1419 0%, #1a1f2e 100%) !important; }
[data-testid="stHeader"] { background: transparent !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }

::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: #1a1f2e; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #3b82f6, #1e40af); border-radius: 5px; }

[data-testid="stFileUploader"] { background: transparent !important; }
[data-testid="stFileUploader"] > div { border: 2px dashed #3b82f6 !important; background: rgba(59, 130, 246, 0.05) !important; border-radius: 16px !important; }
[data-testid="stFileUploader"] label { color: #60a5fa !important; font-weight: 700 !important; }
[data-testid="stFileUploaderDropzoneInstructions"] > div > span { color: #93c5fd !important; }
[data-testid="stFileUploaderDropzoneInstructions"] > div > small { color: #3b82f6 !important; }
[data-testid="stBaseButton-secondary"] { background: rgba(59, 130, 246, 0.2) !important; color: #60a5fa !important; border: 1px solid #3b82f6 !important; border-radius: 10px !important; font-weight: 700 !important; transition: all 0.3s !important; }
[data-testid="stBaseButton-secondary"]:hover { background: rgba(59, 130, 246, 0.3) !important; transform: translateY(-2px) !important; }

[data-testid="stExpander"] { background: rgba(30, 41, 59, 0.8) !important; border: 1px solid rgba(59, 130, 246, 0.3) !important; border-radius: 14px !important; }
[data-testid="stExpander"] summary { color: #60a5fa !important; font-weight: 700 !important; font-size: 14px !important; }
[data-testid="stExpanderDetails"] { background: rgba(15, 20, 25, 0.9) !important; }

[data-testid="stSelectbox"] > div > div { background: rgba(30, 41, 59, 0.8) !important; border: 1px solid rgba(59, 130, 246, 0.3) !important; color: #93c5fd !important; border-radius: 12px !important; }
[data-testid="stDataFrame"] { background: rgba(30, 41, 59, 0.8) !important; }
[data-testid="stSpinner"] > div { color: #60a5fa !important; }

@keyframes slideIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.7; } }
@keyframes gradientShift { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }

.header-bar {
    background: linear-gradient(135deg, #3b82f6 0%, #1e40af 50%, #0c4a6e 100%);
    padding: 24px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid rgba(59, 130, 246, 0.3);
    animation: slideIn 0.6s ease-out;
    box-shadow: 0 20px 40px rgba(59, 130, 246, 0.2);
}
.hb-left { display: flex; align-items: center; gap: 16px; }
.hb-icon {
    width: 52px; height: 52px; border-radius: 16px;
    background: linear-gradient(135deg, #60a5fa, #3b82f6);
    display: flex; align-items: center; justify-content: center;
    font-size: 28px;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4);
    animation: pulse 3s infinite;
}
.hb-title { font-size: 20px; font-weight: 900; color: #ffffff; letter-spacing: -0.5px; }
.hb-subtitle { font-size: 12px; color: rgba(255, 255, 255, 0.8); margin-top: 2px; font-weight: 600; }
.hb-stats { display: flex; gap: 12px; flex-wrap: wrap; }
.stat-pill {
    background: rgba(255, 255, 255, 0.15);
    color: #e0f2fe;
    border-radius: 999px;
    padding: 6px 16px;
    font-size: 12px;
    font-weight: 700;
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    transition: all 0.3s;
}
.stat-pill:hover { background: rgba(255, 255, 255, 0.25); transform: translateY(-2px); }

.content-wrap {
    display: grid;
    grid-template-columns: 320px 1fr;
    min-height: calc(100vh - 88px);
    gap: 20px;
    padding: 20px;
}
.sidebar {
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(59, 130, 246, 0.2);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 24px;
    animation: slideIn 0.6s ease-out 0.1s both;
    max-height: calc(100vh - 128px);
    overflow-y: auto;
}
.main-area {
    background: rgba(30, 41, 59, 0.4);
    border: 1px solid rgba(59, 130, 246, 0.2);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 32px;
    animation: slideIn 0.6s ease-out 0.2s both;
    overflow-y: auto;
}

.section-label {
    font-size: 12px;
    font-weight: 800;
    color: #60a5fa;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.upload-area {
    border: 2px dashed #3b82f6;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(79, 172, 254, 0.05));
    padding: 40px 20px;
    text-align: center;
    margin-bottom: 20px;
    cursor: pointer;
    transition: all 0.3s;
}
.upload-area:hover {
    border-color: #60a5fa;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(79, 172, 254, 0.1));
    transform: translateY(-2px);
}
.ua-icon { font-size: 40px; margin-bottom: 12px; animation: pulse 2s infinite; }
.ua-title { font-size: 15px; font-weight: 800; color: #e0f2fe; }
.ua-sub { font-size: 12px; color: #93c5fd; margin-top: 4px; }

.info-card {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(79, 172, 254, 0.05));
    border: 1px solid rgba(59, 130, 246, 0.3);
    border-radius: 14px;
    padding: 18px;
    margin-top: 20px;
    backdrop-filter: blur(10px);
    animation: slideIn 0.6s ease-out 0.3s both;
}
.ic-header { font-size: 11px; font-weight: 800; color: #60a5fa; text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 14px; }
.ic-row {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    border-bottom: 1px solid rgba(59, 130, 246, 0.2);
    font-size: 13px;
}
.ic-row:last-child { border-bottom: none; }
.ic-label { color: #93c5fd; }
.ic-value { color: #e0f2fe; font-weight: 800; }

.breed-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 6px;
    cursor: pointer;
    transition: all 0.3s;
    background: transparent;
}
.breed-item:hover {
    background: rgba(59, 130, 246, 0.2);
    transform: translateX(4px);
}
.bi-left { display: flex; align-items: center; gap: 10px; }
.bi-name { font-size: 14px; font-weight: 700; color: #e0f2fe; }
.bi-origin { font-size: 11px; color: #93c5fd; }
.bi-tag { font-size: 10px; font-weight: 800; padding: 3px 10px; border-radius: 999px; white-space: nowrap; }
.tag-ind { background: linear-gradient(135deg, rgba(59, 130, 246, 0.3), rgba(79, 172, 254, 0.2)); color: #60a5fa; border: 1px solid #3b82f6; }
.tag-exo { background: linear-gradient(135deg, rgba(168, 85, 247, 0.3), rgba(192, 132, 250, 0.2)); color: #d8b4fe; border: 1px solid #a855f7; }
.tag-buf { background: linear-gradient(135deg, rgba(249, 115, 22, 0.3), rgba(253, 186, 116, 0.2)); color: #fed7aa; border: 1px solid #f97316; }

.result-card {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(79, 172, 254, 0.05));
    border: 1px solid rgba(59, 130, 246, 0.3);
    border-radius: 18px;
    padding: 32px;
    margin-bottom: 28px;
    animation: slideIn 0.6s ease-out;
    backdrop-filter: blur(10px);
}
.rc-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 24px; gap: 16px; }
.rc-left { flex: 1; }
.rc-breed { font-size: 40px; font-weight: 900; background: linear-gradient(135deg, #60a5fa, #93c5fd); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1; }
.rc-category { font-size: 14px; color: #93c5fd; margin-top: 6px; font-weight: 600; }
.rc-badge {
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.3), rgba(74, 222, 128, 0.2));
    color: #86efac;
    font-size: 11px;
    font-weight: 800;
    padding: 8px 16px;
    border-radius: 999px;
    white-space: nowrap;
    border: 1px solid rgba(34, 197, 94, 0.5);
}
.rc-badge.med {
    background: linear-gradient(135deg, rgba(249, 115, 22, 0.3), rgba(253, 186, 116, 0.2));
    color: #fed7aa;
    border-color: rgba(249, 115, 22, 0.5);
}
.rc-badge.low {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.3), rgba(252, 165, 165, 0.2));
    color: #fca5a5;
    border-color: rgba(239, 68, 68, 0.5);
}

.confidence-section { margin-bottom: 28px; }
.conf-large {
    font-size: 64px;
    font-weight: 900;
    background: linear-gradient(135deg, #60a5fa, #93c5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
    animation: slideIn 0.6s ease-out 0.2s both;
}
.conf-large.med {
    background: linear-gradient(135deg, #f97316, #fb923c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.conf-large.low {
    background: linear-gradient(135deg, #ef4444, #f87171);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.conf-label { font-size: 13px; color: #93c5fd; margin-top: 8px; font-weight: 700; }

.progress-bar {
    background: rgba(59, 130, 246, 0.2);
    border-radius: 999px;
    height: 10px;
    margin-top: 16px;
    overflow: hidden;
    border: 1px solid rgba(59, 130, 246, 0.3);
}
.progress-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #60a5fa, #93c5fd);
    transition: width 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    box-shadow: 0 0 20px rgba(96, 165, 250, 0.6);
}
.progress-fill.med { background: linear-gradient(90deg, #f97316, #fb923c); box-shadow: 0 0 20px rgba(249, 115, 22, 0.6); }
.progress-fill.low { background: linear-gradient(90deg, #ef4444, #f87171); box-shadow: 0 0 20px rgba(239, 68, 68, 0.6); }

.details-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 16px;
    margin-top: 28px;
}
.detail-box {
    background: linear-gradient(135deg, rgba(79, 172, 254, 0.1), rgba(59, 130, 246, 0.05));
    border: 1px solid rgba(59, 130, 246, 0.2);
    border-radius: 12px;
    padding: 16px;
    transition: all 0.3s;
}
.detail-box:hover { transform: translateY(-4px); border-color: rgba(59, 130, 246, 0.4); }
.db-label { font-size: 11px; color: #93c5fd; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; }
.db-value { font-size: 16px; font-weight: 900; color: #60a5fa; margin-top: 8px; }

.char-box {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(79, 172, 254, 0.05));
    border-left: 4px solid #3b82f6;
    border-radius: 0 12px 12px 0;
    padding: 16px 18px;
    font-size: 14px;
    color: #93c5fd;
    line-height: 1.8;
    margin-top: 28px;
    border: 1px solid rgba(59, 130, 246, 0.2);
    border-left: 4px solid #60a5fa;
}

.section-title {
    font-size: 12px;
    font-weight: 800;
    color: #60a5fa;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 28px 0 16px;
}

.alt-item {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(79, 172, 254, 0.05));
    border: 1px solid rgba(59, 130, 246, 0.2);
    border-radius: 12px;
    padding: 14px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
    transition: all 0.3s;
}
.alt-item:hover {
    transform: translateX(4px);
    border-color: rgba(59, 130, 246, 0.5);
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(79, 172, 254, 0.1));
}
.ai-left { display: flex; align-items: center; gap: 12px; }
.ai-dot { width: 8px; height: 8px; border-radius: 50%; background: linear-gradient(135deg, #60a5fa, #3b82f6); }
.ai-name { font-size: 14px; font-weight: 700; color: #e0f2fe; }
.ai-cat { font-size: 12px; color: #93c5fd; }
.ai-pct { font-size: 18px; font-weight: 900; background: linear-gradient(135deg, #60a5fa, #93c5fd); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

.empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 450px;
    text-align: center;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(79, 172, 254, 0.05));
    border: 1px dashed rgba(59, 130, 246, 0.3);
    border-radius: 18px;
}
.es-icon { font-size: 60px; color: rgba(59, 130, 246, 0.4); margin-bottom: 20px; animation: pulse 2s infinite; }
.es-title { font-size: 18px; font-weight: 800; color: #e0f2fe; }
.es-desc { font-size: 13px; color: #93c5fd; margin-top: 10px; }

.footer-text {
    text-align: center;
    color: rgba(147, 197, 253, 0.6);
    font-size: 12px;
    padding: 20px;
    border-top: 1px solid rgba(59, 130, 246, 0.2);
    margin-top: 40px;
    font-weight: 600;
}

/* Scrollbar for sidebar and main */
.sidebar::-webkit-scrollbar-thumb,
.main-area::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #60a5fa, #3b82f6) !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        return tf.keras.models.load_model(MODEL_PATH)
    return None

model = load_model()

def preprocess(img):
    img = img.convert("RGB").resize(IMG_SIZE)
    arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img, dtype=np.float32))
    return np.expand_dims(arr, 0)

# ── Header ──
st.markdown("""
<div class="header-bar">
  <div class="hb-left">
    <div class="hb-icon">🐄</div>
    <div>
      <div class="hb-title">PashuPehchan</div>
      <div class="hb-subtitle">Cattle & Buffalo Breed Recognizer</div>
    </div>
  </div>
  <div class="hb-stats">
    <span class="stat-pill">MobileNetV2</span>
    <span class="stat-pill">1,997 images</span>
    <span class="stat-pill">72% accuracy</span>
    <span class="stat-pill">9 breeds</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Layout ──
left, right = st.columns([1, 2.4], gap="small")

# ── LEFT SIDEBAR ──
with left:
    st.markdown('<div class="section-label">📷 Upload image</div>', unsafe_allow_html=True)
    
    uploaded = st.file_uploader("img", type=["jpg","jpeg","png"], label_visibility="collapsed")
    
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, use_container_width=True)
    else:
        st.markdown("""
        <div class="upload-area">
          <div class="ua-icon">⬆️</div>
          <div class="ua-title">Drop image here</div>
          <div class="ua-sub">JPG or PNG • Max 200MB</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
      <div class="ic-header">Model Information</div>
      <div class="ic-row"><span class="ic-label">Architecture</span><span class="ic-value">MobileNetV2</span></div>
      <div class="ic-row"><span class="ic-label">Framework</span><span class="ic-value">TensorFlow</span></div>
      <div class="ic-row"><span class="ic-label">Test accuracy</span><span class="ic-value">72.00%</span></div>
      <div class="ic-row"><span class="ic-label">Val accuracy</span><span class="ic-value">75.92%</span></div>
      <div class="ic-row"><span class="ic-label">Total images</span><span class="ic-value">1,997</span></div>
      <div class="ic-row"><span class="ic-label">Breeds</span><span class="ic-value">9</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-label" style="margin-top:20px;">📚 Breed Directory</div>', unsafe_allow_html=True)
    
    with st.expander("Browse all breeds", expanded=False):
        opts = ["All breeds","Indigenous Cattle","Exotic Cattle","Buffalo"]
        sel  = st.selectbox("Filter", opts, label_visibility="collapsed")
        fmap = {
            "All breeds": list(BREED_INFO.keys()),
            "Indigenous Cattle": ["Gir","Sahiwal","Red Sindhi","Tharparkar"],
            "Exotic Cattle": ["Holstein Friesian","Jersey"],
            "Buffalo": ["Murrah","Jaffrabadi","Nili Ravi"],
        }
        tcls = {"Indigenous":"tag-ind","Exotic":"tag-exo","Buffalo":"tag-buf"}
        for b in fmap[sel]:
            bi = BREED_INFO[b]
            tc = tcls[bi["tag"]]
            st.markdown(f"""
            <div class="breed-item">
              <div class="bi-left">
                <span style="font-size:18px;">{bi['emoji']}</span>
                <div>
                  <div class="bi-name">{b}</div>
                  <div class="bi-origin">{bi['origin']}</div>
                </div>
              </div>
              <span class="bi-tag {tc}">{bi['tag']}</span>
            </div>""", unsafe_allow_html=True)

# ── RIGHT MAIN AREA ──
with right:
    st.markdown('<div class="section-label">🔍 Prediction Result</div>', unsafe_allow_html=True)
    
    if uploaded and model:
        with st.spinner("Analysing image..."):
            preds = model.predict(preprocess(img), verbose=0)[0]
        top3 = np.argsort(preds)[::-1][:3]
        top_breed = CLASS_NAMES[top3[0]]
        top_conf  = float(preds[top3[0]]) * 100
        info = BREED_INFO[top_breed]

        if top_conf >= 80:
            cc, bc, bt = "", "", "High confidence"
        elif top_conf >= 50:
            cc, bc, bt = " med", " med", "Moderate confidence"
        else:
            cc, bc, bt = " low", " low", "Low confidence"

        st.markdown(f"""
        <div class="result-card">
          <div class="rc-header">
            <div class="rc-left">
              <div class="rc-breed">{info['emoji']} {top_breed}</div>
              <div class="rc-category">{info['category']}</div>
            </div>
            <span class="rc-badge{bc}">{bt}</span>
          </div>
          
          <div class="confidence-section">
            <div class="conf-large{cc}">{top_conf:.1f}%</div>
            <div class="conf-label">Confidence score</div>
            <div class="progress-bar">
              <div class="progress-fill{cc}" style="width:{min(top_conf,100):.0f}%"></div>
            </div>
          </div>
          
          <div class="details-grid">
            <div class="detail-box"><div class="db-label">Origin</div><div class="db-value">{info['origin']}</div></div>
            <div class="detail-box"><div class="db-label">Milk yield</div><div class="db-value">{info['milk_yield']}</div></div>
            <div class="detail-box"><div class="db-label">ICAR code</div><div class="db-value">{info['icar']}</div></div>
          </div>
          
          <div class="char-box">{info['characteristics']}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-title">Other possibilities</div>', unsafe_allow_html=True)
        for idx in top3[1:]:
            b  = CLASS_NAMES[idx]
            c  = float(preds[idx]) * 100
            bi = BREED_INFO[b]
            st.markdown(f"""
            <div class="alt-item">
              <div class="ai-left">
                <div class="ai-dot"></div>
                <div>
                  <div class="ai-name">{bi['emoji']} {b}</div>
                  <div class="ai-cat">{bi['category']}</div>
                </div>
              </div>
              <div class="ai-pct">{c:.1f}%</div>
            </div>""", unsafe_allow_html=True)

        with st.expander("View all breed probabilities"):
            import pandas as pd
            df = pd.DataFrame({
                "Breed": CLASS_NAMES,
                "Confidence (%)": [round(float(p)*100, 1) for p in preds]
            }).sort_values("Confidence (%)", ascending=False).reset_index(drop=True)
            st.dataframe(df, use_container_width=True, hide_index=True)

    elif uploaded and not model:
        st.error("Model not found at models/fine_tuned_model.keras — check the path.")
    else:
        st.markdown("""
        <div class="empty-state">
          <div class="es-icon">🔍</div>
          <div class="es-title">Waiting for image</div>
          <div class="es-desc">Upload a cattle or buffalo photo<br>on the left to see prediction</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="footer-text">PashuPehchan · MobileNetV2 + TensorFlow + Streamlit · 9 Indian bovine breeds · For BPA field use</div>', unsafe_allow_html=True)